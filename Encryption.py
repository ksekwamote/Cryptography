import pyperclip
def Ecaesar(key , plaintext):
	char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?:;,.-()"
	count = len(plaintext)
	text =""
	for num in range(count):
		text = text+char[(char.find(plaintext[num])+key)% len(char)]
	text_file = open("215077958_CAESAR_CIPHER.txt", "a")
	text_file.write(text+"\n")
	text_file.close()
	pyperclip.copy(text)
	print(text)


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

def Evigenere(key, plaintext):
        enc=""
        char= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        spaces=plaintext                    #encrypt plaintext
        plaintext=plaintext.replace(" ","")
        key=entireKey(key,plaintext)
        for num in range(len(key)):
                i = (char.find(key[num])+char.find(plaintext[num]))%26
                enc=enc+char[i]
        enc=includeSpace(spaces,enc)
        text_file = open("215077958_VIGENERE_CIPHER.txt", "a")
        text_file.write(enc +"\n")
        text_file.close()
        pyperclip.copy(enc)
        print(enc)


cipher= raw_input("what type of cipher do you want to use, 'caesar' or 'vigenere':")
key=raw_input("state your key:")
plaintext=raw_input("Type the plaintext:")

def chose(ans):
        answer=""
        if(ans.lower()=="vigenere"):

               return(Evigenere(key.upper(),plaintext.upper())) 
                
        else:
                return(Ecaesar(int(key) , plaintext))     
             
chose(cipher)
