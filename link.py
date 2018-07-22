#在网页msg获取的
import requests
import time
from tkinter import *
import threading

root=Tk()
url = r'https://api.live.bilibili.com/ajax/msg'
form ={'roomid': 5096,'csrf_token' : '8555f03a84aaf5c5599091cdc7959e0c'}
alldm =[]

def dmall(howdm = 0,alldm =[]):
    html = requests.post(url,data=form)
    for dm in html.json()['data']['room']:
        if dm not in alldm:
            alldm.append(dm)
        if len(alldm)  >howdm:
            alldm.pop(0)
    return alldm

def textchange():
    global alldm
    text = ''
    time.sleep(1)
    alldm = dmall(10,alldm)
    print('--------------------------------------------------------------')
    for dm in alldm:
        print(dm['nickname'],' 说 ',dm['text'])
        text = text+dm['nickname']+' 说 '+dm['text']+'\n'
    text0.delete(1.0,END)
    text0.insert(END, text)
    root.after(500, textchange)

text0 = Text (width = 50,height=12)
text0.pack()
textchange()
root.mainloop()
