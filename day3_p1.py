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
valid_triangles = 0
ttl_triangles = 0
for triangle in triangles:
	ttl_triangles += 1
	tri = triangle.split()
	if test_triangle(tri):
		valid_triangles += 1

print('Tested triangles: %s' % ttl_triangles)
print('Valid triangles: %s' % valid_triangles)