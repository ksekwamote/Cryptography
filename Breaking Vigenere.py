import pyperclip
#############################METHODS THAT RUN IN GUI##########################
char= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def longString(arr):
	maxi=0
	for i in range(len(arr)):
		if len(arr[i])>maxi:
			maxi=len(arr[i]);      #Finds the longest string out of the substrings
	return maxi

def substrings(word):
	count=0
	subs=[]
	realsubs=[]
	for i in range(len(word)):
		for j in range(len(word)):    # Finds common substrings in the ciphertext
			if word.count(word[i:j])>1:
				subs.append(word[i:j])
	for z in range(len(subs)):
		if len(subs[z])==longString(subs):
			realsubs.append(subs[z])
	
	return list(set(realsubs))

def spaceLen(string, sub):
	num= string.find(sub)
	return string[num+1:].find(sub)+1            

def commonFactor(fac):
	com=[]                               #Find the common factor that exist between sets of factos 
	comf=0
	for i in range(len(fac)):
		com=com+factor(fac[i])
	return list(set(com))

def factor(num):
	factors =[]
	for i in range(num):                #Finds the factors of a number 
		if i>1 and i<20:
			if num%i==0:
				factors.append(i)
	return factors

def keyLengthMethod(plaintext):
	subs= substrings(plaintext)        #Gives out a list of most possible key lengths 
	spacelengths=[]                      
	for num in range(len(subs)):
		spacelengths.append(spaceLen(plaintext,subs[num]))
	return commonFactor(spacelengths)

def entireKey(key, cipher):
	theKey=""
	for x in range(len(cipher)):           #repeats the key over and over to make it equal to the length of cipher or plaintext
		theKey=theKey+ key[x%len(key)]
	return theKey

def includeSpace(spaces,msg):
	ans=""                    #includes white space after it was removed
	count=0
	for i in range(len(msg)):
		if spaces[count]==" ":
			ans=ans+" "+msg[i]
			count=count+1
		else:
			ans=ans+msg[i]
		count=count+1
	return ans

def Dvigenere(key, text):                      #decrypts cipher
	enc=""
	char= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	spaces=text
	text=text.replace(" ","")
	key=entireKey(key,text)
	for num in range(len(key)):
		i = (char.find(text[num])-char.find(key[num]))%26
		enc=enc+char[i]
	enc=includeSpace(spaces,enc)
	return enc

def gr(index ,alpha,cipherT,lens):
   count=0                                 #Used to plot the graph of that illustrates the number of characters in sequence respectively
   for i in range(len(cipherT)):             #Takes in the characters in question,the character itself, the ciphertext and the length of the key
      if i%lens==index and cipherT[i]==alpha:
         count=count+1
   return (count/26)*15
   
         
      
   
########################  DRAWING THE INTERFACE  ######################################################
import numpy as np
import tkinter as tk         #import necessary packages to make GUI
import sys
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("1000x850")
root.title(" BREAKING THE VIGENER CIPHER")  #Create Window/Frame

var=StringVar()
L= Label(root,textvariable=var, relief=RAISED)
L.pack()
L.place(x=175,y=0)                       #create CipherText label
var.set("CIPHERTEXT")

cipher=Text(root, height=8,width=50)
cipher.pack()                            #InputBox to enter the cipherText
cipher.place(x=10,y=20)

vari=StringVar()
mess= Label(root,textvariable=vari , relief=RAISED)
mess.pack()
mess.place(x=150 ,y=160)
vari.set("DECRYPTED MESSAGE")             #Label for the Decrypted Message

msg=Text(root, height=8,width=50)       #Input box for decrypted message
msg.pack()
msg.place(x=10 ,y=180)


keyLength = Listbox(root)               #Scroll bar contain only possible key length(s)
keyLength.pack()
keyLength.place(x=450,y=25)

va=StringVar()
Le= Label(root,textvariable=va, relief=RAISED)  
Le.pack()
Le.place(x=450,y=200)
va.set("CHECK LETTER")

letter = Listbox(root)
letter.pack()
letter.place(x=450 ,y=220)

