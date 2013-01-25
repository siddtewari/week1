# This is where Exercise 5.4 goes
# Name: Sidd Tewari

# Triangles

def is_triangle(a,b,c):
	if (a <= 0 or b <= 0 or c <= 0):
		print 'Please enter only positive numbers'
	else:
		if (a > (b + c)) or (b > (c + a)) or (c > (a + b)):
			print 'No'
		else:
			print 'Yes'

#is_triangle(1,2,3)
#is_triangle(8,2,1)
#is_triangle(3,4,7)
#is_triangle(3,4,8)

def get_lengths():
	x = input("Please enter the first side of the triangle: ")
	y = input("Please enter the second side of the triangle: ")
	z = input("Please enter the third side of the triangle: ")
	is_triangle(int(x),int(y),int(z))
	#is_triangle(x,y,z)

get_lengths()

