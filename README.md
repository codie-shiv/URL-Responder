# URL_Responder
A handy script for bug bounty hunters/pentesters to check the http status code of all the links(URLs) collectively \
So you'll never have to worry about checking a bunch of URLs manually... 


![responder](https://user-images.githubusercontent.com/80361940/113623774-6d5f3800-967c-11eb-9423-bbae6b2498dc.JPG)



1. NOTE: Remember to put the extension i.e. ".txt" at the end of file name 
2. NOTE: The target list on which you are going to test should be in the same path/directory as your program file \
3. For demo purposes I've added a file named "demo.txt". You may use it to check the working of the script if you want in case.

# Tested on:
* Kali Linux
* Parrot Security OS
* Windows OS
* Termux

# Requirements:
1. git (not necessary in case of Windows OS)
2. Python3 (having latest version is better)


# Installation & Usage
* `Termux` \
\
$ pkg install git\
$ pkg install python \
$ pip install requests \
$ git clone https://github.com/codie-shiv/URL-Responder \
$ cd URL-Responder \
$ python responder.py \
\
After that enter the file name where you have stored all your URLs

` `
* `Windows` 

1. Download and Extract the zip. 
2. Run the python file i.e. responder.py 
3. Done! 

* `Linux` \
\
$ sudo apt install git \
$ sudo apt install python \
$ pip install requests \
$ git clone https://github.com/codie-shiv/URL-Responder \
$ cd URL-Responder \
$ python responder.py \

Thanks for your visit guys! Hope that you loved my work! \
This script is dedicated to Mr. Anand M Nandurkar (My Computer Science Teacher in school days.. )
