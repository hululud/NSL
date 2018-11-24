# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:06:19 2018

@author: liu
"""
def fileTest(strVal):
        lineNum = 0
        with open(r"proxy.conf", 'rt',encoding="utf-8") as file:
            for line in file.readlines():
                lineNum = lineNum + 1
                if strVal in line.strip():
                    return(lineNum)
                    break
import urllib.request
import win32con,win32api
url='https://www.nsl-net.com/link/kSqNBT7LdmoE6KoS?is_ss=1'
headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
req=urllib.request.Request(url=url,headers=headers)
f=urllib.request.urlopen(req)
data=f.read()
with open("proxy.conf","wb") as code:
    code.write(data)
linestart=fileTest('DIRECT = direct')
lineend=fileTest('[Proxy Group]')
win32api.SetFileAttributes('NSL.conf',win32con.FILE_ATTRIBUTE_NORMAL)
f=open('NSL.conf','w',encoding="utf-8")
with open(r"proxy.conf", 'rt',encoding="utf-8") as file:
    for i in file.readlines()[linestart:lineend-1]:
        f.write(i)
f.close()
win32api.SetFileAttributes('NSL.conf',win32con.FILE_ATTRIBUTE_READONLY)
import hashlib
hash=hashlib.md5(open('NSL.conf','rb').read()).hexdigest()
open(hash,'w')
print('all done')  