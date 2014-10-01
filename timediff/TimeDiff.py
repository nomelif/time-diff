import time
import datetime
import sys
import platform
import locale
import os
import re
import StringIO

class TimeDiff:
	"""

Class containing all methods related to parsing logs. The program itself is run from _../bin/time-diff_.

	"""

# Empty __init__-method

	def __init__(self):
		""" Empty _\_\_init\_\__ function """
		pass

# Returns help to be showed with -h or --help argument

	def get_help_text(self):
		"""
Returns help text, used when calling _time-diff -h_ or _time-diff --help_.

		""" 
		return """Use by piping file (or greped lines) to program.

ARGUMENTS (All are mandatory)


-h,  --help           : Show this help
-f=, --format=        : Set datetime format options, defaults to "%b %d %H:%M:%S"
-F=, --format-preset= : Set datetime formatting preset, defaults to none accepted values are:

	* custom1 : "%Y%m%d_%H%M%S"

-l=, --locale=        : Sets locale to be used with parsing month and weekday names, defaults to American English (en_US on unix, en-US on Windows).
-r                    : Removes zero-padding from lines, eg. 002 becomes 2.
-p                    : Cancels adding zero-padding, eg. without -p 2 would become 02"""

	def respond_to_wrong_parameters(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Tells user that he / she enttered parameters, that werent understood, doesn't affect parsing of logs.

		"""
		for arg in args[1:]:
		 	is_known = False
		 	for known_arg in ["-p", "-r" "-f", "-h", "--help", "--format", "-F", "--format-preset", "-l", "--locale"]:
		 		try:
					if arg.split("=")[0] == known_arg:
		 				is_known = True
		 		except:
		 			pass
		 	if not is_known:
		 		if debug:
		 			return "Argument {0} not understood, only -p, -r, -h, --help, -l, --locale, -f, --format, -F and --format-preset are known, ignoring argument.".format(arg)
		 		else:
		 			print("Argument {0} not understood, only -p, -r, -h, --help, -l, --locale, -f, --format, -F and --format-preset are known, ignoring argument.".format(arg))

	def display_help(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Displays help from _self.get_help_text()_.

		"""
		if self.is_help_needed(args, os_name, debug):
			if debug:
				return self.get_help_text()
			else:
				print(self.get_help_text())
				return True
		return False
	def is_help_needed(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Returns True if _../bin/time-diff_ was called with argument _-h_ or _--help_.

		"""
		for arg in args:
			if arg == "-h" or arg == "--help":
					return True
		return False

	def set_locale_settings(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Sets locale if such is given through _-l_ or _--locale_ for formatting logs containing names of months and weekdays. Default is American English, if it isn't installed this falls back to the systems current locale.

		"""
		locale_error = False
		eng_locale = "en_US"
		if os_name == "Windows":
			eng_locale = "en-US"
		try:
			locale.setlocale(locale.LC_ALL, eng_locale)
		except:
			locale_error = True
		for arg in args[1:]:
			if "-l=" in arg or "-locale=" in arg:
				try:
					locale.setlocale(locale.LC_ALL, arg.split("=")[1])
				except:
					print("Unknown locale or locale not installed, setting locale to {0}".format(eng_locale))
			elif locale_error:
				if debug:
					raise LocaleError("")
				else:
					print("Can't set locale to {0}, is it installed correctly?".format(eng_locale))

	def get_formatting_string(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Returns string to use for formatting log input. If a preset is correctly specified using _-F_ or _--format-preset_, the corresponding formatting string is returned. If no preset is given and a string is correctly specified using _-f_ or _--format_, it is returned. If a preset is specified, but it doesn't exist and no correct explicit formatting string is given with _-f_ or _--format_, this returns "%b %d %H:%M:%S". If no correct preset is specified, but a correct explicit formatting is, this returns the later. If no correct formatting of any sort is specified, returns "%b %d %H:%M:%S".

		"""
		for arg in args[1:]:
			if "--format=" in arg:
				try:
					return arg.split("--format=")[1]
				except:
					print("Formatting error for datetime format, ignoring")
					return "%b %d %H:%M:%S"
			elif "-f=" in arg:
				try:
					return arg.split("-f=")[1]
				except:
					print("Formatting error for datetime format, ignoring")
					return "%b %d %H:%M:%S"
			elif "--format-preset=" in arg:
				try:
					if arg.split("--format-preset=")[1] == "custom1":
						return "%Y%m%d_%H%M%S"
					else:
						print("No such formatting prefix exists, ignoring")
						return "%b %d %H:%M:%S"
				except:
					print("Formatting error for datetime format prefix, ignoring")
					return "%b %d %H:%M:%S"
			elif "-F=" in arg:
				try:
					if arg.split("-F=")[1] == "custom1":
						return "%Y%m%d_%H%M%S"
					else:
						print("No such formatting prefix exists, ignoring")
						return "%b %d %H:%M:%S"
				except:
					print("Formatting error for datetime format prefix, ignoring")
					return "%b %d %H:%M:%S"
		return "%b %d %H:%M:%S"

	def check_add_zero_pads(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Returns, whether to add zero-paddings or not. If one of the args give is _-p_, returns False, else returns True.

		"""
		for arg in args:
			if arg == "-p":
				return False
		return True

	def check_remove_zero_pads(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Returns, whether to remove zero-paddings or not. If one of the args given is _-r_, returns True, else returns False.

		"""
		for arg in args:
			if arg == "-r":
				return True
		return False

	def remove_zero_pads(self, line):
		"""

Removes zero-paddings from input string. Eg. if input is "Tue Oct 03", the function returns "Tue Oct 3".

		"""
		p = re.compile("([^0-9]0+[1-9][0-9]*|[^0-9]0{2,}[^0-9])")
		matches = p.findall(" "+line+" ")
		for match in matches:
			match = match.strip(" /b")
			i = 0
			while match[i] == "0" and i < len(match)-1:
				i=i+1
			line = line.replace(match, match[i:])
		return line

	def set_formatting(self, args=sys.argv, os_name=platform.system(), debug=False):
		"""

Calls _self.display_help()_, _self.set_locale_settings()_ and _self.get_formatting_string()_, returns output from _self.get_formatting_string()_.

		"""
		self.respond_to_wrong_parameters(args, os_name, debug)
		self.display_help(args, os_name, debug)
		self.set_locale_settings(args, os_name, debug)
		return self.get_formatting_string(args, os_name, debug)
	
	def check_first_line_matches(self, formatting_string, input_data):
		"""

Checks, whether the formatting string matches first line of data. If so, returns True, else returns False.

		"""
		first_time = ""
		try:
			try:
				first_time = time.strptime(" ".join(input_data[0].strip("\n").split(" ")[:3]), formatting_string) # Time of first message as time.struct_time
				return True
			except ValueError, v:
			    if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
			        first_time = input_data[0].split(v.args[0][26:])[0]
			        first_time = time.strptime(first_time, formatting_string)
			    else:
					raise v
		except ValueError:
					print("Formatting string {0} does not match line {1}\n".format(formatting_string, input_data[0]))
					return False

	def cache_input(self, input_data=sys.stdin, args=sys.argv, debug=False):
		"""

Caches given logs into a list, returns the list where the log is cached. Every item in the list is a line from the logs.

		"""
		if self.is_help_needed() and (not sys.stdin.isatty()) or debug:
			log_input = [] # Cache input into list
			if debug and not isinstance(input_data, list):
				log_input = input_data.getvalue().split("\n")
			else:
				for line in input_data:
					log_input.append(line)
			return log_input
		elif (not sys.stdin.isatty()) or debug:
			log_input = [] # Cache input into list
			for line in input_data:
				log_input.append(line)
			return log_input
		return []

	def parse_log(self, log_input, time_format="%b %d %H:%M:%S", out=sys.stdout, zero_pads_add=None, zero_pads_remove=None):
		"""

Parses log files using _self.parse_line()_, formats result using _self.format_line()_

		"""
		if(len(log_input) > 0):
			try:
				try:
					self.first_time = time.strptime(" ".join(log_input[0].strip("\n").split(" ")[:3]), time_format) # Time of first message as time.struct_time
				except ValueError, v:
				    if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
				        self.first_time = log_input[0].split(v.args[0][26:])[0]
				        self.first_time = time.strptime(self.first_time, time_format)
				    else:
						raise v
			except ValueError:
				out.write("Formatting string {0} does not match line {1}\n".format(time_format, log_input[0]))
			else:
				out.write("0:00:00 : {0}\n".format(log_input[0]))
				self.previous_time = self.first_time
				for line in log_input[1:]: # Iterate over list
					new_line = self.parse_line(line, time_format, zero_pads_add, zero_pads_remove)
					if new_line == None:
						out.write("Formatting string {0} does not match line {1}\n".format(time_format, log_input[0]))
					else:
						out.write(self.format_line(new_line))
		elif self.is_help_needed():
			out.write("No input specified, see --help or -h for intructions\n")

	def format_line(self, args):
		"""

Expects a tuple of three elemts containing the time from the first line in the log, the time from the previous line in the log and the contents of the current line, formats it to match: [time from first line] [time from previous line] : [contents of the line].

		"""
		return("{0} {1} : {2}\n".format(args[0], args[1], args[2]))

	def parse_line(self, line, time_format, zero_pads_add=None, zero_pads_remove=None):
		"""

Parses a single line from a log, returns the tuple (difference_in_time_from_first, difference_in_time_from_previous, line's_contents)

		"""
		orig_line = line
		if zero_pads_add == None:
			zero_pads_add = self.check_add_zero_pads()
		if zero_pads_remove == None:
			zero_pads_add = self.check_remove_zero_pads()
		if  zero_pads_add and not zero_pads_remove:
			line = line.zfill(2)
		elif not zero_pads_add and zero_pads_remove:
			line = self.remove_zero_pads(line)
		try:
			msg_time = time.strptime(line, time_format) # Time of first message as time.struct_time
		except ValueError, v:
			msg_time = line.split(v.args[0][26:])[0]
			msg_time = time.strptime(msg_time, time_format)
			time_diff_from_begin = time.mktime(msg_time) - time.mktime(self.first_time)
			time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
			self.previous_time = msg_time
			return (str(datetime.timedelta(seconds=time_diff_from_begin)), str(datetime.timedelta(seconds=time_diff_from_previous)), line.strip("\n"))
		else:
			time_diff_from_begin = time.mktime(msg_time) - time.mktime(self.first_time)
			time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
			self.previous_time = msg_time
			return (str(datetime.timedelta(seconds=time_diff_from_begin)), str(datetime.timedelta(seconds=time_diff_from_previous)), line.strip("\n"))