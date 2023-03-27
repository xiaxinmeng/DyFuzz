import random
import typegenor

gp = typegenor.genParam()

class mutator():
	def mtParam(self,paramlist):
		i = 0 
		while i < len(paramlist):
			if isinstance(paramlist[i], int):
				paramlist[i] = self.mt_int(paramlist[i])

			if isinstance(paramlist[i], bool):
				paramlist[i] = self.mt_bool(paramlist[i])

			if isinstance(paramlist[i], float):
				paramlist[i] = self.mt_float(paramlist[i])

			if isinstance(paramlist[i], complex):
				paramlist[i] = self.mt_complex(paramlist[i])

			if isinstance(paramlist[i], str):
				paramlist[i] = self.mt_str(paramlist[i])


			# if isinstance(paramlist[i],tuple):
			# 	paramlist[i] = self.mt_tuple(paramlist[i])


			if isinstance(paramlist[i], bytes):
				paramlist[i] = self.mt_bytes(paramlist[i])


			if isinstance(paramlist[i], list):
				paramlist[i] = self.mt_list(paramlist[i])


			if isinstance(paramlist[i], bytearray):
				paramlist[i] = self.mt_bytearray(paramlist[i])

			if isinstance(paramlist[i], set):
				paramlist[i] = self.mt_set(paramlist[i])


			if isinstance(paramlist[i], dict):
				paramlist[i] = self.mt_dict(paramlist[i])


			if isinstance(paramlist[i],gp.gen_Class() ):
				paramlist[i] = self.mt_class(paramlist[i])

			if type(paramlist[i]) == type(gp.gen_IO_object() ):
				paramlist[i] = self.mt_io(paramlist[i])


			if not isinstance(paramlist[i], type):
				paramlist[i] = self.mt_classinstance(paramlist[i])






			# if isinstance(paramlist[i],gp.gen_frame_object() ):
			# 	paramlist[i] = self.mt_frame_object(paramlist[i])	

			# if isinstance(paramlist[i],gp.gen_traceback_object() ):
			# 	paramlist[i] = self.mt_traceback_object(paramlist[i])	

			# if isinstance(paramlist[i], gp.gen_slice_object()):
			# 	paramlist[i] = self.mt_slice_object(paramlist[i])


			i = i + 1
		return paramlist

	def mt_int(self, init_value):
		mtvalue = init_value ^ (1 << random.randint(0, 32))
		return mtvalue
	
	def mt_bool(self, init_value):
		mtvalue = random.choice([True,False])
		return mtvalue		

	def mt_float(self, init_value):
		value = self.mt_int(int(init_value))
		rand = random.randint(1,20)
		mtvalue = float(value/rand)
		return mtvalue	

	def mt_complex(self, init_value):
		real = self.mt_float(init_value.real)
		image = self.mt_float(init_value.imag)
		mtvalue = complex(real,image)
		return mtvalue	

	def mt_str(self, init_value):
		mtvalue = init_value*random.randint(1,3)*1024*random.randint(1,1024)
		return mtvalue	

	def mt_tuple(self, init_value):
		mtvalue = init_value
		return mtvalue	

	def mt_bytes(self, init_value):
		mtvalue =  init_value*random.randint(1,3)*1024*random.randint(1,1024)
		return mtvalue	

	def mt_list(self, init_value):
		# print(init_value)
		mtvalue = init_value*10**(random.randint(1,8))
		return mtvalue	

	def mt_bytearray(self, init_value):
		mtvalue = init_value*10**(random.randint(1,8))
		return mtvalue	

	def mt_set(self, init_value):
		mrand  = random.randint(1,100)
		for i in range(0, mrand):
			randelem = gp._gen_baseelement()
			# print(randelem)
			if randelem.__hash__:
				init_value.add(randelem)
		mtvalue = init_value
		return mtvalue	


	def mt_dict(self, init_value):
		mrand  = random.randint(1,100)
		for i in range(0, mrand):
			randkey = gp._gen_baseelement()
			if not randkey.__hash__:
				randkey = "hash"
			randvalue = gp._gen_baseelement()
			init_value[randkey] = randvalue
		mtvalue = init_value
		return mtvalue	


	def mt_class(self, init_value):
		randop = random.choice(["addition","modification","deletion"])
		if randop == "addition":
			addran = random.randint(1,10)
			for i in range(0,addran):
				setattr(init_value,gp.gen_string(),_gen_baseelement())

		if randop == "modification":
			for item in init_value.__dict__:
				if not item.startswith("__"):
					newattr = gp._gen_baseelement()

					if not isinstance(newattr,gp.gen_Class()) and isinstance(newattr, type):
						newattr = self.mtParam([newattr])[0]

					setattr(init_value,item, newattr)
		if randop == "deletion":
			dellist = []
			for item in init_value.__dict__:
				if not item.startswith("__"):
					dellist.append(item) 
			randdel =  random.randint(0,len(dellist))
			for i in range(0,randdel):
				delelem = random.choice(dellist)
				dellist.remove(delelem)
				delattr(init_value,delelem)



		mtvalue = init_value
		return mtvalue	


	def mt_classinstance(self, init_value):
		mtvalue = init_value
		return mtvalue	

	def mt_io(self, init_value):
		randmode = random.choice(['t','x','b','+','U','r','rb','r+','rb+','w','wb','w+','wb+','a','ab','a+','ab+'])
		# print(randmode)
		init_value.mode = randmode
		mtvalue = init_value
		return mtvalue	


	# def mt_code_object(self, init_value):
	# 	mtvalue = init_value
	# 	return mtvalue	

	# def mt_frame_object(self, init_value):
	# 	mtvalue = init_value
	# 	return mtvalue	

	# def mt_traceback_object(self, init_value):
	# 	mtvalue = init_value
	# 	return mtvalue	

	# def mt_slice_object(self, init_value):
	# 	mtvalue = init_value
	# 	return mtvalue	


















