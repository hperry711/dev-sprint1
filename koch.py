#5.6 Koch Curve
#Hunter Perry

world.clear()
bob = Turtle()
def koch (t, l):
	
	if l < 10:
		fd (t, l)
		return  
	n = l/3.0
	koch (t, n)
	lt (t, 60)
	koch (t, n)
	rt (t, 120)
	koch (t, n)
	lt (t, 60)
	koch (t, n)

def snowflake (t, l):
	for i in range (3):
		koch (bob, length)
		rt (bob, 120)

bob = Turtle()
length = 100
bob.delay = 0.00001
 
snowflake (bob, length)

