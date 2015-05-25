import sys,os,hashlib, time

sep = "---------------"
def encrypt(s):
    md5 = hashlib.new('md5')
    md5.update(s)
    return md5.hexdigest()

def readfile(f): 
    l = open(f,'r')
    data = l.readlines()
    l.close()
    return data

def readcsv(f):
    l = open(f, 'r')
    data = l.read()
    l.close()
    return data.split(",") #returns words in a list

# ------------------------------------------------
def crack(wordFile, _hash): #This method expects words to be on seperate lines...
    wordlist = readfile(wordFile)
    for line in wordlist:
        e = encrypt(line)
        if e == _hash:
            print "%s\nFound hash!\nThe cracked pass is %s\n%s\n\nFinished! " %(sep,line,sep)
            break
        else:
           "Failed with => %s : %s"%(line,e)
# ------------------------------------------------
def crackfromCSV(CSV_file, _hash):
    csv_list = readcsv(CSV_file) #Store the values that were comma sep. in a list
    for item in csv_list:
        enc_item = encrypt(item)
        if enc_item == _hash: #If the word we encrypted is equal to the hash
            print "%s\nFound hash!\nThe cracked pass is %s\n%s\n\nFinished! " %(sep,item,sep) #Print word
            break
        else:
            print "Failed with => %s : %s"%(item, enc_item)
# ------------------------------------------------






# Crack from a line seperated wordlist or CSV file
#crack("wordlists/conficker.txt","1e6947ac7fb3a9529a9726eb692c8cc5")
#crackfromCSV("../mthesaur.txt", "1e6947ac7fb3a9529a9726eb692c8cc5")

crackfromCSV("wordlists/mthesaur.txt", "1e6947ac7fb3a9529a9726eb692c8cc5")












