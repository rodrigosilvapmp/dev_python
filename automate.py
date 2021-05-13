#python library

#posicionamento da tela
#time.sleep(5)
#valor = pyautogui.position()
#print (valor)

# pyautogui.alert ('Fim')
# import pyautogui
# import time
# import pyperclip
#
#
# pyautogui.press("win")
# pyautogui.write ("chrome")
#
# pyautogui.press ("enter")
#
# pyautogui.PAUSE = 1
#
#
# pyautogui.hotkey('ctrl','t')
# link = "http://google.com.br"
# pyperclip.copy (link)
# pyautogui.hotkey('ctrl','v')
# pyautogui.press("enter")
#
# pyautogui.PAUSE = 1
# pyautogui.click(289, 312)
# pyautogui.write("Cotação dolar")
# pyautogui.press("enter")
#
# pyautogui.PAUSE = 1
#
# pyautogui.click(297, 416)
# pyautogui.doubleClick()
# pyautogui.hotkey('ctrl','c')
# valordolar = pyperclip.paste()
# print(valordolar)
#
# pyautogui.alert ('Fim da Cotação ' + valordolar)

#Convertendo strings e numeros
#print ("Qual é o seu nome? ")
#meuNome = input()
#print ("seu nome é " + meuNome)
#print (" seu nome tem o tamanho de ")
#print (len(meuNome))
#print ("Qual é a sua idade? ")
#minhaIdade = input()
#print ("Sua idade é de " +str(int(minhaIdade)))

#if (42==41):
#    print ("É igual")
#else:
#    print ("Não é igual")

#senha = "rodrigo"
#if (senha == "rodrigo"):
#    print ("Usuario ok")
#else
#    print ("Usuário errado")

#spam = 0
#while spam <5:
#	print ('Hello world!')
#	spam = spam +1

#for i in range(5):
#	print ('olá ' + str(i))

#import random
#random.randint (1,10)

# import tkinter as tk
#
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=400, height=300)
# canvas1.pack()
#
# entry1 = tk.Entry(root)
# canvas1.create_window(200, 140, window=entry1)
#
#
# def getSquareRoot():
#     x1 = entry1.get()
#
#     label1 = tk.Label(root, text=float(x1) ** 0.5)
#     canvas1.create_window(200, 230, window=label1)
#
#
# button1 = tk.Button(text='Enviar', command=getSquareRoot)
# canvas1.create_window(200, 180, window=button1)
#
# root.mainloop()

#print ("teste")


import pyautogui
import pyperclip


#pyperclip.copy("Teste")
#print (pyperclip.paste())

#def hello ():
#	print ("oLA")
#hello()

#def plusOne (number):
#	return number +1

#newNumber = plusOne(5)
#print (newNumber)

#def divisao (numero):
#	try:
#		return 10/numero
#	except ZeroDivisionError:
#	    print("Erroooo")
#print (divisao(2))

#def divisao (numero):
#	try:
#		return 10/numero
#	except:
#	    print("Erroooo")
#print (divisao(0))

#print ('oi')

#helloFile = open ('c:\\temp\\hello.txt')
#Single string
#conteudo = helloFile.read()
#lista de strings
#conteudo = helloFile.readlines()
#print (conteudo)
#helloFile.close()

#helloFile = open ('c:\\temp\\hello.txt', 'a')
#helloFile.write ('Aeeee 2')
#helloFile.close()

#import os
#os.getcwd()

import shutil
#shutil.copy('c:\\temp\\hello.txt', 'c:\\temp\\hello2.txt')
#shutil.rmtree('c:\\temp)

import webbrowser, sys
#import bs4
#import requests
#webbrowser.open("https://www.google.com.br")

#Rua = "Rua Antonio Cavalli, 219 Jardim morada do Sol, Indaiatuba SP"
#webbrowser.open("https://www.google.com.br/maps/place/" + Rua)

#res = requests.get ('https://www.amazon.com.br/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16FJ3ITY99DUZ&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1620921105&sprefix=automate+%2Caps%2C293&sr=8-1')
#res.raise_for_status()
#soup = bs4.BeautifulSoup(res.text, 'html.parser')

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.binary_location = "c:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe", )
#driver.get("https://www.google.com/")

