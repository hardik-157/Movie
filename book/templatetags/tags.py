from django import template

register = template.Library()

@register.filter
def divide(value, arg):
	try:
		return int(int(value) / int(arg))
	except (ValueError, ZeroDivisionError):
		return None

@register.filter
def modulo(value, arg):
	return int(int(value)%int(arg))

@register.filter
def mul(value, arg):
	return int(int(value)*int(arg))

@register.filter
def update(value,arg):
	print(value)
	value[arg]=1;
	print(value)
	return value
