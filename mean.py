
import os
import numpy as np
import matplotlib.pyplot as plt


data_list = [] # empty list
torque_x_list = []
torque_mean_list = []

for i in range(11):
    data_list.append(np.loadtxt('gear{0}_info_0.txt'.format(i)))
    torque_x_list.append(data_list[i][:,10])
    torque_mean_list.append(np.mean(data_list[i][1000:-1,10]))

torque_mean = np.sum(np.abs(torque_mean_list))

print(torque_mean)





