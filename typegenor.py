import random
import sys
import string
import secrets


class genParam():
	"""docstring for genParameter"""
	# def __init__(self, arg):
	# 	self.arg = arg
	
	def gen_None(self):
		return None

	def gen_NotImplemented(self):
		return NotImplemented

	def gen_Ellipsis(self):
		return Ellipsis

	def gen_Number(self):
		# number = None
		rand = random.choice(["Integral","float","complex"])
		if rand == "Integral":
			number = self.gen_integral()
		if rand == "float":
			number = self.gen_float()
		if rand == "complex":
			number = self.gen_complex()
		return number
	
	def _gen_baseelement(self):
		rand = random.choice(["None","NotImplemented","Ellipsis","Number","Byte","String","class","class instance","IO","internal"])
		# print(rand)
		if rand == "None":
			element = self.gen_None()
		if rand == "NotImplemented":
			element = self.gen_NotImplemented()
		if rand == "Ellipsis":
			element = self.gen_Ellipsis()
		if rand == "Number":
			element = self.gen_Number()
		if rand == "Byte":
			element = self.gen_byte()
		if rand == "String":
			element = self.gen_string()
		if rand == "class":
			element = self.gen_class()
		if rand == "class instance":
			element = self.gen_classinstance()
		if rand == "IO":
			element = self.gen_IO()
		if rand  == "internal":
			element = self.gen_Internal()

		return element



	def gen_Sequences(self):
		# seq = None
		rand = random.choice(["mutable_seq","immutable_seq"])
		if rand == "mutable_seq":
			seq = self.gen_mutable_seq()
		if rand == "immutable_seq":
			seq = self.gen_immutable_seq()
		# seq =  self.gen_string()
		return seq




	def gen_Set(self):
		rand = random.choice(["set","frozenset"])
		if rand == "set":
			mset = self.gen_set()
		if rand == "frozenset":
			mset = self.gen_frozenset()
		return mset

	def gen_Mappings(self):
		mapping = self.gen_dict()
		return mapping


	def gen_Class(self):
		clas = self.gen_class()
		return clas

	def gen_ClassInstance(self):
		classins = self.gen_classinstance()
		return classins

	def gen_IO(self):
		io = self.gen_IO_object()
		return io

	def gen_Internal(self):
		rand = random.choice(["code_object","frame_object","traceback_object","slice_object"])
		if rand == "code_object":
			internal = self.gen_code_object()
		if rand == "frame_object":
			internal = self.gen_frame_object()
		if rand == "traceback_object":
			internal = self.gen_traceback_object()
		if rand == "slice_object":
			internal = self.gen_slice_object()
		return internal


	def gen_integral(self):
		rand = random.choice(["int","bool"])
		if rand == "int":
			integral = self.gen_int()
		if rand == "bool":
			integral = self.gen_bool()				
		return integral

	def gen_mutable_seq(self):
		rand = random.choice(["list","bytearray"])		
		if rand =="list":
			mut_seq = self.gen_list()
		if rand == "bytearray":
			mut_seq = self.gen_bytearray()
		return mut_seq



	def gen_immutable_seq(self):
		rand = random.choice(["string","tuple","byte"])		
		if rand =="string":
			immut_seq = self.gen_string()
		if rand =="tuple":
			immut_seq = self.gen_tuple()
		if rand =="byte":
			immut_seq = self.gen_byte()
		return immut_seq



	def gen_int(self):	
		rint = random.getrandbits(1)
		return rint



	def gen_bool(self):
		boolvalue = random.choice([True,False])
		return boolvalue


	def gen_float(self):
		rfloat = random.uniform(0.0,10.0)
		return rfloat


	def gen_complex(self):
		creal = random.choice(["int","float"])
		cimg  = random.choice(["int","float"])
		if creal == "int":
			real = random.randint(0,10)
		if creal == "float":
			real = random.uniform(0.0,10.0)
		if cimg == "int":
			img = random.randint(1,10)
		if cimg == "float":
			img = random.uniform(1,10.0)
		compx = complex(real,img)
		return compx




	def gen_string(self):
		alphabet = string.printable
		chs = random.choices(['str','path'],weights = [3,1], k = 1)
		if chs[0] == "path":
			gstr = '/'.join(secrets.choice(alphabet) for i in range(random.randint(0,10)))
		else:
			gstr = ''.join(secrets.choice(alphabet) for i in range(random.randint(0,10)))
		return gstr

	def gen_tuple(self):
		rand = random.randint(0,1)
		if rand == 0:
			tup = ()
		if rand == 1:
			tup = (self._gen_baseelement())
		return tup
	
	def gen_byte(self):
		byte = random.randbytes(random.randint(0,10))
		return byte

	def gen_list(self):
		lst = []
		rand = random.randint(0,1)
		for i in range(0,rand):
			lst.append(self._gen_baseelement())
		return lst
	
	def gen_bytearray(self):
		bytearr = bytearray(random.randint(0,10))
		return bytearr


	def gen_set(self):
		st = set()
		rand = random.randint(0,1)
		for i in range(0,rand):
			ele = self._gen_baseelement()
			if ele.__hash__:
				st.add(ele)
		return st

	def gen_frozenset(self):
		fset = frozenset()
		return fset




	def gen_dict(self):
		dic = {}
		rand = random.randint(0,1)
		for i in range(0,rand):
			dic["a"] = self._gen_baseelement()
		return dic

	# def gen_userdefinedfunctions(self):
	# 	pass

	# def gen_instancemethods(self):
	# 	pass
	
	# def gen_generatorfunc(self):
	# 	pass

	# def gen_coroutine_func(self):
	# 	pass

	# def gen_asyncgeneratorfunc(self):
	# 	pass

	# def gen_builtinfunc(self):
	# 	pass
	
	# def gen_builtin_method(self):
	# 	pass

	def gen_class(self):
		class tclass:
			att = None
		return tclass
	
	def gen_classinstance(self):
		tclass = self.gen_class()
		instance = tclass()
		return instance

	def gen_code_object(self):
