import time
import datetime
import sys
import platform
import locale
import os

class TimeDiff:

	def __init__(self):
		pass

	def get_help_text(self):
		return """Use by piping file (or greped lines) to program.

ARGUMENTS (All are mandatory)


-h,  --help           : Show this help
-f=, --format=        : Set datetime format options, defaults to "%b %d %H:%M:%S"
-p=, --format-preset= : Set datetime formatting preset, defaults to none accepted values are:

	* custom1 : "%Y%m%d_%H%M%S"

-l=, --locale=        : Sets locale to be used with parsing month and weekday names, defaults to American English (en_US on unix, en-US on Windows)."""

	def set_formatting(self, args=sys.argv, os_name=platform.system(), debug=False):

		if "-h" in args[-1]:
			if debug:
				return self.get_help_text()
			else:
				print(self.get_help_text())
		locale_error = False
		eng_locale = "en_US"
		if os_name == "Windows":
			eng_locale = "en-US"
		try:
			locale.setlocale(locale.LC_ALL, eng_locale)
		except:
			locale_error = True
		for arg in args[1:]:
			is_known = False
			for known_arg in ["-f", "-h", "--help", "--format", "-p", "--format-preset", "-l", "--locale"]:
				if arg.split("=")[0] == known_arg:
					is_known = True
			if not is_known:
				print("Argument {0} not understood, only -h, --help, -l, --locale, -f, --format, -p and --format-preset are known, ignoring argument.".format(arg))
			else:
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

				try:
					if "--format=" in args[1]:
						try:
							return args[1].split("--format=")[1]
						except:
							print("Formatting error for datetime format, ignoring")
							return "%b %d %H:%M:%S"
					elif "-f=" in args[1]:
						try:
							return args[1].split("-f=")[1]
						except:
							print("Formatting error for datetime format, ignoring")
							return "%b %d %H:%M:%S"
					elif "--format-preset=" in args[1]:
						try:
							if args[1].split("--format-preset=")[1] == "custom1":
								return "%Y%m%d_%H%M%S"
							else:
								print("No such formatting prefix exists, ignoring")
								return "%b %d %H:%M:%S"
						except:
							print("Formatting error for datetime format prefix, ignoring")
							return "%b %d %H:%M:%S"
					elif "-p=" in args[1]:
						try:
							if args[1].split("-p=")[1] == "custom1":
								return "%Y%m%d_%H%M%S"
							else:
								print("No such formatting prefix exists, ignoring")
								return "%b %d %H:%M:%S"
						except:
							print("Formatting error for datetime format prefix, ignoring")
							return "%b %d %H:%M:%S"
					else:
						return "%b %d %H:%M:%S"
				except IndexError:
					return "%b %d %H:%M:%S"
		return "%b %d %H:%M:%S"

	def cache_input(self, input_data=sys.stdin, args=sys.argv, debug=False):
		#print(sys.stdin.isatty())
		if len(args) > 1:
			if not "-h" in args[1] and (not sys.stdin.isatty()) or debug:
				log_input = [] # Cache input into list
				if debug:
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
		else:
			return []

	def parse_log(self, log_input, time_format="%b %d %H:%M:%S", out=sys.stdout):
		if(len(log_input) > 0):
			try:
				try:
					first_time = time.strptime(" ".join(log_input[0].strip("\n").split(" ")[:3]), time_format) # Time of first message as time.struct_time
				except ValueError, v:
				    if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
				        first_time = log_input[0].split(v.args[0][26:])[0]
				        first_time = time.strptime(first_time, time_format)
				    else:
						raise v
			except ValueError:
						out.write("Formatting string {0} does not match line {1}\n".format(time_format, log_input[0]))
			else:
				previous_time = first_time
				try:
					for line in log_input[1:]: # Iterate over list
						try:
							try:
								msg_time = time.strptime(" ".join(line.strip("\n").split(" ")[:3]), time_format) # Time of first message as time.struct_time
							except ValueError, v:
							    if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
							        msg_time = line.split(v.args[0][26:])[0]
							        msg_time = time.strptime(msg_time, time_format)
							    else:
									raise v
						except ValueError:
							out.write("Formatting string {0} does not match line {1}\n".format(time_format, line))
						else:
							time_diff_from_begin = time.mktime(msg_time) - time.mktime(first_time)
							time_diff_from_previous = time.mktime(msg_time) - time.mktime(previous_time)
							out.write("{0} {1} : {2}\n".format(str(datetime.timedelta(seconds=time_diff_from_begin)), str(datetime.timedelta(seconds=time_diff_from_previous)), line.strip("\n")))
							previous_time = msg_time
				except ValueError:
					out.write("Formatting string {0} does not match line {1}\n".format(time_format, log_input[0]))
		elif not "-h" in sys.argv[-1]:
			out.write("No input specified, see --help or -h for intructions\n")