import random
import string

#Karakterleri kendimizin seçtiği fonksiyon
#Function where we choose our own characters
def generate_password(length=12):
    characters=my_choice
    password="".join(random.choice(characters) for i in range(length))
    return password
#Karakterler random seçildiği fonksiyon
#Function where we choose random characters
def random_password(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(characters) for i in range(length))
    return password

if __name__=="__main__":
    print("1-I will choose my characters\n2-Random characters")
    a=input()
    if a=="1":
        my_choice=input("Input for your password which character,number or symbol want:")
        length=int(input("Input password length: "))
        generate_password=generate_password(length)
        print("Created password:",generate_password)
    elif a=="2":
        length=int(input("Input password length:"))
        random_password=random_password(length) 
        print("Created password:",random_password)
    else:
        print("Wrong input")


    

        

    
    