# This is where Exercise 5.4 goes
# Name: Sidd Tewari

# Triangles

def is_triangle(a,b,c):
	if (a > (b + c)) or (b > (c + a)) or (c > (a + b)):
		print 'No'
	else:
		print 'Yes'

is_triangle(1,2,3)
is_triangle(8,2,1)
is_triangle(3,4,7)
is_triangle(3,4,8)
