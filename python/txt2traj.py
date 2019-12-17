#!/usr/bin/env python
import os, sys
 
 
def convertTXTToPCD(txt_file, pcd_file):
    content = "# .PCD v.7 - Point Cloud Data file format\n\
VERSION .7\n\
FIELDS x y z rgb\n\
SIZE 4 4 4 4\n\
TYPE F F F F\n\
COUNT 1 1 1 1\n\
WIDTH XXXX\n\
HEIGHT 1\n\
VIEWPOINT 0 0 0 1 0 0 0\n\
POINTS XXXX\n\
DATA ascii\n"

    input_file = open(txt_file)
    out = pcd_file
    output_file = open(out, 'w')
    count = 0
    print(content)
    for s in input_file.readlines():
        if "#" not in s:
            count += 1
            s = s.split(" ")
            content += "%.5f %.5f %.5f %.4e\n" % (float(s[1]), float(s[2]), float(s[3]), 256 * 256 * int(s[4]) + 256 * int(s[5]) +int(s[6]))
    content.replace("XXXX", str(count), 2)

    print(content)
    output_file.write(content)
    input_file.close()
    output_file.close()
 
def usage():
     print "\nUsage: python ", sys.argv[0], "<input.txt> <output_cloud.pcd> \n"
 
if __name__ == "__main__":
    if sys.argv.__len__() != 3:
        usage()
        sys.exit(2)
    txt_file = sys.argv[1]
    pcd_file = sys.argv[2]
    convertTXTToPCD(txt_file, pcd_file)