####################################################################################
def graphAlpha(index,plain,lens):
   i=index
   p=plain
   fig = plt.figure(figsize=(7,2))
   objects = ('A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
   y_pos = np.arange(len(objects))
   performance = [gr(i,'a',p,lens), gr(i,'b',p,lens) ,gr(i,'c',p,lens) ,gr(i,'d',p,lens) , gr(i,'e',p,lens) , gr(i,'f',p,lens) , gr(i,'g',p,lens) , gr(i,'h',p,lens) , gr(i,'i',p,lens) , gr(i,'j',p,lens) ,gr(i,'k',p,lens) , gr(i,'l',p,lens) , gr(i,'m',p,lens)  , gr(i,'n',p,lens) , gr(i,'o',p,lens) , gr(i,'p',p,lens) , gr(i,'q',p,lens) , gr(i,'r',p,lens) ,gr(i,'s',p,lens), gr(i,'t',p,lens) ,gr(i,'u',p,lens),gr(i,'v',p,lens),gr(i,'w',p,lens),gr(i,'x',p,lens),gr(i,'y',p,lens),gr(i,'z',p,lens)]
 
   plt.bar(y_pos, performance, align='center', alpha=0.5)
   plt.xticks(y_pos, objects)
   plt.ylabel('Frequencies')                              #Draws the graph that represents Frequences of charcters in the converted cipherText according to the selected character in the key listbox
   plt.title('Frequencies of Letters in the Sequence')

   canvas = FigureCanvasTkAgg(fig, master=root)
   plot_widget = canvas.get_tk_widget()
   plot_widget.grid(row=0, column=0)
   plot_widget.place(x=0, y=610)

############################FUNCTION TO BE CALLED BY BUTTONS########################################################


def keyLengths():
   if not cipher.get("1.0","end-1c").replace(" ",""): #Function that puts possible keyLength into the listbox
      print("Nothing in textBpx")
   else:
      lens=keyLengthMethod(cipher.get("1.0","end-1c").replace(" ",""))
      for x in range(0,len(lens)):
         keyLength.insert(x,lens[x])
def onselect(evt):
   w=evt.widget
   #print("selectted value is"+ str(keyLength.get(ANCHOR)))
   for i in range(keyLength.get(ANCHOR)):
      letter.insert(i,"L1")


def shiftCipher(value,index):
   index= int(index)      #Decrypts certain characters in the ciphertext according to the selected and shifted character in the keyListbox
   msg.delete(1.0,END)
   enc=""
   cipherText=cipher.get("1.0","end-1c").replace(" ","")
   if not cipherText:
      print("Nothing in textBpx")
   else:
      for i in range(len(cipherText)):
         if(i%int(keyLength.get(ANCHOR))==int(index)):
            t = (char.find(cipherText[i])-char.find(value))%26
            enc=enc+char[t].lower()
         else:
                 enc=enc+cipherText[i]
   msg.insert(END,enc)

def shiftnext():
   index= letter.curselection()[0]
   value= letter.get(ANCHOR)
   #shiftCipher(value,index)
   if value=="L1":
      letter.delete(index)
      letter.insert(index,"A")
   elif value=="Z":
      letter.delete(index)              #Shift to the next Alphabet/character 
      letter.insert(index,"A")
   else:
      letter.delete(index)
      i=char.find(value)
      letter.insert(index,char[i+1])
   

def shiftprev():
   index= letter.curselection()[0]
   value= letter.get(ANCHOR)
   if value=="L1":
      letter.delete(index)
      letter.insert(index,"Z")         #shift to the previous Alphabet
   elif value=="A":
      letter.delete(index)
      letter.insert(index,"Z")
   else:
      letter.delete(index)
      i=char.find(value)
      letter.insert(index,char[i-1])
   #shiftCipher(value,index)
def shift():
        shiftCipher(letter.get(ANCHOR),letter.curselection()[0])
   
def shiftCipher(value,index):
   index= int(index)
   enc=""
   cipherText=cipher.get("1.0","end-1c").replace(" ","")
   if not cipherText:
           print("Nothing in textBox")  #Converts characters in the cipherText at a certain index or position  e,g ABABAB -->   cABdAB
   else:
           for i in range(len(cipherText)):
                   if(i%int(keyLength.get(ANCHOR))==int(index)):
                           t = (char.find(cipherText[i].upper())-char.find(value.upper()))%26
                           enc=enc+char[t].lower()
                           print(cipherText[i])
                   else:
                           enc=enc+cipherText[i]
               
   graphAlpha(index,enc ,keyLength.get(ANCHOR))
   msg.delete(1.0,END)
   msg.insert(END,enc)


def decrypt():
        msg.delete(1.0,END)
        key=''.join(letter.get(0,tk.END))
        key=str(key)
        cip=Dvigenere(key,cipher.get("1.0","end-1c"))
        text_file = open("C:\\Users\\215077958\\Documents\\Crypto\\test.txt", "a")
        writes="\n"+cip+"\n KEY: \n"+key
        text_file.write("\n"+cip+"\n"+"KEY: "+key)
        text_file.close()
        msg.insert(END,cip)
        print(cip)
        pyperclip.copy(cip)
        
        

print(letter.get(0, tk.END))
###################################################################################
            
   
        

N= Button(root, text="SHIFT NEXT" , command=lambda:shiftnext())
P= Button(root, text="SHIFT PREV" , command=lambda:shiftprev())        #link Buttons to Methods/Fuctions
CHECK=Button(root, text="CHECK", command=lambda:shift())
keyLength.bind('<<ListboxSelect>>', onselect)
LENGTH=Button(root, text="KEYWORD LENGTH" ,command=lambda:keyLengths())
DECRYPT=Button(root, text="\n          DECRPT          \n",command=lambda:decrypt())
#################################################################################
#graphAlpha()
fig = plt.figure(figsize=(7,2))
objects = ('A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
y_pos = np.arange(len(objects))
performance = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)            #Draw Graph thats represents the frequency of respective letters in the english alphabet
plt.xticks(y_pos, objects)
plt.ylabel('Frequencies')
plt.title('Frequencies of Letters in the English Alphabet')

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)
plot_widget.place(x=0, y=400)
################################################################################

N.pack()
P.pack()
LENGTH.pack()
CHECK.pack()
DECRYPT.pack()
N.place(x=150, y=350)
P.place(x=60, y=350)
CHECK.place(x=240, y=350)
LENGTH.place(x=450, y=0)
DECRYPT.place(x=750, y=350)
root.mainloop()
