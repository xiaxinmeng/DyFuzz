import os 
import inspect
import traceback
import re
import json
import sys

log_print = open('/home/xxm/Desktop/apifuzz/doc/log.txt' , 'w')
sys.stdout = log_print
sys.stderr = log_print

# def getAPINameFromDoc(docdir = '/home/xxm/Desktop/apifuzz/doc/library' ):

# 	doclist = []
# 	for root,dirs,files in os.walk(docdir):
# 		for file in files:
# 			doc = file.replace(".rst","")
# 			try:
# 				mstr = "import %s;"%doc
# 				exec(compile(mstr,'','exec'))
# 				doclist.append(doc)
# 			except:
# 				pass

# 	return sorted(doclist)


# doclist = getAPINameFromDoc()
# print(doclist)


doclist = ['__future__', '__main__', '_thread', 'abc', 'aifc', 'argparse', 'array', 'ast',
'asynchat', 'asyncio', 'asyncore', 'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'binhex', 
'bisect', 'builtins', 'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs',
'codeop', 'collections', 'collections.abc', 'colorsys', 'compileall', 'concurrent', 'concurrent.futures',
'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'curses', 
'curses.ascii', 'curses.panel', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils',
'doctest', 'email', 'email.charset', 'email.contentmanager', 'email.encoders', 'email.errors', 'email.generator',
'email.header', 'email.headerregistry', 'email.iterators', 'email.message', 'email.mime', 'email.parser', 'email.policy',
'email.utils', 'ensurepip', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput', 'fnmatch', 'formatter', 'fractions', 
'ftplib', 'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 
'html.entities', 'html.parser', 'http', 'http.client', 'http.cookiejar', 'http.cookies', 'http.server', 'imaplib', 'imghdr', 'imp', 
'importlib', 'importlib.metadata', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword', 'linecache', 'locale', 'logging',
'logging.config', 'logging.handlers', 'lzma', 'mailbox', 'mailcap', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 
'multiprocessing', 'multiprocessing.shared_memory', 'netrc', 'nis', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'os.path',
'ossaudiodev', 'parser', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib', 'posix',
'pprint', 'profile', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'pyexpat', 'queue', 'quopri', 'random', 're', 'readline', 
'reprlib', 'resource', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 
'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3', 'ssl', 'stat', 'statistics', 'string',
'stringprep', 'struct', 'subprocess', 'sunau', 'symbol', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile',
'telnetlib', 'tempfile', 'termios', 'textwrap', 'threading', 'time', 'timeit', 'tkinter', 'tkinter.colorchooser', 
'tkinter.dnd', 'tkinter.font', 'tkinter.messagebox', 'tkinter.scrolledtext', 'tkinter.tix', 'tkinter.ttk', 'token', 'tokenize', 
'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'types', 'typing', 'unicodedata', 'unittest', 'unittest.mock', 'urllib', 
'urllib.error', 'urllib.parse', 'urllib.request', 'urllib.robotparser', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 
'webbrowser', 'wsgiref', 'xdrlib', 'xml', 'xml.dom', 'xml.dom.minidom', 'xml.dom.pulldom', 'xml.sax', 'xml.sax.handler', 'xmlrpc',
'xmlrpc.client', 'xmlrpc.server', 'zipapp', 'zipfile', 'zipimport', 'zlib', 'zoneinfo']

print(len(doclist))

def getAllAPIAttr(doclist):
	allAttrDic ={}
	for lib in doclist:
		try:
			# print(lib)
			exec(compile("import %s;attr = dir(%s)"%(lib,lib),'','exec'))
			allAttrDic[lib]=locals()["attr"]
		except:
			traceback.print_exc()
	return allAttrDic



def getparaFromTraceBack(lib,api):

#0: isleap() takes 1 positional argument but 999 were given
#1: format() takes from 1 to 3 positional arguments but 999 were given

#2: decompressobj() takes at most 2 arguments (999 given)

#3: cmath.asin() takes exactly one argument (999 given)
#4: _contextvars.copy_context() takes no arguments (999 given)

#5: crc32 expected at most 2 arguments, got 999

#6: init_color expected 4 arguments, got 999

#7. _curses.newwin requires 2 to 4 arguments


