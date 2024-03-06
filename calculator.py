#2 sayılı işlem fonksiyonu
#2 numbered operation function
def result_2(num1,num2,select):
    if select==1:
        print("Result:",num1+num2)   
    elif select==2:
        print("Result: ",num1-num2)  
    elif select==3:
        print("Result: ",num1*num2)
    elif select==4:
        print("Result: ",num1/num2)
    else:
        print("Wrong input")
#3 sayılı işlem fonksiyonu
#3 numbered operation function
def result_3(num1,num2,num3,select):
    if select==1:
        print("Result:",num1+num2+num3)   
    elif select==2:
        print("Result: ",num1-num2-num3)  
    elif select==3:
        print("Result: ",num1*num2*num3)
    elif select==4:
        print("Result: ",(num1/num2)/num3)
    else:
        print("Wrong input")
#4 sayılı işlem fonksiyonu
#4 numbered operation function
def result_4(num1,num2,num3,num4,select):
    if select==1:
        print("Result:",num1+num2+num3+num4)   
    elif select==2:
        print("Result: ",num1-num2-num3-num4)  
    elif select==3:
        print("Result: ",num1*num2*num3*num4)
    elif select==4:
        print("Result: ",((num1/num2)/num3)/num4)
    else:
        print("Wrong input")

 

     



print("Welcome to the calculator application\n")
print("What operation do you want to do?\n")
print("1-Total\n2-Subtract\n3-Multiply\n4-Divide")
select=int(input())
print("How many number do you want to operate with?\n2/3/4")
number=int(input())
#Kaç sayı kullanılacağı öğrenme ve fonksiyonlara yönlendirme
#Learning how many numbers to use and directing to functions
if number==2:
    num1=int(input("number 1: "))
    num2=int(input("number 2:"))
    print(result_2(num1,num2,select))
    
    
elif number==3:
    num1=int(input("number 1: "))
    num2=int(input("number 2:"))
    num3=int(input("number 3:"))
    print(result_3(num1,num2,num3,select))

elif number==4:
    num1=int(input("number 1: "))
    num2=int(input("number 2:"))
    num3=int(input("number 3:"))
    num4=int(input("number 4:"))
    print(result_4(num1,num2,num3,num4,select))
else:
    print("Wrong input")



