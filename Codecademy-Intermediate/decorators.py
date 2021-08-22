def title_decorator(printfn):
	def wrapper():
		print("hi")
		printfn()
	return wrapper


def my_printfn():
	print("shashank")


decorated_name = title_decorator(my_printfn)
print(decorated_name())
