#在网页msg获取的
import requests
import time
from tkinter import *

root=Tk()
url = r'https://api.live.bilibili.com/ajax/msg'
form ={'roomid': 5096,'csrf_token' : '8555f03a84aaf5c5599091cdc7959e0c'}
alldm =[]

def dmall():
    global alldm
    text = ''
    html = requests.post(url,data=form)
    for dm in html.json()['data']['room']:
        if dm not in alldm:
            alldm.append(dm)
        if len(alldm)  >10:
            alldm.pop(0)
        text = ''
        for dmin in alldm:
            text = text+dmin['nickname']+' 说 '+dmin['text']+'\n'
        text0.delete(1.0,END)
        text0.insert(END, text)
    root.after(100, dmall)

text0 = Text (width = 50,height=12)
text0.pack()
dmall()
root.mainloop()
