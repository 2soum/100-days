import random
print ("Welocome to the PyPassword Generator !")
print("Choose your security : ")
print("1: Bad secure")
print("2: Meh secure")
print ("3: Good secure")
print("4: Giga secure")

choice = int(input())
minchar =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
maxchar = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minnum = ["0","1","2","3","4","5","6","7","8","9"]
charspec = ["!","#","$","%","&","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"]
all = minchar + maxchar + minnum + charspec

match choice:
    case 1 :
        password = []
        for i in range(0,8):
            password.append(random.choice(all))

        print("".join(password))

    case 2 :
        password = []
        for i in range(0,12):
            password.append(random.choice(all))

        print("".join(password))

    case 3 :
        password = []
        for i in range(0,16):
            password.append(random.choice(all))

        print("".join(password))

    case 4 :
        password = []
        for i in range(0,20):
            password.append(random.choice(all))

        print("".join(password))

    case _ :
        print("error")

