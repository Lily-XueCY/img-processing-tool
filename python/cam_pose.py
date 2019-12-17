f = open('/home/lilyxue/dense/images.txt', 'r')
out = ""
for line in f.readlines():
	if ".jpg" in line:
		out += line
f_out = open('/home/lilyxue/traj.txt', 'w')
f_out.write(out)
f.close()
f_out.close()