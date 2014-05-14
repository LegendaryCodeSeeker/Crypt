FileName = raw_input("Type a File Name to save as")
Words = raw_input("type a couple of Sentence's(use only a-z 0-9 . ,  ' ! ? " )
Words = Words.lower()#makes it lowercase (Only lowercase will be encrypted)
File1 = open("Txt's\N!tro.txt","w")
File1.write(Words)#takes the input from the user and puts it in the txt file
File1.close()
File2 = open("Txt's\N!tro.txt","r")
File = File2.read() #Reads the file into a string
EncList = []
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','"',"'",'!','?','1','2','3','4','5','6','7','8','9','0']
EncAlphabet = ['*','/',',','-','%','r','<','!','+','$','1','^','0','=','&','I','`','X','.','9','4','q','_','p','o','"',' ']
for counter in range(0,len(File)):     #Take's the txt file and make's it a list
 EncList.append(File[counter])
counter = 0
for counter in range(0,len(File)):     #Encrypt's the file
 if EncList[counter] == Alphabet[0] :
  EncList[counter] = EncAlphabet[0]
 elif EncList[counter] == Alphabet[1] :
  EncList[counter] = EncAlphabet[1]
 elif EncList[counter] == Alphabet[2] :
  EncList[counter] = EncAlphabet[2]
 elif EncList[counter] == Alphabet[3] :
  EncList[counter] = EncAlphabet[3]
 elif EncList[counter] == Alphabet[4] :
  EncList[counter] = EncAlphabet[4]  
 elif EncList[counter] == Alphabet[5] :
  EncList[counter] = EncAlphabet[5]
 elif EncList[counter] == Alphabet[6] :
  EncList[counter] = EncAlphabet[6]
 elif EncList[counter] == Alphabet[7] :
  EncList[counter] = EncAlphabet[7]
 elif EncList[counter] == Alphabet[8] :
  EncList[counter] = EncAlphabet[8] 
 elif EncList[counter] == Alphabet[9] :
  EncList[counter] = EncAlphabet[9]
 elif EncList[counter] == Alphabet[10] :
  EncList[counter] = EncAlphabet[10]
 elif EncList[counter] == Alphabet[11] :
  EncList[counter] = EncAlphabet[11]
 elif EncList[counter] == Alphabet[12] :
  EncList[counter] = EncAlphabet[12]  
 elif EncList[counter] == Alphabet[13] :
  EncList[counter] = EncAlphabet[13]
 elif EncList[counter] == Alphabet[14] :
  EncList[counter] = EncAlphabet[14]
 elif EncList[counter] == Alphabet[15] :
  EncList[counter] = EncAlphabet[15]
 elif EncList[counter] == Alphabet[16] :
  EncList[counter] = EncAlphabet[16] 
 elif EncList[counter] == Alphabet[17] :
  EncList[counter] = EncAlphabet[17]
 elif EncList[counter] == Alphabet[18] :
  EncList[counter] = EncAlphabet[18]
 elif EncList[counter] == Alphabet[19] :
  EncList[counter] = EncAlphabet[19]
 elif EncList[counter] == Alphabet[20] :
  EncList[counter] = EncAlphabet[20]  
 elif EncList[counter] == Alphabet[21] :
  EncList[counter] = EncAlphabet[21]
 elif EncList[counter] == Alphabet[22] :
  EncList[counter] = EncAlphabet[22]
 elif EncList[counter] == Alphabet[23] :
  EncList[counter] = EncAlphabet[23]
 elif EncList[counter] == Alphabet[24] :
  EncList[counter] = EncAlphabet[24] 
 elif EncList[counter] == Alphabet[25] :
  EncList[counter] = EncAlphabet[25]
 else:
  EncList[counter] = EncAlphabet[26]
counter = 0

Encstring = "".join(EncList) #Makes a string out of the list
print ("").join(EncList)
File10 = open("Encrypted_Files\$" + FileName + ".D@a" , "w") #Saves it to a .D@a (Txt) File With a custom name 
File10.write(Encstring)
File10.close()
File2.close()
raw_input('press enter to exit')
