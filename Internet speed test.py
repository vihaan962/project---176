# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:39:04 2022

@author: VIHAAN KATHURIA
"""


import speedtest
import matplotlib.pyplot as plt
import time

list_download_speed = []
list_upload_speed = []


for i in range(5):
    st = speedtest.Speedtest()
    download_speed=round(st.download()/1000000,2)
    list_download_speed.append(download_speed)   
       
    upload_speed=round(st.upload()/1000000,2)
    list_upload_speed.append(upload_speed)
    time.sleep(60)
    
    print(list_download_speed)
    print(list_upload_speed)
    
x = [1,2,3,4,5]

plt.plot(x,list_download_speed,label = "download speed")
plt.plot(x,list_upload_speed,label = "upload speed")
plt.title("speed")
plt.legend()
plt.show()




