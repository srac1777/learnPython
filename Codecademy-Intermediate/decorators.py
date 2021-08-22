def title_decorator(printfn):
	def wrapper(*args, **kwargs):
		print("hi")
		printfn(*args, **kwargs)
	return wrapper

@title_decorator
def my_printfn(name):
	print(name)


# decorated_name = title_decorator(my_printfn)
# print(decorated_name())
print(my_printfn("shashank"))
