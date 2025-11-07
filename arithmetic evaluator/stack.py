class Stack:
	def __init__(self):
		self.list = []
		# Initialise the stack's data attributes
		pass
	
	def push(self, item):
		self.list.insert(0,item)
		# Push an item to the stack
		pass

	def peek(self):
		if len(self.list)>0:
			return self.list[0]
		else:
			return "Error"
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		pass

	def pop(self):
		if len(self.list)>0:
			self.list.pop(0)
		# Pop an item from the stack if non-empty
		pass

	def is_empty(self):
		return len(self.list)==0
		# Return True if stack is empty, False otherwise
		pass

	def __str__(self):
		s = ""
		for i in self.list:
			s = s + str(i) + " "
		s = s[:len(s)-1]
		return s
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		pass
	
	def list_(self):
		return self.list
	
	def __len__(self):
		return len(self.list)
		# Return current number of elements in the stack
		pass