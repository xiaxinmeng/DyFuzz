import os 
import platform
import signal, functools
import timeout
import json
import time
# print(platform.system())

# mod ="ctypes"
# api = "string_at"
# n=1


# mod = "os"
# api = "abort"
# n=0

# mod = "pdb"
# api = "run"
# n = 1


# mod = "nis"
# api = "maps"
# n = 1


# mod = "nis"
# api = "cat"
# n = 2





# mod = "imp"
# api = "load_dynamic"
# n = 2

# mod ="builtins"
# api = "eval"
# n =1

# mod ="random"
# api = "choice"


totalAPI = 0


def gen_log(mod,api,n,s):
    # print(s)
    if s != 0 and s!=256: 

      if not os.path.exists("error"):
        os.mkdir("error")
      if not os.path.exists("error/%s"%mod):
        os.mkdir("error/%s"%mod)

      if not os.path.exists("error/%s/%s"%(mod,api)):
        os.mkdir("error/%s/%s"%(mod,api))

      filelist = os.listdir("error/%s/%s"%(mod,api)) 
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

      f2 = open("error/%s/%s/%s.py"%(mod,api,number),'w')
      f2.write(code)
      f2.close()

      f3 = open("log.txt",'a')
      f3.write(mod)
      f3.write("........")
      f3.write(api)
      f3.write("........")
      f3.write(str(s))
      f3.write("........%s"%number)
      f3.write("........")
      f3.write(str(time.time()))
      f3.write("\n")

def after_timeout():
  print("finish..........")

@timeout.set_timeout(300,after_timeout)
def run( mod,api,n):
  global totalAPI
  while True:
    # os.system("python39 test.py")
    # if platform.system() == "Linux":
    # 	s = os.system(" python39  apifuzzer.py %s %s %s"%(mod,api,n))


    # if platform.system() == "Darwin":
    # 	s = os.system(" python3.9  apifuzzer.py %s %s %s"%(mod,api,n))
    s = os.system("'Python-3.9.2/python'  apifuzzer.py %s %s %s"%(mod,api,n))
    totalAPI = totalAPI +2
      
    # t = t+2
    gen_log(mod,api,n,s)
    # return t




      



# while True:
#   run(mod,api,n)


t1 = time.time()
open("log.txt",'a').write(str(t1))
open("log.txt",'a').write("\n")

# run(mod,api,n)

moddic = json.load(open( 'doc/modules.json','r'))
# ignorelist = ["sigwait","crypt","binhex",'kill','killpg','tcflow','askokcancel',"askquestion"]
ignorelist =[]


# print(len(moddic.keys()))

# mcount = 0
for mod in list(moddic.keys()):
  # mcount = mcount + 1
  for api in moddic[mod]:
    if api in ignorelist:
      pass
    else:
      n = moddic[mod][api]["pn"][1]
      if n == 0:
        s = os.system("'Python-3.9.2/python'  apifuzzer.py %s %s %s"%(mod,api,n))
        gen_log(mod,api,n,s)
        totalAPI =totalAPI + 1
      else:
        run(mod,api,n)

			# print(mcount, mod,api,moddic[mod][api]["pn"])
			# stest(stresslist,mod,api,moddic[mod][api]["pn"][1])

print("...........finish..........")



t2 = time.time()

open("log.txt",'a').write(str(t2))
open("log.txt",'a').write("\n")
open("log.txt",'a').write("It takes ")
open("log.txt",'a').write(str(t2-t1))
open("log.txt",'a').write("\n")
open("log.txt",'a').write("Total API Calls: %s"%(str(totalAPI)))