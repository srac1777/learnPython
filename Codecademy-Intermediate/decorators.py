def title_decorator(printfn):
	def wrapper():
		print("hi")
		printfn()
	return wrapper

@title_decorator
def my_printfn():
	print("shashank")


# decorated_name = title_decorator(my_printfn)
# print(decorated_name())
print(my_printfn())
