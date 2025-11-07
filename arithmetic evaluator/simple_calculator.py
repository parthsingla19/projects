from stack import Stack

class SimpleCalculator:
	def __init__(self):
		self.input_expression = None
		self.A = Stack()
		"""
		Instantiate any data attributes
		"""
		pass

	def evaluate_expression(self, input_expression):
		self.input_expression = input_expression
		k = self.input_expression
		check = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
		s = ""
		a = "+-*/"
		cnt1 = 0
		i = 0
		while(i<len(k)):
			if k[i]!=" " and k[i] not in a:
				j = i
				while(j<len(k) and k[j]!=" " and k[j] not in a):
					j = j + 1
				s = s + k[i:j]
				cnt1 = cnt1 + 1
				i = j -1
			elif k[i]!=" " and k[i] in a:
				cnt1 = cnt1 + 1
				s = s + k[i]
			i = i + 1
		for checker in s:
			if checker not in check:
				self.A.push((input_expression, "Error"))
				return "Error"
		cnt = 0
		for j in s:
			if a.find(j)!=-1:
				cnt = cnt + 1
		if cnt1!=3:
			self.A.push((input_expression, "Error"))
			return "Error"
		else:
			if cnt!=1:
				self.A.push((input_expression, "Error"))
				return "Error"
			else:
				for j in range(len(s)):
					if a.find(s[j])!=-1:
						s1 = s[:j]
						s2 = s[j+1:]
						break
				if len(s1)==0:
					self.A.push((input_expression, "Error"))
					return "Error"
				elif len(s2)==0:
					self.A.push((input_expression, "Error"))
					return "Error"
				else:
					_s1_ = int(s1)
					_s2_ = int(s2)
				if s[j] == "+":
					k1 = float(_s1_ + _s2_)
				elif s[j]=="-":
					k1 = float(_s1_ - _s2_)
				elif s[j]=="*":
					k1 = float(_s1_ * _s2_)
				elif s[j] == "/":
					if _s2_!=0:
						k1 = float(_s1_ / _s2_)
					else: 
						k1 = "Error"
				self.A.push((input_expression, k1))
				return k1
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		pass

	def get_history(self):
		return self.A.list_()
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		pass
a = SimpleCalculator()
print(a.evaluate_expression("x + 5"))