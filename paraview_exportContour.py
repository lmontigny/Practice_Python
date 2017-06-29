try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

out_folder = "surfaces"

Contour1 = FindSource("Contour1")
disp_contour1 = GetDisplayProperties(Contour1)
#Contour2 = FindSource("Contour2")
#disp_contour2 = GetDisplayProperties(Contour2)
#Contour3 = FindSource("Contour3")
#disp_contour3 = GetDisplayProperties(Contour3)
#Contour4 = FindSource("Contour4")
#disp_contour4 = GetDisplayProperties(Contour4)
#Contour5 = FindSource("Contour5")
#disp_contour5 = GetDisplayProperties(Contour5)

for index in range(1,132):
  RenderView2 = GetRenderView()
  AnimationScene2 = GetAnimationScene()
  AnimationScene2.AnimationTime = index
  Render()


  # FIRST CONTOUR
  disp_contour1.Visibility = 1
#  disp_contour2.Visibility = 0
#  disp_contour3.Visibility = 0
#  disp_contour4.Visibility = 0
#  disp_contour5.Visibility = 0
  out_filename = out_folder + "/contour1_" + "%d" % index + ".x3d"
  exporters = servermanager.createModule("exporters")
  x3dExporter = exporters.X3DExporter(FileName=out_filename)
  x3dExporter.SetView(RenderView2)
  x3dExporter.Write()

  # SECOND CONTOUR
#  disp_contour1.Visibility = 0
#  disp_contour2.Visibility = 1
#  disp_contour3.Visibility = 0
#  disp_contour4.Visibility = 0
#  disp_contour5.Visibility = 0
#  out_filename = out_folder + "/contour2_" + "%d" % index + ".x3d"
#  exporters = servermanager.createModule("exporters")
#  x3dExporter = exporters.X3DExporter(FileName=out_filename)
#  x3dExporter.SetView(RenderView2)
#  x3dExporter.Write()

  # THIRD CONTOUR
#  disp_contour1.Visibility = 0
#  disp_contour2.Visibility = 0
#  disp_contour3.Visibility = 1
#  disp_contour4.Visibility = 0
#  disp_contour5.Visibility = 0
#  out_filename = out_folder + "/contour3_" + "%d" % index + ".x3d"
#  exporters = servermanager.createModule("exporters")
#  x3dExporter = exporters.X3DExporter(FileName=out_filename)
#  x3dExporter.SetView(RenderView2)
#  x3dExporter.Write()

#  # FOURTH CONTOUR
#  disp_contour1.Visibility = 0
#  disp_contour2.Visibility = 0
#  disp_contour3.Visibility = 0
#  disp_contour4.Visibility = 1
#  disp_contour5.Visibility = 0
#  out_filename = out_folder + "/contour4_" + "%d" % index + ".x3d"
#  exporters = servermanager.createModule("exporters")
#  x3dExporter = exporters.X3DExporter(FileName=out_filename)
#  x3dExporter.SetView(RenderView2)
#  x3dExporter.Write()

#  # FIFTH CONTOUR
#  disp_contour1.Visibility = 0
#  disp_contour2.Visibility = 0
#  disp_contour3.Visibility = 0
#  disp_contour4.Visibility = 0
#  disp_contour5.Visibility = 1
#  out_filename = out_folder + "/contour5_" + "%d" % index + ".x3d"
#  exporters = servermanager.createModule("exporters")
#  x3dExporter = exporters.X3DExporter(FileName=out_filename)
#  x3dExporter.SetView(RenderView2)
#  x3dExporter.Write()

