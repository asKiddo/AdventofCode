def test_triangle(sides):
	sides = [int(x) for x in sides]
	sides.sort()
	if sides[0] + sides[1] > sides[2]:
		return True
	else:
		return False

#File
fl = open('day3_triangles.txt')
fl_str = fl.read()
fl.close()

triangles = fl_str.split('\n')
test_tri = list()
valid_triangles = 0
ttl_triangles = 0
for triangle in triangles:
	test_tri.append([int(x) for x in triangle.split()])

for i in range(int(len(test_tri)/3)):
	for j in range(3):
		tri = [test_tri[i*3][j],test_tri[i*3+1][j],test_tri[i*3+2][j]]
		ttl_triangles +=1
		if test_triangle(tri):
			valid_triangles += 1

print('Tested triangles: %s' % ttl_triangles)
print('Valid triangles: %s' % valid_triangles)