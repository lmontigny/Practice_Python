try: paraview.simple
except: from paraview.simple import *
from numpy import *

timedata=dict()
npdata=dict()
sumdata=dict()
sumdata1=dict()
qldata=dict()
velxdata=dict()
velmeandata=dict()
n=dict()

AnimationScene = GetAnimationScene()
AnimationScene.Caching=False

# --- Parameter ---
H=0.0015;
AnimationScene.GoToFirst() #Comment to start from the current view 
limitTime = 0.09; 
folder='/home/lmontigny/meetingjlocaldata/k8x/k8x-r10a-model1p5/'
#+Change the lengthBox X:1-0 or Y:3-2 or Z:5-4
nClip=10
#Define each clip normal direction 
#------------------

oldtime = -1
newtime = AnimationScene.AnimationTime


for ii in range(1,nClip+1):
  timedata[ii]=[]
  npdata[ii]=[]
  sumdata[ii]=[]
  sumdata1[ii]=[]
  qldata[ii]=[]
  velxdata[ii]=[]
  velmeandata[ii]=[]
  n[ii]=[]

# Normals of each clip
n[1]=[1,0,0]
n[2]=[1,0,0]
n[3]=[1,0,0]
n[4]=[1,0,0]
n[5]=[1,0,0]
n[6]=[-0.9,0,-0.45]
n[7]=[-0.707,0,-0.707]
n[8]=[-0.707,0,-0.707]
n[9]=[-0.707,0,-0.707]
n[10]=[-0.707,0,-0.707]


while newtime>oldtime:
  View = GetRenderView()
  Render()

  for i in range(1,nClip+1):	  
    clip = FindSource("Clip"+str(i))	  
    data = servermanager.Fetch(clip);
    np = data.GetNumberOfPoints();

    #--- Parameters ---
    lengthBox =  abs(data.GetBounds()[1] -  data.GetBounds()[0]);
    #lengthBox =  0.02; #Same length for each clip
    #if (i == 9) or (i == 10):
    #  lengthBox = 0.0135

    sum = 0.;
    velmean = 0;
    for j in xrange(np):
      rho  = data.GetPointData().GetArray('Rho').GetValue(j);
      vel = data.GetPointData().GetArray('Vel').GetTuple(j);
      velx = vel[0]
      vely = vel[1]
      velz = vel[2]
      Vol  = H**3;

      sum += Vol * (velx*n[i][0] + vely*n[i][1] + velz*n[i][2]);
      velmean += sqrt(velx**2 + vely**2 + velz**2);

    # --- Debug ---
    #velxdata.append(velx);
    #savetxt('/home/lmontigny/tmp/massflow/pvVelDebug.txt', column_stack((velxdata)))
    
    if np != 0:
      velmean /= np;
    else:
      velmean = 0;
  
    sum1=sum;
    if lengthBox != 0:
      sum /=  lengthBox;
    else:
      sum = 0;
  
    ql = sum*1000*60;
  
    sumdata[i].append(sum);
    sumdata1[i].append(sum1);
    qldata[i].append(ql);
    npdata[i].append(np);
    velmeandata[i].append(velmean);
    timedata[i].append(GetActiveView().ViewTime);
  
    savetxt(folder+'pvMassFlow_oil'+str(i)+'.txt', column_stack((timedata[i],npdata[i],sumdata[i],qldata[i],velmeandata[i],sumdata1[i])))

  AnimationScene.GoToNext()
  oldtime = newtime
  newtime = AnimationScene.AnimationTime
  if newtime > limitTime:
    break

print 'DONE with Q=' + str(ql) + ' l/min'
