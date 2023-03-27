import json
import itertools
import traceback
import os
import typegenor as tg
import inspect
import random
import typegenor
import mutator 
import sys
import timeout



def gparam(kind):
	gp = typegenor.genParam() 
	if kind == "None":
		param = gp.gen_None()
	if kind == "NotImplemented":
		param = gp.gen_NotImplemented()
	if kind == "Ellipsis":
		param = gp.gen_Ellipsis()
	if kind == "Int":
		param = gp.gen_int()
	if kind == "Float":
		param = gp.gen_float()
	if kind == "Bool":
		param = gp.gen_bool()
	if kind == "Complex":
		param = gp.gen_complex()
	if kind == "String":
		param = gp.gen_string()
	if kind == "Byte":
		param = gp.gen_byte()
	if kind == "Byte_Array":
		param = gp.gen_bytearray()

	if kind == "Tuple":
		param = gp.gen_tuple()
	if kind == "List":
		param = gp.gen_list()
	# if kind == "Number":
	# 	param = gp.gen_Number()
	# if kind == "Sequences":
	# 	param = gp.gen_Sequences()

	if kind == "Set":
		param = gp.gen_set()

	if kind == "Frozenset":
		param = gp.gen_frozenset()
	# if kind == "Mappings":
	# 	param = gp.gen_Mappings()
	if kind == "Dict":
		param = gp.gen_dict()

	if kind == "Class":
		param = gp.gen_class()
	if kind == "ClassInstance":
		param = gp.gen_classinstance()
	if kind == "IO":
		param = gp.gen_IO_object()
	if kind == "Code_Object":
		param = gp.gen_code_object()
	if kind == "Frame_Object":
		param = gp.gen_frame_object()
	if kind == "Slice_Object":
		param = gp.slice_object()
	if kind == "Traceback":
		param = gp.gen_traceback_object()



	# if kind == "Internal":
	# 	param = gp.gen_Internal()
	return param



def get_paramlist(n):
	typelist = ["None","NotImplemented","Ellipsis","Int","Float","Complex","Bool","String","Byte","Byte_Array","Tuple","List","Set","Frozeset", "Dict","Class","ClassInstance","IO", "Code_Object","Frame_Object","Slice_Object","Traceback"]
	choicelist = random.choices(typelist,weights = [3,1,1,5,4,1,4,5,2,2,3,4,3,1,3,3,3,3,1,1,1,1], k = n)
	paramlist = []
	for item in choicelist:

		paramlist.append(gparam(item))


	# paramlist = [0]
	return paramlist



def get_api_content(mod,api,n):
	code = "import %s;\n"%mod 
	code =code+ mod+'.'+api+'('
	c = 0
	while c < n-1:
		code = code + "paramlist[%s]"%c + ","	
		c = c + 1	

	code = code +  "paramlist[%s]"%c +")"

	
	return code


def get_mulist(paramlist):
	mt = mutator.mutator()
	mt.mtParam(paramlist)
	# paramlist = get_paramlist(1)
	newlist = paramlist
	return newlist


mod = sys.argv[1]
api = sys.argv[2]
n = int(sys.argv[3])


# paramlist = get_paramlist(n)
# print("seed......",paramlist)
# print(".......mutant",get_mulist(paramlist))




def tt():
	if not os.path.exists("timeout"):
		os.mkdir("timeout")
	if not os.path.exists("timeout/%s"%mod):
		os.mkdir("timeout/%s"%mod)

	if not os.path.exists("timeout/%s/%s"%(mod,api)):
		os.mkdir("timeout/%s/%s"%(mod,api))

	filelist = os.listdir("timeout/%s/%s"%(mod,api)) 
	# print(filelist)

	if filelist:
		mx = int(filelist[0].replace(".py",''))
		for item in filelist:
			if mx < int(item.replace(".py",'')):
				mx = int(item.replace(".py",''))
		number = mx + 1
	else:
		number = 1

	f1 = open("temp.py",'r')
	code = f1.read()
	f1.close()

	f2 = open("timeout/%s/%s/%s.py"%(mod,api,number),'w')
	f2.write(code)
	f2.close()



@timeout.set_timeout(5,tt)
def fuzzapi(mod,api,n):

	if n == 0:
		codeprefix = "import %s;\n"%mod
		code = codeprefix+ mod+'.'+api+'('+')'
		open("./temp.py",'w').write(code)
		try:
			exec(compile(code,'','exec'))
		except:
			traceback.print_exc()
	else:
		
		paramlist = get_paramlist(n)
		code = get_api_content(mod,api,n)
		print(code)
		f = open("./temp.py",'w')
		for item in paramlist:
			f.write(str(item))
			f.write("\n")
		f.write("\n")
		f.write(code)
		f.close()

		try:
			exec(compile(code,'','exec'))
		except:
			traceback.print_exc()
			pass

		
		paramlist = get_mulist(paramlist)
		# print(paramlist)
		code = get_api_content(mod,api,n)
		print(code)
		f = open("./temp.py",'w')
		for item in paramlist:
			f.write(str(item))
			f.write("\n")
		f.write("\n")
		f.write(code)
		f.close()

		try:
			exec(compile(code,'','exec'))
		except:
			traceback.print_exc()
			pass

		# paramlist = get_mulist(paramlist)
		print("____________\n\n\n\n")



fuzzapi(mod,api,n)





