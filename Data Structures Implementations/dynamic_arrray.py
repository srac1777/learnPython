class DynamicArray():
	def __init__(self):
		self.data = [None]
		self.curr_idx = 0
	def append(self, val):
		if self.curr_idx >= len(self.data):
			self.increase_and_append(val)
		self.data[self.curr_idx] = val
		self.curr_idx += 1
		return self.data
	def increase_and_append(self, val):
		new_data = [None]*self.curr_idx*2
		for i in range(0, len(self.data)):
			new_data[i] = self.data[i]
		self.data = new_data

p = DynamicArray()
print(p.data)
print(p.append(3))
print(p.append(1))
print(p.append('v'))
print(p.append('p'))
print(p.append(7))
print(p.data)