import select
import sys
import locale


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
		params_dict = {"-v":False, "-h":False, "-f":None, "-F":None, "-p":False, "-l":None, "-r":None}
		for key in params_dict.keys():
			if self.match_arg(args, key):
				key_val = True
				if not key in ("-v", "-h", "-p"):
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

Takes the input stream, reads it and returns an array with the stream read into it, every line of the stream becomes one entry of the array. Stream can be for example a file, _sys.stdin_ or a _StringIO_ object.

		"""
		arr = []
		for line in logs_stream:
			arr.append(line.strip("\n"))
		return arr

	def parse_args_dict(self, args, debug=False):
		"""

Returns correct values for various settings used by both _/bin/time-diff_ and _/bin/time-diff-plot_. Also sets locale.

		"""
		out = {"err code":0, "err msg":"", "format":"%Y%m%d_%H%M%S", "proceed to parse":False}
		if select.select([sys.stdin,],[],[],0.0)[0] or debug:
			if args["-F"] != None or args["-f"] != None:
				if args["-F"] != None and args["-f"] != None:
					out["format"] = args["-f"]
				elif args["-F"] != None:
					if args["-F"] == "custom1":
						out["format"] = "%b %d %H:%M:%S"
				else:
					out["format"] = args["-f"]
			eng_locale = "en_US"
			if args["-l"]  != None:
				try:
					locale.setlocale(locale.LC_ALL, args["l"])
				except:
					out["err code"] = 22
					if args["-v"]:
						out["err msg"] = out["err msg"]+"Unknown locale or locale not installed, setting locale to {0}\n".format(eng_locale)
			else:
				try:
					locale.setlocale(locale.LC_ALL, eng_locale)
				except:
					out["err code"] = 22
					if args["-v"]:
						out["err msg"] = out["err msg"]+"Locale en_US not installed, setting locale to system default.\n"
					locale.setlocale(locale.LC_ALL, "")
			out["proceed to parse"] = True
		else:
		    if args["-h"]:
		    	print(help)
		    else:
		    	out["err code"] = 1
		    	out["err msg"] = "No input specified\n"
		return out