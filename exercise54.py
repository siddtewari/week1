# This is where Exercise 5.4 goes
# Name: Sidd Tewari

def is_triangle(a,b,c):
	"""Evaluates if a triangle can be formed
	:p,q,r - absolute values of the parameters
	"""
	# taking the absolute values
	p, q, r = abs(a), abs(b), abs(c)
	if (p==0 or q==0 or r==0):
		print '\n Zero, 0, is not an acceptable value. Please renter values \n'
		get_lengths()
	elif (p > (q + r)) or (q > (r + p)) or (r > (p + q)):
		print 'NO ___ :( you shan\'t create the three sided thingie \n'
	else:
		print 'YES!  ... you may create your triangular world \n'

def get_lengths():
	"""Takes input from the user and does a type convert 
	to int to pass as arguments to the function is_triangle
	"""
	x = input("\nPlease enter the first side of the triangle: ")
	y = input("Please enter the second side of the triangle: ")
	z = input("Please enter the third side of the triangle: ")
	is_triangle(int(x),int(y),int(z))

# test to prompt user for input and to evaluate tringularity
get_lengths()