#8. literal_eval() missing 1 required positional argument: 'node_or_string'
#9. start_new_thread expected at least 2 arguments, got 0


	p = None
	try:
		arg_test = 999	
		l = [None] * arg_test
		exec(compile("import %s; %s.%s(*l)"%(lib,lib,api),'','exec'))
	except TypeError as e:

		message = str(e)
		print(message)
		# print(r"[\w]+\(\) takes ([0-9]{1,3}) positional argument[s]* but " +
				# str(arg_test) + " were given")
		found = re.match(
			r".+ takes ([0-9]{1,3}) positional (argument|arguments).*", message)

		found1 = re.match(
			r".+ takes from ([0-9]{1,3}) to ([0-9]{1,3}) positional (argument|arguments).*", message)


		found2 = re.match(
			r".+ takes at most ([0-9]{1,3}|[\w]+) (argument|arguments) \("+ str(arg_test) + " given\)", message)


		found3 = re.match(
			r".+ takes exactly ([0-9]{1,3}|[\w]+) (argument|arguments) \("+ str(arg_test) + " given\)", message)

		found4 = re.match(
			r".+ takes no arguments \("+ str(arg_test) + " given\)", message)


		found5 = re.match(
			r".+ expected at most ([0-9]{1,3}|[\w]+) (argument|arguments), got "+
				str(arg_test), message)


		found6 = re.match(
			r".+ expected ([0-9]{1,3}) (argument|arguments), got "+
				str(arg_test), message)

		found7 = re.match(
			r".+ requires ([0-9]{1,3}) to ([0-9]{1,3}) arguments", message)

		if found:
			p= (int(found.group(1)),int(found.group(1)))

		elif found1:
			p= (int(found1.group(1)),int(found1.group(2)))

		elif found2:
			p= (0,int(found2.group(1)))

		elif found3:
			if found3.group(1)  == "one":
				p = (1,1)
			else:
				p = (int(found3.group(1)),int(found3.group(1)))

		elif found4:
			p = (0,0)
		elif found5:
			p = (0,int(found5.group(1)))
		elif found6:
			p = (int(found6.group(1)),int(found6.group(1)))
		elif found7:
			p= (int(found7.group(1)),int(found7.group(2)))


	print(p)
	return p


# print(getparaFromTraceBack("tokenize","detect_encoding"))



allAttrDic = getAllAPIAttr(doclist)

# print(len(allAttrDic.keys()))
# print(allAttrDic.keys())

def getAPIInfo(allAttrDic):
	moddic = {}
	for lib in allAttrDic:
		libapidic = {}
		for api in allAttrDic[lib]:
			
			if api.startswith("_") or api.endswith("_"):
				pass
			else:
				try:
					exec(compile("import %s;s_ = %s.%s"%(lib,lib,api),'','exec'))
					s = locals()["s_"]
					# if inspect.ismodule(s):
					# 	counter = counter + 1
					# 	print(s)


					# if inspect.ismethod(s):
					# 	counter = counter + 1
					# 	# print(s)

					# if inspect.isgeneratorfunction(s):
					# 	counter = counter + 1
					# 	# print(s)

					# if inspect.iscoroutinefunction(s):
					# 	counter = counter + 1
						# print(s)

					# if inspect.iscoroutinefunction(s):
					# 	counter = counter + 1
					# 	# print(s)


					# if inspect.isclass(s):
					# 	counter = counter + 1
					# 	setcc.add(s)
					# 	# print(s)

					# if inspect.isfunction(s):
					# 	print(API,ATT)
					# 	print(inspect.getfullargspec(s))
					# 	print(s)

					# 	print(s,p)
					# 	counter =counter + 1

					if inspect.isroutine(s):
						# counter = counter + 1
						print(s,lib,api)
						# setcc.add(s)
						paramNum = getparaFromTraceBack(lib,api)
						print("\n")
						if paramNum:
							apidic = {}
							apidic["pn"]= paramNum
							libapidic[api] = apidic
				except:
					traceback.print_exc()
					print("\n")

		moddic[lib] = libapidic
	return moddic


moddic = getAPIInfo(allAttrDic)



def addapi(moddic, lib , api , pn1,pn2):
	if lib in moddic.keys():
		if api in moddic[lib].keys():
			moddic[lib][api]["pn"] = (pn1,pn2)
		else:
			moddic[lib][api] = {"pn":(pn1,pn2)}
	else:
		moddic[lib] = {api:{"pn":(pn1,pn2)}}
	return moddic


# moddic = addapi(moddic,"zoneinfo","hhhhhhhhh",1,2)

with open('/home/xxm/Desktop/apifuzz/doc/modules.json','w') as f:
	json.dump(moddic, f)