import datetime
class CliOutput():
	"""

Class used to format line-tuples given by parser.Parser

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass

	def format_timedelta(self, timedelta, round_to="s"):
		"""

Takes in a datetime.Timedelta, that gets formatted to a String. Without arguments it returns "[spaces_to_create_consistent_padding][seconds] seconds". If it is given a _round_to_-argument, it returns "[spaces_to_create_consistent_padding][time_floored_in_given_unit] [units name]". Accepted values for time-units to round to are: _s_, _min_, _ms_, _h_ and _d_.

		"""
		if round_to == "s" :
			return " "*(10 - len(str(int(timedelta.total_seconds())))) + str(int(timedelta.total_seconds())) + " s"
		else:
			if round_to == "ms":
				return " "*(10 - len(str(int(timedelta.total_seconds())))) + str(int(timedelta.total_seconds())*1000 + int(timedelta.microseconds/1000.)) + " ms"
			elif round_to == "min":
				return " "*(10 - len(str(int(timedelta.total_seconds()) / 60))) + str(int(timedelta.total_seconds()) / 60) + " min"
			elif round_to == "h":
				return " "*(10 - len(str(int(timedelta.total_seconds()) / 60 / 24))) + str(int(timedelta.total_seconds()) / 60 / 24) + " h"
			elif round_to == "d":
				return " "*(10 - len(str(timedelta.days))) + str(timedelta.days) + " d"

	def format_line(self, line_tuple, round_to="s"):
		"""

Returns formated string containing data from _Parser.parse_line_. Times are formatted using _CliOutput.format_timedelta_. Takes _round_to_-argument, that will be forwarded to _format_timedelta_.

		"""
		try:
			return "{0} {1} : {2}".format(self.format_timedelta(line_tuple[0], round_to), self.format_timedelta(line_tuple[1], round_to), str(line_tuple[2]))
		except:
			pass