#my employe encapsulations
class Employe:
    def __init__(self , name , salary , jobs):
        self.name = name
        self.salary = salary 
        self.jobs = jobs 
    def show(self):
        print('Name : ' , self.name , " Salary : ", self.salary , "Jobs : " , self.jobs)
    def work(self):
        print(self.name, "is Working on" , self.jobs)

print('')
print('')
print('')

emp = Employe('Adam', 2000 , "Software Engineer")

emp.show()
emp.work()

 
#calculations 

def add(x,y):
    return x + y
def minus(x,y):
    return x - y
def multiply(x, y):
    return x * y 
def divide(x, y):
    return x / y


print("")
print('')
print('')
print("============== MY CALCULATOR =================")

print('1. Add number')
print('2. Minus Number')
print("3. Multiply Number")
print("4. Divide Number")

choice = input('Select the operations above (1/2/3/4) : ')
num1 = float(input('select number 1 : '))
num2 = float(input('select the number 2 : '))

#code
while True :
    if choice == '1':
        print( num1 , "+", num2, "=" , add(num1 , num2))
       
    elif choice == '2':
        print(num1 , "-", num2 , "=" , minus(num1 , num2))
        
    elif choice == "3":
        print(num1 , '*', num2 , '=' , multiply(num1 , num2))
        
    elif choice == "4":
        print(num1 , '/' , num2 , '=' , divide(num1 , num2))
        
    else:
        print('your in put not valid motherfucker')
        
    usernext = input('Wanna use it again? (y/n): ')

    if usernext == 'y':
        print(choice)
    else:
        print('Thanks for use it motherfucker')
        break

