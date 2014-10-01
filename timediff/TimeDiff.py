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

Class containing all methods related to parsing logs

	"""

# Empty __init__-method

	def __init__(self):
		pass

# Returns help to be showed with -h or --help argument

	def get_help_text(self):
		return """Use by piping file (or greped lines) to program.

ARGUMENTS (All are mandatory)


-h,  --help           : Show this help
-f=, --format=        : Set datetime format options, defaults to "%b %d %H:%M:%S"
-F=, --format-preset= : Set datetime formatting preset, defaults to none accepted values are:

	* custom1 : "%Y%m%d_%H%M%S"

-l=, --locale=        : Sets locale to be used with parsing month and weekday names, defaults to American English (en_US on unix, en-US on Windows).
-r                    : Removes zero-padding from lines, eg. 002 becomes 2.
-p                    : Cancels adding zero-padding, eg. without -p 2 would become 02"""

# Looks for not understood parameters and outputs error messages if such are found

	def respond_to_wrong_parameters(self, args=sys.argv, os_name=platform.system(), debug=False):
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



# Displays help if the user asked for it

	def display_help(self, args=sys.argv, os_name=platform.system(), debug=False):
		if self.is_help_needed(args, os_name, debug):
			if debug:
				return self.get_help_text()
			else:
				print(self.get_help_text())
				return True
		return False
	def is_help_needed(self, args=sys.argv, os_name=platform.system(), debug=False):
		for arg in args:
			if arg == "-h" or arg == "--help":
					return True
		return False

# Sets locale for formatting logs containing names of months and weekdays

	def set_locale_settings(self, args=sys.argv, os_name=platform.system(), debug=False):
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

# Returns string to use for formatting log input

	def get_formatting_string(self, args=sys.argv, os_name=platform.system(), debug=False):
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

# Returns, whether to add zero-paddings or not

	def check_add_zero_pads(self, args=sys.argv, os_name=platform.system(), debug=False):
		for arg in args:
			if arg == "-p":
				return False
		return True

# Returns, whether to remove zero-paddings or not

	def check_remove_zero_pads(self, args=sys.argv, os_name=platform.system(), debug=False):
		for arg in args:
			if arg == "-r":
				return True
		return False

# Removes zero-paddings

	def remove_zero_pads(self, line):
		p = re.compile("([^0-9]0+[1-9][0-9]*|[^0-9]0{2,}[^0-9])")
		matches = p.findall(" "+line+" ")
		for match in matches:
			match = match.strip(" /b")
			i = 0
			while match[i] == "0" and i < len(match)-1:
				i=i+1
			line = line.replace(match, match[i:])
		return line

# Calls set_locale_settings and get_formatting_string, returns output from get_formatting_string

	def set_formatting(self, args=sys.argv, os_name=platform.system(), debug=False):
		self.respond_to_wrong_parameters(args, os_name, debug)
		self.display_help(args, os_name, debug)
		self.set_locale_settings(args, os_name, debug)
		return self.get_formatting_string(args, os_name, debug)
	
# Checks, whether the formatting string matches first line of data

	def check_first_line_matches(self, formatting_string, input_data):
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

# Caches given logs into a list, returns the list

	def cache_input(self, input_data=sys.stdin, args=sys.argv, debug=False):
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

	def parse_log(self, log_input, time_format="%b %d %H:%M:%S", out=sys.stdout):
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
				self.previous_time = self.first_time
				for line in log_input[1:]: # Iterate over list
					new_line = self.parse_line(line, time_format)
					if new_line == None:
						out.write("Formatting string {0} does not match line {1}\n".format(time_format, log_input[0]))
					else:
						out.write(new_line)
		elif not "-h" in sys.argv[-1]:
			out.write("No input specified, see --help or -h for intructions\n")

	def parse_line(self, line, time_format):
		orig_line = line
		if self.check_add_zero_pads() and not self.check_remove_zero_pads():
			line = line.zfill(2)
		elif not self.check_add_zero_pads() and self.check_remove_zero_pads():
			line = self.remove_zero_pads(line)
		try:
			msg_time = time.strptime(line, time_format) # Time of first message as time.struct_time
		except ValueError, v:
			msg_time = line.split(v.args[0][26:])[0]
			msg_time = time.strptime(msg_time, time_format)
			time_diff_from_begin = time.mktime(msg_time) - time.mktime(self.first_time)
			time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
			self.previous_time = msg_time
			return("{0} {1} : {2}\n".format(str(datetime.timedelta(seconds=time_diff_from_begin)), str(datetime.timedelta(seconds=time_diff_from_previous)), line.strip("\n")))
		else:
			time_diff_from_begin = time.mktime(msg_time) - time.mktime(self.first_time)
			time_diff_from_previous = time.mktime(msg_time) - time.mktime(self.previous_time)
			self.previous_time = msg_time
			return("{0} {1} : {2}\n".format(str(datetime.timedelta(seconds=time_diff_from_begin)), str(datetime.timedelta(seconds=time_diff_from_previous)), line.strip("\n")))