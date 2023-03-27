import os 
import platform
import signal, functools
import timeout
import json
import time



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

@timeout.set_timeout(600,after_timeout)
def run( mod,api,n):
  global totalAPI
  while True:
    
    s = os.system("'Python-3.9.2/python'  apifuzzer.py %s %s %s"%(mod,api,n))
    totalAPI = totalAPI +2
      
    # t = t+2
    gen_log(mod,api,n,s)
    # return t





t1 = time.time()
open("log.txt",'a').write(str(t1))
open("log.txt",'a').write("\n")

# run(mod,api,n)


modlist = [("ctypes","string_at",1),("ctypes","wstring_at",1),("os","abort",0),("posix","abort",0),("time","pthread_getcpuclockid",1),("signal","pthread_kill",2),
("nis","maps",1),("nis","cat",2),("builtins","input",1),("locale","dgettext",2),("imp","load_dynamic",2),("pdb","runeval",2),("pdb","run",1),("pdb","runctx",3),("dis","dis",1),
("dis","get_instructions",1),("dis","show_code",1),("ast","literal_eval",1),("builtins","compile",3),("builtins","exec",1),("ast","parse",1),("builtins","eval",1),
 ]
 




for item in modlist:
  mod = item[0]
  api = item[1]
  n = item[2]
  if n == 0:
    s = os.system("'Python-3.9.2/python'  apifuzzer.py %s %s %s"%(mod,api,n))
    gen_log(mod,api,n,s)
    totalAPI =totalAPI + 1
  else:
    run(mod,api,n)


print("...........finish..........")



t2 = time.time()

open("log.txt",'a').write(str(t2))
open("log.txt",'a').write("\n")
open("log.txt",'a').write("It takes ")
open("log.txt",'a').write(str(t2-t1))
open("log.txt",'a').write("\n")
open("log.txt",'a').write("Total API Calls: %s"%(str(totalAPI)))
