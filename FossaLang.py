class Info:
	varaibles = {}
	functions = {}

class Functions:
	def func(self, funcname, parameters, optional_parameters, description, func):
		'''
		Takes the function's name, number of needed parameters, number of optional parameters, description and the function.
		'''
		print('Received ' + str(func) + '!')
		print('Updating...')
		Info.functions[funcname] = [parameters, optional_parameters, description, func]
		print('Updated ' + funcname + '.')
	def find_func(self, funcname):
		try:
			return Info.functions[funcname]
		except:
			return False
	def find_func(self, funcname):
		try:
			return Info.Functions[funcname]
		except:
			return False
			