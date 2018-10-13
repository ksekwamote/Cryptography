#import enchant 
import pyperclip
def most(word):
	maxi=0                          #letter than occurs the most 
	char='q'
	for num in range(len(word)):
		if word.count(word[num])>maxi:
			maxi=word.count(word[num])
			char=word[num]
	return char

def Dcaesar(key , plaintext):
	char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?:;,.-()"
	count = len(plaintext)
	text =""
	for num in range(count):
		text = text+ char[(char.find(plaintext[num])+key)% len(char)]
	return text

def breakCaesar(word):
	pos = ['a' ,'e','i','o','u',' ']
	char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?:;,.-()"  #test it against single most common charactcters
	for num in range(len(pos)):
		chara=most(word)
		key= abs(char.find(chara)-char.find(pos[num]))
	
	print(Dcaesar(key,word))
	print("KEY: "+str(key))
	text_file = open("215077958_Caesar_Break.txt", "a")
	text_file.write("\n"+"ANSWER"+Dcaesar(key,word)+"\n"+" KEY: "+ str(key))
	text_file.close()
	pyperclip.copy(answer)

cipher= input("what type of cipher do you want to break, 'caesar' or 'vigenere':")

plaintext=input("Type the plaintext:")
answer=" "
if cipher=="caesar":
        breakCaesar(plaintext)
else:
        filename=r'''Breaking Vigenere.py'''
        exec(open(filename).read())
        
