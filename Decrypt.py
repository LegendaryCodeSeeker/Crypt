from os import listdir

Folder_Content = listdir("Encrypted_Files/") #list the entire content of the directory (Thank's to "Egbie Anderson" For helping me)
for counter in range(0,len(Folder_Content)):
    print counter, " ----> " , Folder_Content[counter]
counter = 0

def Decrypt(File2,Folder_Content):
 EncList = []
 Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
 EncAlphabet = ['*','/','z','-','%','r','<','!','+','$','9','^','i','=','&',',','`','x','.','u','8','p','2','4','w','"',' ']
 for counter in range(0,len(File2)):
  EncList.append(File2[counter])           
 counter = 0
 for counter in range(0,len(File2)):       #Decrypt's the file
  if EncList[counter] == EncAlphabet[0] :
   EncList[counter] = Alphabet[0]
  elif EncList[counter] == EncAlphabet[1] :
   EncList[counter] = Alphabet[1]
  elif EncList[counter] == EncAlphabet[2] :
   EncList[counter] = Alphabet[2]
  elif EncList[counter] == EncAlphabet[3] :
   EncList[counter] = Alphabet[3]
  elif EncList[counter] == EncAlphabet[4] :
   EncList[counter] = Alphabet[4]  
  elif EncList[counter] == EncAlphabet[5] :
   EncList[counter] = Alphabet[5]
  elif EncList[counter] == EncAlphabet[6] :
   EncList[counter] = Alphabet[6]
  elif EncList[counter] == EncAlphabet[7] :
   EncList[counter] = Alphabet[7]
  elif EncList[counter] == EncAlphabet[8] :
   EncList[counter] = Alphabet[8] 
  elif EncList[counter] == EncAlphabet[9] :
   EncList[counter] = Alphabet[9]
  elif EncList[counter] == EncAlphabet[10] :
   EncList[counter] = Alphabet[10]
  elif EncList[counter] == EncAlphabet[11] :
   EncList[counter] = Alphabet[11]
  elif EncList[counter] == EncAlphabet[12] :
   EncList[counter] = Alphabet[12]  
  elif EncList[counter] == EncAlphabet[13] :
   EncList[counter] = Alphabet[13]
  elif EncList[counter] == EncAlphabet[14] :
   EncList[counter] = Alphabet[14]
  elif EncList[counter] == EncAlphabet[15] :
   EncList[counter] = Alphabet[15]
  elif EncList[counter] == EncAlphabet[16] :
   EncList[counter] = Alphabet[16] 
  elif EncList[counter] == EncAlphabet[17] :
   EncList[counter] = Alphabet[17]
  elif EncList[counter] == EncAlphabet[18] :
   EncList[counter] = Alphabet[18]
  elif EncList[counter] == EncAlphabet[19] :
   EncList[counter] = Alphabet[19]
  elif EncList[counter] == EncAlphabet[20] :
   EncList[counter] = Alphabet[20]  
  elif EncList[counter] == EncAlphabet[21] :
   EncList[counter] = Alphabet[21]
  elif EncList[counter] == EncAlphabet[22] :
   EncList[counter] = Alphabet[22]
  elif EncList[counter] == EncAlphabet[23] :
   EncList[counter] = Alphabet[23]
  elif EncList[counter] == EncAlphabet[24] :
   EncList[counter] = Alphabet[24] 
  elif EncList[counter] == EncAlphabet[25] :
   EncList[counter] = Alphabet[25]
  else:
   EncList[counter] = Alphabet[26]
 Decstring = "".join(EncList)
 print ''.join(EncList)
 File10 = open("Decrypted_Files\Finished.txt","w")
 File10.write(Decstring)
 File10.close()
 FileLast = File.read()
 File.close()
 
GetUserInput = raw_input ('What file would you like to Decrypt?(Only 16 files Will be able to be Chosen from): ')
while not GetUserInput.isdigit():
    GetUserInput = raw_input("That was not a number. Please give me a number: ")
Number = int(GetUserInput)
if int(Number) == 0 :
    File = open("Encrypted_Files/" + Folder_Content[0], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 1 :
    File = open("Encrypted_Files/" + Folder_Content[1], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 2 :
    File = open("Encrypted_Files/" + Folder_Content[2], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 3 :
    File = open("Encrypted_Files/" + Folder_Content[3], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 4 :
    File = open("Encrypted_Files/" + Folder_Content[4], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 5 :
    File = open("Encrypted_Files/" + Folder_Content[5], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 6 :
    File = open("Encrypted_Files/" + Folder_Content[6], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 7 :
    File = open("Encrypted_Files/" + Folder_Content[7], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 8 :
    File = open("Encrypted_Files/" + Folder_Content[8], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 9 :
    File = open("Encrypted_Files/" + Folder_Content[9], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 10 :
    File = open("Encrypted_Files/" + Folder_Content[10], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 11 :
    File = open("Encrypted_Files/" + Folder_Content[11], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 12 :
    File = open("Encrypted_Files/" + Folder_Content[12], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 13 :
    File = open("Encrypted_Files/" + Folder_Content[13], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 14 :
    File = open("Encrypted_Files/" + Folder_Content[14], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
elif int(Number) == 15 :
    File = open("Encrypted_Files/" + Folder_Content[15], "r")
    File2 = File.read()
    Decrypt(File2,Folder_Content)
   

raw_input('press enter to exit')
