import time
import datetime

class LogParser():
	"""

Class used to parse logs.

	"""
	first_time = None
	"""

Time of the first line.

	"""
	previous_time = None
	"""

Time of the previous line.

	"""
	def __init__(self):
		"""

Empty _\_\_init\_\__ -method.

		"""
		pass
		
	def parse_logs(self, log_arr, time_format, zero_pad=True):
		"""

Function that parses a log-array as given by cli_input.CliInput. Returns a list of tuples from _parse_line_.

		"""
		logs = []
		for line in log_arr:
			logs.append(self.parse_line(line, time_format, zero_pad))
		return logs

	def get_diff(self, line, time_format, zero_pad=True):
		"""

Parses a single line from a log-array. Returns the difference in time from the previous line
		"""
		msg_time = None
		msg_time_set = False
		if  zero_pad:
			line = line.zfill(2)
		try:
			try:
				msg_time = time.strptime(line, time_format)
				msg_time_set = True
			except ValueError, v:
				msg_time = line.split(v.args[0][26:])[0]
				msg_time = time.strptime(msg_time, time_format)
				if(msg_time.tm_year == 1900):
					msg_time=time.struct_time((2001, msg_time.tm_mon, msg_time.tm_mday, msg_time.tm_hour, msg_time.tm_min, msg_time.tm_sec, msg_time.tm_wday, msg_time.tm_yday, msg_time.tm_isdst))
				msg_time_set = True
			else:
				if(msg_time.tm_year == 1900):
						msg_time=time.struct_time((2001, msg_time.tm_mon, msg_time.tm_mday, msg_time.tm_hour, msg_time.tm_min, msg_time.tm_sec, msg_time.tm_wday, msg_time.tm_yday, msg_time.tm_isdst))
				msg_time_set = True
			if msg_time_set:
				if self.first_time == None and self.previous_time == None:
					self.first_time = msg_time
					self.previous_time = msg_time
				time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
				self.previous_time = msg_time
				return(time_diff_from_previous)

			else:
				return None
		except ValueError:
			return None

	def parse_line(self, line, time_format, zero_pad=True):
		"""

Parses a single line from a log-array. Returns the tuple [time from first line] [time from last line] : [line's contents]

		"""
		orig_line = line
		msg_time = None
		msg_time_set = False
		if  zero_pad:
			line = line.zfill(2)
		try:
			try:
				msg_time = time.strptime(line, time_format)
				msg_time_set = True
			except ValueError, v:
				msg_time = line.split(v.args[0][26:])[0]
				msg_time = time.strptime(msg_time, time_format)
				if(msg_time.tm_year == 1900):
						msg_time=time.struct_time((2001, msg_time.tm_mon, msg_time.tm_mday, msg_time.tm_hour, msg_time.tm_min, msg_time.tm_sec, msg_time.tm_wday, msg_time.tm_yday, msg_time.tm_isdst))
				msg_time_set = True
			else:
				if(msg_time.tm_year == 1900):
						msg_time=time.struct_time((2001, msg_time.tm_mon, msg_time.tm_mday, msg_time.tm_hour, msg_time.tm_min, msg_time.tm_sec, msg_time.tm_wday, msg_time.tm_yday, msg_time.tm_isdst))
				msg_time_set = True
			if msg_time_set:
				if self.first_time == None and self.previous_time == None:
					self.first_time = msg_time
					self.previous_time = msg_time
				time_diff_from_begin = time.mktime(msg_time) - time.mktime(self.first_time)
				time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
				self.previous_time = msg_time
				return(datetime.timedelta(seconds=time_diff_from_begin), datetime.timedelta(seconds=time_diff_from_previous), orig_line)

			else:
				return None
		except ValueError:
			return None