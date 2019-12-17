import os
path_name='/home/lilyxue/Downloads/IMG_9167_frames'
i=0
for item in os.listdir(path_name):
    num = item[14:].lstrip('0')
    os.rename(os.path.join(path_name,item),os.path.join(path_name,('image'+num)))
    i+=1


