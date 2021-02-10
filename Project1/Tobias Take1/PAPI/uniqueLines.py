def lineSort(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	numbers = []
	for line in lines:
		if line not in numbers:
			numbers.append(line)
	numbers.sort()
	f1 = open("newFile.txt","w")
	for a in numbers:
		f1.write(a)
	f1.flush()
	f1.close()
	
def line(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	numbers = []
	for line in lines:
		if line not in numbers:
			numbers.append(line)
	f1 = open("newFile.txt","w")
	for a in numbers:
		f1.write(a)
	f1.flush()
	f1.close()
