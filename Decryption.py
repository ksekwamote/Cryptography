import pyperclip
def Dcaesar(key , plaintext):
	char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?:;,.-()"
	count = len(plaintext)
	plaintext= plaintext.replace("'","")
	text =""
	for num in range(count):
		text = text+ char[(char.find(plaintext[num])-key)% len(char)]
	return(text)

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
cipher= raw_input("what type of cipher do you want to use, 'caesar' or 'vigenere':  ")
key=raw_input("state your key:  ")
plaintext=raw_input("Type the plaintext:  ")
answer=""
if(cipher.lower()=="caesar"):
        answer=Dcaesar(int(key) , plaintext)
        text_file = open("215077958_Caesar_Decrypt.txt", "a")
        text_file.write("\n"+answer+"\n")
        text_file.close()
else:
        answer=Dvigenere(key.upper(),plaintext.upper())
        text_file = open("215077958_Vigenere_Decrypt.txt", "a")
        text_file.write("\n"+answer+"\n")
        text_file.close()
        
pyperclip.copy(answer)
print(answer)

