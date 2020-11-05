import imageio 

path = '.\\figs_n100\\'

# im = imageio.imread(path+'foo_real_0.000000.png')

# imageio.imwrite(path+'aaa_test.png', im)

file1 = open(path+'filename.txt', 'r')
count = 0 
images = []
# line = file1.readline().rstrip()
 
while True: 
	count += 1 
	line = file1.readline().rstrip()
	if not line: 
		break 
	images.append(imageio.imread(path+line))
	print(line)
file1.close() 
imageio.mimsave(path+'movie.gif', images)
