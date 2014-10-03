class CliOutput():
	"""

Class used to format line-tuples given by parser.Parser

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass

	def format_line(self, line_tuple):
		"""

Returns formated string containing data from _Parser.parse_line_.

		"""
		try:
			return "{0} {1} : {2}".format(str(line_tuple[0]), str(line_tuple[1]), str(line_tuple[2]))
		except IndexError:
			pass