# 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames'
		code_object = (lambda: 0).__code__
		return code_object

	def gen_frame_object(self):
		frame = sys._getframe()
		# frame.f_back
		return frame

	def gen_traceback_object(self):
		try: 
			raise NameError
		except:
			traceback_object = sys.exc_info()[2]
			return traceback_object
	
	def gen_slice_object(self):
		slice_object = slice(1, 10, None)
		return slice_object


	def gen_IO_object(self):
		# file_object = open('file.txt' , 'rb')
		file_object = sys.stdin
		return file_object


# gp = genParam()
# a = gp.gen_classinstance()
# print(isinstance(a,type))
# print("None:", gp.gen_None())
# print("NotImplemented:", gp.gen_NotImplemented())
# print("Ellipsis:", gp.gen_Ellipsis())
# print("decinteger:", gp.gen_decinteger())
# print("bininteger:", gp.gen_bininteger())
# print("octinteger:", gp.gen_octinteger())
# print("hexinteger:", gp.gen_hexinteger())
# print("bool:", gp.gen_bool())
# print("pointfloat:", gp.gen_pointfloat())
# print("exponentfloat:", gp.gen_exponentfloat())
# print("floatnumberImageJ:", gp.gen_floatnumberImageJ())
# print("floatnumberImagej:", gp.gen_floatnumberImagej())
# print("digitpartImageJ:", gp.gen_digitpartImageJ())
# print("digitpartImagej:", gp.gen_digitpartImagej())
# print("string:", gp.gen_string())
# print("tuple:", gp.gen_tuple())
# print("byte:", gp.gen_byte())
# print("list:", gp.gen_list())
# print("bytearray:", gp.gen_bytearray())
# print("set:", gp.gen_set())
# print("frozenset:", gp.gen_frozenset())
# print("dict:", gp.gen_dict())
# # print("userdefinedfunctions:", gp.gen_userdefinedfunctions())
# # print("instancemethods:", gp.gen_instancemethods())
# # print("generatorfunc:", gp.gen_generatorfunc())
# # print("coroutine_func:", gp.gen_coroutine_func())
# # print("asyncgeneratorfunc:", gp.gen_asyncgeneratorfunc())
# # print("builtinfunc:", gp.gen_builtinfunc())
# # print("builtin_method:", gp.gen_builtin_method())
# a = gp.gen_class()
# del a.att
# a.att = 2

# print("class:", a.__dict__)
# print("classinstance:", gp.gen_classinstance())
# print("code_object:", gp.gen_code_object())
# print("frame_object:", gp.gen_frame_object())
# print("traceback_object:", gp.gen_traceback_object())
# print("slice_object:", gp.gen_slice_object())
# print("static_method_object:", gp.gen_static_method_object())
# print("IO_object:", gp.gen_IO_object())




# i ^ (1 << random.randint(0, 32))


# class A:
#     def __init__(self):
#             self.field = 1
# a.__dict__
# {'field': 1}
# for field in a.__dict__:
#     setattr(a, field, random.randint(1, 3))




# tgdic = {1:"None",2:"NotImplemented"}











