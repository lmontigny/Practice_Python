def plot_trajectories(x1,x2,ylabel):
    colors = [ '#2D328F', '#F15C19' ]
    label_fontsize = 18
    tick_fontsize = 14
    linewidth = 3

    T = x1.shape[0]
    t = np.arange(0,T)
    plt.plot(t,x1,color=colors[0],linewidth=linewidth,label='R=1')
    plt.plot(t,x2,color=colors[1],linewidth=linewidth,label='R=10')
        
    plt.xlabel('time',fontsize=label_fontsize)
    plt.ylabel(ylabel,fontsize=label_fontsize)
    plt.legend(fontsize=label_fontsize)
    plt.xticks(fontsize=tick_fontsize)
    plt.yticks(fontsize=tick_fontsize)

    plt.grid(True)
    plt.show()
    
plot_trajectories(x_lo[0,:],x_hi[0,:],'Position')
