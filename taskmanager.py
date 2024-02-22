#ad/soyad/yaş bilgiler soruldugu fonksiyon
#name/surname/age asked information function
def user_information(ussname,passwd):
    name=input("Enter your name:")
    sur_name=input("Enter your surname:")
    age=input("Enter your age")
    ussname_=ussname+"task.txt"
    f=open(ussname_,"+a")
    f.write(passwd)
    f.write(f"\nName: {name}\n")
    f.write(f"Surname: {sur_name}\n")
    f.write(f"Birth Day: {age}\n")
    
    f.close()

#kayıt için bilgilerin alındığı fonksiyon
#function to retrieve information for registration
def sign_up():
    print("Enter your username do you want to acess ")
    username=input("Enter here:")
    password=input("Enter a password:")
    #şifre kullanıcı adıl ile aynı olamaz ve 3 harften fazla olmalı
    #the password can not same with username and must longer than 3 words
    if password==username:
        print("Username and password can not same")
        sign_up()
    elif len(password)<3:
        print("Short password.Make a longer password then 3 character")
        sign_up()
    else:
        #kullanıcı giriş yapmaya yonlendırılıyor
        #the user goes toward login
        user_information(username,password)
        print("You toward to login")
        login()
        
    
def login():
    #q ya basarak fonksiyondan cıkılır ve ana menüye dogru gidilebilir
    #if you press q you left the function and going to main menu
    print("İf you want quick press q")
    user_name=input("Enter here username:")
    if user_name=='q':
        print("\nYou are goin to main menu\n")
        main()
        return
    pass_word=input("Enter password:")+"\n"
    if pass_word=='q':
        print("\nYou are goin to main menu\n")
        main()
        return
    try:
        username=user_name+"task.txt"
        f_=open(username,"r")
        #dosyanın içini okur ve ilk satır ile parola doğruluğuna bakar
        #reads the first line in the file and verifies the password
        pswd=f_.readlines(0)[0]
        f_.close()
        
        if pass_word==pswd:
            while True:
                print("1--to view your data \n2--To add task \n3--Update task \n4--VIEW TASK STATUS\n5--exit")
                choice=input()
                if choice=="1":
                    view_data(username)
                elif choice=="2":
                    add_task(username)
                elif choice=="3":
                    update_task(user_name)
                elif choice=="4":
                    update_view_task(user_name)
                elif choice=="5":
                    #5 secildiğinde ana menuye yonlendirilir
                    #if you press 5 you goes to toward main menu
                    print("Bye Bye...")
                    main()
                    break
                else:
                    print("Wrong input!!")
        else:
            print("Your password or username is wrong!!")
            login()         
            
    except:
        print("We don't found your account.You toward to sign up")
        sign_up()

def view_data(username):
    ff=open(username,"r")
    #dosyanın içindeki ilk  3 satırı okur
    #reads the first 3 line  in the file
    print(ff.readline())
    print(ff.readline())
    print(ff.readline())
    ff.close()
def add_task(username):
    print("How many task you want add?")
    j=int(input())
    #ne kadar gorev girilecekse o kadar girdi alir
    #how many task do you give he will for you give input
    f1=open(username,"a")
    for i in range(1,j+1):
        task=input("enter here task:")
        target=input("enter here target:")
        f1.write(f"\nTask-{i}: {task}\n")
        f1.write(f"Target-{i}: {target}\n")
    f1.close()
               
def update_task(username):
    username=username+"task.txt"
    print("Enter your completed task:")
    completed=input()
    print("Enter task you atr still not started:")
    not_started=input()
    print("Enter task which are you doing:")
    doing_now=input()
    fw=open(username,"a")
    fw.write(f"Completed Task: {completed}\n")
    fw.write(f"Not yet started task: {not_started}\n")
    fw.write(f"On going task: {doing_now}\n")
def update_view_task(username):
    ussname=username+"task.txt"
    o=open(ussname,"r")
    print(o.read())
    o.close() 
def main():
    print("WELCOME TO TASK MANAGER")
    choice=input("if you a new user press 1\nYou have an account press 2:\nExit to press 3:\n")
    if choice=="1":
        sign_up()
    elif choice=="2":
        login()
    elif choice=="3":
        return
    else:
        print("wrong input")
if __name__=="__main__":
    main()
