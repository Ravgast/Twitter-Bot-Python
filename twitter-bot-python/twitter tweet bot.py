from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from threading import Thread
from PIL import ImageTk
from tkinter import *
import tkinter as tk
import time

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

durum = True

sure = [0,0,0,0]
metin = '{0:02d}:{1:02d}:{2:02d}:{3:02d}'

def Login(): # 1. Pencere
    username = str(ent5.get())
    password = str(ent6.get())

    url = 'https://twitter.com/login'
    driver.get(url)

    time.sleep(2)
    searchInput=driver.find_element("name", "text") #Kullanıcı adı text kutusu
    time.sleep(1)
    searchInput.send_keys(username)
    searchInput.send_keys(Keys.ENTER)
    time.sleep(1)
    searchInput = driver.find_element("name", "password") #Şifre text kutusu
    time.sleep(2/3)
    searchInput.send_keys(password)
    searchInput.send_keys(Keys.ENTER)
    time.sleep(4)
 
def Login2(): # 2. Pencere
    username = str(ent2.get())
    password = str(ent4.get())

    url = 'https://twitter.com/login'
    driver2.get(url)

    time.sleep(2)
    searchInput=driver2.find_element("name", "text") #Kullanıcı adı text kutusu
    time.sleep(1)
    searchInput.send_keys(username)
    searchInput.send_keys(Keys.ENTER)
    time.sleep(1)
    searchInput = driver2.find_element("name", "password") #Şifre text kutusu
    searchInput.send_keys(password)
    searchInput.send_keys(Keys.ENTER)
    time.sleep(4)

def Tweet(ne):
    message = str(ent1.get('1.0', tk.END))
    # Tweet yazma kutusuna tıklayıp text kutusunu aktifleştirme
    searchInput = driver.find_element(By.XPATH, 
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
    searchInput.click()
    searchInput.send_keys(f' {ne} {message}  ') 
    # Tweet gönderme butonu
    searchInput = driver.find_element(By.XPATH, 
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
    searchInput.click()
    time.sleep(2)

def Tweet2(ne):
    message = str(ent1.get('1.0', tk.END))
    # Tweet yazma kutusuna tıklayıp text kutusunu aktifleştirme 
    searchInput = driver2.find_element(By.XPATH, 
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
    searchInput.click()
    searchInput.send_keys(f' {ne} {message}  ') 
    # Tweet gönderme butonu
    searchInput = driver2.find_element(By.XPATH, 
    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
    searchInput.click()
    time.sleep(2)

def Kronometre():
    if (durum):
        global sure
        sure [3]+=1
        if(sure[3]>=60):
            sure[3]=0
            sure[2]+=1
        if(sure[2]>=60):
            sure[1]+=1
            sure[2]= 0
        if(sure[1]>=60):
            sure[0]+=1
            sure[1]= 0

        sureformati = metin.format(sure[0],sure[1],sure[2],sure[3])
        label.configure(text=sureformati)
    form.after(10,Kronometre)

def End_data():
    driver.close()
    driver2.close()
    exit()

def Tur():
    xdd = int(ent3.get())

    Login()

    res = 1
    while res < xdd+1:
        time.sleep(2) 
        Tweet('. \n '+str(res)) # Tweetin başına . koyuyor ayrıyeten kaçıncı tweetse numarasını yazıyor çünkü aynı tweeti tekrar atamıyoruz
        time.sleep(2) # Nokta opsiyonel
        res+=1

def Tur2():
    xdd = int(ent3.get())

    Login2()

    res = 1
    while res < xdd+1:
        time.sleep(2)
        Tweet2('. \n '+str(res)) # Tweetin başına . koyuyor ayrıyeten kaçıncı tweetse numarasını yazıyor çünkü aynı tweeti tekrar atamıyoruz
        time.sleep(2) # Nokta opsiyonel
        res+=1

def Start():
    form.wm_attributes('-alpha',0.5)
    Thread(target=Kronometre).start()
    Thread(target=Tur).start()
    Thread(target=Tur2).start()

form = tk.Tk()
form.geometry('1000x500+450+250')
form.title('                                                                                                                                Twitter Bot by Ravgast')
form.state('normal')
form.resizable(False,False)
form.iconbitmap(r'C:\Users\ravga\Desktop\Twitter\tem.ico')

bg= ImageTk.PhotoImage(file="son_foto.png")

canvas= Canvas(form,width= 400, height= 200)
canvas.pack(expand=True, fill= BOTH)
canvas.create_image(0,0,image=bg, anchor="nw")

tk.Label(form, text="Ne yazacaksın :- ",
         font=("Gill Sans", 13), bg="#d9d9d9").place(x=70,y=30)
ent1 = tk.Text(form)
ent1.place(x=10, y=50, height=180, width=250)

tk.Label(form,text='Kullanıcı Adı',bg='#d9d9d9',font= 'Times 13 bold').place(x=420,y=25)
ent2 = tk.Entry(form)
ent2.place(x=350,y=50)
ent2.place(width=250,height=20)

tk.Label(form,text='Kaç Tweet ',bg='#d9d9d9',font= 'Times 13 bold').place(x=425,y=340)
ent3 = tk.Entry(form)
ent3.place(x=420,y=370)
ent3.place(width=100,height=20)

tk.Label(form,text='Sifre',bg='#d9d9d9',font= 'Times 13 bold').place(x=450,y=145)
ent4 = tk.Entry(form, show="*")
ent4.place(x=350,y=170)
ent4.place(width=250,height=20)

ent5 = tk.Entry(form)
ent5.place(x=350,y=82)
ent5.place(width=250,height=20)

ent6 = tk.Entry(form, show="*")
ent6.place(x=350,y=202)
ent6.place(width=250,height=20)

button1 = tk.Button(form, text="Start",
                    font=("black", 20), bg='green',
                    command=Start)
button1.place(x=100,y=350) 
button1.place(width=200,height=70)

button2 = tk.Button(form, text="Stop",
                    font=("black", 20), bg='red',
                    command=End_data)
button2.place(x=650,y=350) 
button2.place(width=200,height=70)

label = tk.Label(form,text='Sayaç',fg='Black',bg='#ffffff',font= 'Times 10 bold')
label.pack()
label.place(x=925,y=477)

label1 = tk.Label(form,text='1',fg='Black',bg='#ffffff',font= 'Times 13 bold')
label1.pack()
label1.place(x=335,y=48)

label2 = tk.Label(form,text='2',fg='Black',bg='#ffffff',font= 'Times 13 bold')
label2.pack()
label2.place(x=335,y=78)

label3 = tk.Label(form,text='1',fg='Black',bg='#ffffff',font= 'Times 13 bold')
label3.pack()
label3.place(x=335,y=170)

label4 = tk.Label(form,text='2',fg='Black',bg='#ffffff',font= 'Times 13 bold')
label4.pack()
label4.place(x=335,y=200)

form.mainloop()