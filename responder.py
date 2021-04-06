#!/bin/bash
try:
    import requests
    from time import sleep
    import os.path
    import sys
except ImportError:
   exit("install requests/dependencies and try again ...")

banner = """
  _   _   _   _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( U | R | L |   | R | e | s | p | o | n | d | e | r )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

 Author:           Codie Shiv
 Special Thanks:   Mr. Ichigo kurosaki
 Instagram :       www.instagram.com/codie_shiv
 Github:           www.github.com/codie-shiv
 """



def responder(lst):
    lis = open(lst,'r')
    read_lis = lis.readlines()
    for i in read_lis:
        i = i.replace('\n', '')
        try:
            if i.startswith("http://") is False:
               i = "http://" + i
            response = requests.get(i)
            status = response.status_code
            print(i + " --> " + str(status))
            sleep(1)
        except KeyboardInterrupt:
            print; exit()
        except:
         print(i + " --> could not connect!! try again..")



def main(__bn__):
   print(__bn__)
   print(" ")
   print("NOTE: \"The target file should be in the same directory as this file is...\" \n\"If not, then copy/move it here\"\n")
   while True:
      try:
         a = input("Enter your file name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   responder(a) 

if __name__ == "__main__":
    main(banner)


