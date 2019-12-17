#!/usr/bin/env python
import os, sys
 
header = "# .PCD v.7 - Point Cloud Data file format\n\
FIELDS x y z rgb\n\
SIZE 4 4 4 1\n\
TYPE F F F F\n\
COUNT 1 1 1 1\n\
WIDTH XXXX\n\
HEIGHT 1\n\
VIEWPOINT 0 0 0 1 0 0 0\n\
POINTS XXXX\n\
DATA ascii"
 
def convertPLYToPCD(mesh_file, pcd_file):
    input_file = open(mesh_file)
    out = pcd_file
    output_file = open(out, 'w')
    write_points = False
    points_counter = 0
    nr_points = 0
    for s in input_file.readlines():
        print("In!!!!!!!")
        if s.find("element vertex") != -1:
            nr_points = int(s.split(" ")[2].rstrip().lstrip())
            new_header = header.replace("XXXX", str(nr_points))
            output_file.write(new_header)
            print(new_header)	
            output_file.write("\n")
        if s.find("end_header") != -1:
            write_points = True
            continue
        if write_points and points_counter < nr_points:
            points_counter = points_counter + 1
            output_file.write(" ".join(s.split(" ", 4)[:4]))
            print(" ".join(s.split(" ", 4)[:4]))
            output_file.write("\n")
    input_file.close()
    output_file.close()
 
def usage():
     print "\nUsage: python ", sys.argv[0], "<input_mesh.ply> <output_cloud.pcd> \n"
 
if __name__ == "__main__":
    if sys.argv.__len__() != 3:
        usage()
        sys.exit(2)
    mesh_file = sys.argv[1]
    pcd_file = sys.argv[2]
    convertPLYToPCD(mesh_file, pcd_file)
