#class&instance
class Student(object):
	def _init_(self, name, score):
		self.name = name
		self.score = score
		self._name = name# private

bart = Student('Bart Simp', 59)
bart.name
bart.score
