def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >=0:
		return x
	else:
		return -x
def my_age(x):
	if x >= 18:
		return 'adult'
	else:
		return 'teenager'

print(my_abs('o'))
print(my_abs(3))
print(my_age(32))