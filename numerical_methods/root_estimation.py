from math import exp

def f(x):
	return 1 - (400/(9.81*(3*x + (x*x)/2)**3))*(x+3)

def fp(x):
	return -exp(-x) - 1

def slope(xa,xb):
	return (f(xb) - f(xa))/(xb-xa)

def secant(x0, x1):
	m1 = slope(x0,x1)
	print('m1 is ', m1)

	x2 = x1 - (f(x1)/m1)
	print('x2 is ', x2)
	print(f(x2))

	m2 = slope(x1,x2)
	print('m2 is ', m2)

	x3= x2 - (f(x2)/m2)

	print('x3 is ', x3)
	print(f(x3))
	m3 = slope(x2,x3)
	print('m3 is ', m3)

	x4 = x3 - (f(x3)/m3)

	print('x4 is ', x4)
	print(f(x4))

def newtonraphson(x0):
	x = x0
	for i in range(0,4):
		y = f(x)
		print('x{} is {}'.format(i, x))
		print('f(x{}) is {}'.format(i,y))
		yp = fp(x)
		print('fp(x{}) is {}'.format(i, yp))
		x= x - (y/yp)

def false_position(a, b, MAX_ITER):
	if f(a) * f(b) >= 0:
		print("You have not assumed right a and b")
		return -1

	c = a # Initialize result

	for i in range(MAX_ITER):
		m = slope(a,b)
		# Find the point that touches x axis
		fa = f(a)
		fb = f(b)
		c = b - (fb/m)
		fc = f(c)

		print(i)
		print('a is {}\nb is {}'.format(a,b))
		print('f(a) is {}'.format(fa))
		print('f(b) is {}\n'.format(fb))
		print('new c value of {} f(c) = {}\n------\n\n'.format(c, fc))


		if fa * fc < 0:
			b = c
			fb = fc
		else:
			a = c
			fa = fc

def bisection(a, b, iterations):
	for i in range(iterations):
		midpoint = (a+b)/2
		fa = f(a)
		fb = f(b)
		fm = f(midpoint)
		print(f'a is {a}\nb is {b}\nmidpoint is {midpoint}, f(m) = {fm}')
		if fb * fm < 0:
			a = midpoint
		else:
			b = midpoint

# false_position(1.5,2.5, 4)
bisection(.5,2.5,4)
