
class CliInput():
	"""

Class used to parse command-line input.

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass

	def get_params_dict(self, args):
		"""

Returns a dictionary with one key per parameter.

		"""
		params_dict = {"-v":False, "-h":False, "-f":None, "-F":None, "-p":False, "-l":None}
		for key in params_dict.keys():
			if self.match_arg(args, key):
				key_val = True
				if not key in ("-v", "-h", "-p", "-l"):
					try:
						for arg in args:
							if arg[:len(key)] == key:
								key_val = arg.split("=")[1]
					except:
						key_val = None
				params_dict[key] = key_val
		return params_dict

	def match_arg(self, args, arg):
		"""

Returns True, if the argument _arg_ is given in the list of args.

		"""
		for arg_to_test in args:
			if arg_to_test[:len(arg)] == arg:
				return True
		return False

	def get_log_arr(self, logs_stream):
		"""

Takes the input stream, reads it and returns an array with the stream read into it, ery line of the stream becomes one entry of the array. Stream can be for example a file, _sys.stdin_ or a _StringIO_ object.

		"""
		arr = []
		for line in logs_stream:
			arr.append(line.strip("\n"))
		return arr