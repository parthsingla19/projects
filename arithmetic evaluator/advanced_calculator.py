from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		self.input_expression = None
		super().__init__()
		self.tokens = []
		self.ls = []
		self.A = Stack()
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		pass

	def evaluate_expression(self, input_expression):
		check = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","(",")","{","}"," "]
		for checker in input_expression:
			if checker not in check:
				self.A.push((input_expression, "Error"))
				return "Error"
		tokens = self.tokenize(input_expression)
		if tokens is None:
			self.A.push((input_expression,"Error"))
			return "Error"
		if self.check_brackets(tokens) == False:
			self.A.push((input_expression,"Error"))
			return "Error"
		bracket_replacer = 0
		while(bracket_replacer<len(tokens)):
			if tokens[bracket_replacer]=="{":
				tokens[bracket_replacer]="("
			elif tokens[bracket_replacer]=="}":
				tokens[bracket_replacer]=")"
			bracket_replacer = bracket_replacer + 1
		operators = "+-*/"
		brackets = "()"
		def division(list):
			print(list)
			if "/" not in list:
				return list
			else:
				div = list.index("/")
				try:
					div_previous = float(list[div-1])
					div_next = float(list[div + 1])
					if div_next == 0:
						return "Error"
					div_substitute = div_previous/div_next
					list = list[:div-1] + [div_substitute] + list[div+2:]
					return division(list)
				except:
					return "Error"
		def multiplication(list):
			print(list)
			if "*" not in list:
				return list
			else:
				mult = list.index("*")
				try:
					mult_previous = float(list[mult-1])
					mult_next = float(list[mult + 1])
					mult_substitute = mult_previous*mult_next
					list = list[:mult-1] + [mult_substitute] + list[mult+2:]
					return multiplication(list)
				except:
					return "Error"
		def addition(list):
			print(list)
			if "+" not in list and "-" not in list:
				return list
			else:
				try:
					if "+" in list and "-" in list:
						add = list.index("+")
						subtract = list.index("-")
						add_sub = min(add, subtract)
						if add<subtract:
							operation = "+"
						else:
							operation = "-"
					elif "+" in list and "-" not in list:
						add_sub = list.index("+")
						operation = "+"
					elif "-" in list and "+" not in list:
						add_sub = list.index("-")
						operation = "-"
					print(add_sub)
					print(operation)
					add_sub_previous = float(list[add_sub-1])
					add_sub_next = float(list[add_sub + 1])
					if operation == "-":
						add_sub_substitute = add_sub_previous-add_sub_next
						list = list[:add_sub-1] + [add_sub_substitute] + list[add_sub+2:]
					elif operation == "+":
						add_sub_substitute = add_sub_previous + add_sub_next
						list = list[:add_sub-1] + [add_sub_substitute] + list[add_sub+2:]
					return addition(list)
				except:
					return "Error"
		def eval_without_brackets(list):
			if len(list)==1:
				if list[0] is int or float:
					return float(list[0])
			operators = "+-*/"
			if str(list[0]) in operators:
				return "Error"
			elif str(list[len(list)-1]) in operators:
				return "Error"
			div = division(list)
			mult = multiplication(div)
			add = addition(mult)
			return add[0]
		def brackets_problems_to_be_solved(list):
			print(list)
			if "(" in list:
				first_bracket_index = list.index("(")
				last_bracket_index = list.index(")")
				for bracket_finder in range (first_bracket_index + 1,len(list)):
					if list[bracket_finder] == "(":
						first_bracket_index = bracket_finder
					elif list[bracket_finder] == ")":
						break
				if first_bracket_index + 1 == last_bracket_index:
					return "Error"
				else:
					list = list[:first_bracket_index] + [eval_without_brackets(list[(first_bracket_index+1):last_bracket_index])] + list[(last_bracket_index+1):]
					return brackets_problems_to_be_solved(list)
			else:
				return list
		if brackets[0] not in tokens:
			self.A.push((input_expression, eval_without_brackets(tokens)))
			return eval_without_brackets(tokens)
		else:
			tokens_without_brackets = brackets_problems_to_be_solved(tokens)
			self.A.push((input_expression, eval_without_brackets(tokens_without_brackets)))
			return eval_without_brackets(tokens_without_brackets)
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		pass

	def tokenize(self, input_expression):
		a = "+-*/"
		b = "{}()"
		i = 0
		k = []
		while(i<len(input_expression)):
			if input_expression[i]!=" " and input_expression[i] not in a and input_expression[i] not in b:
				j = i + 1
				while(j<len(input_expression) and input_expression[j]!=" " and input_expression[j] not in a and input_expression[j] not in b):
					j = j + 1
				k = k + [int(input_expression[i:j])]
				i = j - 1
			elif input_expression[i]!=" ":
				k = k + [input_expression[i]]
			i = i + 1
		return k
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		pass		

	def check_brackets(self, list_tokens):
		k = []
		a = ["(",")","{","}"]
		for i in list_tokens:
			if i in a:
				k = k + [i]
		b = 0
		c = 0
		i = 0
		while(i<len(k)):
			d = True
			if c>0 and k[i]=="{":
				d = False
				break
			elif b<0 or c<0:
				d = False
				break
			elif k[i]=="{":
				b = b + 1
			elif k[i]=="}":
				b = b - 1
			elif k[i]=="(":
				c = c + 1
			elif k[i]==")":
				c = c - 1
			i = i + 1
		if b!=0 or c!=0:
			d = False
		else:
			d = True
		if d==False:
			return False
		else:
			return True
			
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		pass

	def evaluate_list_tokens(self, list_tokens):
		check = ["+","-","*","/","(",")","{","}"," "]
		for checker in list_tokens:
			if checker not in check:
				if checker%1!=0:
					return "Error"
		if list_tokens is None:
			return "Error"
		if self.check_brackets(list_tokens) == False:
			return "Error"
		bracket_replacer = 0
		while(bracket_replacer<len(list_tokens)):
			if list_tokens[bracket_replacer]=="{":
				list_tokens[bracket_replacer]="("
			elif list_tokens[bracket_replacer]=="}":
				list_tokens[bracket_replacer]=")"
			bracket_replacer = bracket_replacer + 1
		operators = "+-*/"
		brackets = "()"
		def division(list):
			print(list)
			if "/" not in list:
				return list
			else:
				div = list.index("/")
				try:
					div_previous = float(list[div-1])
					div_next = float(list[div + 1])
					if div_next == 0:
						return "Error"
					div_substitute = div_previous/div_next
					list = list[:div-1] + [div_substitute] + list[div+2:]
					return division(list)
				except:
					return "Error"
		def multiplication(list):
			print(list)
			if "*" not in list:
				return list
			else:
				mult = list.index("*")
				try:
					mult_previous = float(list[mult-1])
					mult_next = float(list[mult + 1])
					mult_substitute = mult_previous*mult_next
					list = list[:mult-1] + [mult_substitute] + list[mult+2:]
					return multiplication(list)
				except:
					return "Error"
		def addition(list):
			print(list)
			if "+" not in list and "-" not in list:
				return list
			else:
				try:
					if "+" in list and "-" in list:
						add = list.index("+")
						subtract = list.index("-")
						add_sub = min(add, subtract)
						if add<subtract:
							operation = "+"
						else:
							operation = "-"
					elif "+" in list and "-" not in list:
						add_sub = list.index("+")
						operation = "+"
					elif "-" in list and "+" not in list:
						add_sub = list.index("-")
						operation = "-"
					print(add_sub)
					print(operation)
					add_sub_previous = float(list[add_sub-1])
					add_sub_next = float(list[add_sub + 1])
					if operation == "-":
						add_sub_substitute = add_sub_previous-add_sub_next
						list = list[:add_sub-1] + [add_sub_substitute] + list[add_sub+2:]
					elif operation == "+":
						add_sub_substitute = add_sub_previous + add_sub_next
						list = list[:add_sub-1] + [add_sub_substitute] + list[add_sub+2:]
					return addition(list)
				except:
					return "Error"
		def eval_without_brackets(list):
			if len(list)==1:
				if list[0] is int or float:
					return float(list[0])
			operators = "+-*/"
			if str(list[0]) in operators:
				return "Error"
			elif str(list[len(list)-1]) in operators:
				return "Error"
			div = division(list)
			mult = multiplication(div)
			add = addition(mult)
			return add[0]
		def brackets_problems_to_be_solved(list):
			if "(" in list:
				first_bracket_index = list.index("(")
				last_bracket_index = list.index(")")
				for bracket_finder in range (first_bracket_index + 1,len(list)):
					if list[bracket_finder] == "(":
						first_bracket_index = bracket_finder
					elif list[bracket_finder] == ")":
						break
				if first_bracket_index +2 == last_bracket_index:
					list = list[:first_bracket_index] + [list[first_bracket_index+1]] + list[(last_bracket_index+1):]
					return brackets_problems_to_be_solved(list)
				elif first_bracket_index + 1 == last_bracket_index:
					return "Error"
				else:
					list = list[:first_bracket_index] + [eval_without_brackets(list[(first_bracket_index+1):last_bracket_index])] + list[(last_bracket_index+1):]
					return brackets_problems_to_be_solved(list)
			else:
				return list
		if brackets[0] not in list_tokens:
			return eval_without_brackets(list_tokens)
		else:
			tokens_without_brackets = brackets_problems_to_be_solved(list_tokens)
			print(tokens_without_brackets)
			return eval_without_brackets(tokens_without_brackets)
		
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		pass

	def get_history(self):
		return self.A.list_()
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		pass