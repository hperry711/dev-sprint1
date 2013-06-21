# This is where Exercise 5.4 goes
# Name: Hunter Perry
def is_triangle (x,y,z):
	if (x+y)<z:
		print "No"
	elif (y+z)<x:
		print "No"
	elif (z+x)<y:
		print "No"
	else:
		print "Yes"
is_triangle (5,4,7)
