file1 = open('test.txt','r')

lines = file1.readlines();
for line in lines:
	print(line)
file2 = open('copyTest.txt','a')
for line in lines:
	file2.write(line)
