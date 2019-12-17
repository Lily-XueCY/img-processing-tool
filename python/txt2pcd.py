#!/usr/bin/env python
import os, sys
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
 
 
def draw(txt_file, image_file):
    input_file = open(txt_file)
    # out = image_file
    # output_file = open(out, 'w')
    count = 0
    x = []
    y = []
    z = []
    for s in input_file.readlines():
        if "#" not in s and ".jpg" in s:
            print(s)
            count += 1
            s = s.split(" ")
            # x.append(float(s[5]))
            # y.append(float(s[6]))
            # z.append(float(s[7]))
            z.append(float(s[5]))
            y.append(float(s[6]))
            x.append(float(s[7]))
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("Camera Pose Trajectory")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    figure = ax.plot(x, y, z, c='r')
    plt.savefig(image_file)
    plt.show()
    # print(content)
    # output_file.write(content)
    input_file.close()
    # output_file.close()
 
def usage():
     print "\nUsage: python ", sys.argv[0], "<input.txt> <output_cloud.pcd> \n"
 
if __name__ == "__main__":
    if sys.argv.__len__() != 3:
        usage()
        sys.exit(2)
    txt_file = sys.argv[1]
    pcd_file = sys.argv[2]
    draw(txt_file, pcd_file)
