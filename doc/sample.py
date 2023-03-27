#lib, api, pn

import os
import re
import json

moddic = json.load(open( '/home/xxm/Desktop/apifuzz/doc/modules.json','r'))

# for mod in moddic:
# 	for api in moddic[mod]:
# 		print(mod,api,moddic[mod][api]["pn"])





testDir = '/home/xxm/Desktop/apifuzz/Python-3.9.2/Lib/test'
 
for root,dirs,files in os.walk(testDir):
	for file in files:
		if file.endswith(".py") and file.startswith("test_"):
			f = open(root+"/"+file,'r').read()
			ast.parse(f)