def menu():    
    print('Please Enter 1 for Celsius conversion\n'
          'Enter 2 for Fahrenheit to Celsius conversion\n'
          'Or Enter 3 to exit the program\n')

#Function to convert from Celcius to Fahreneit
def menu1(number1):
    #number1= float(input("Enter the temperture in Celcius\n"))
    return (number1 * 9/5) + 32

def menu2(number1):
    #number1= float(input("Enter the temperture in Fahrenheit\n"))
    return (number1 - 32) * 5/9
def menu3(number1):
    
    return number1



def select(operation, number1):
    if operation == 1:
        return menu1(number1)
    elif operation == 2:
        return menu2(number1)
    elif operation == 3:
        return menu3(number1)
        

operation = 0                       
#while loop 
name = input('Please Enter your name:\n')
print('Welcome', name, 'to the Temperture Converter Application.')  
while operation !=3: 
    menu()
    operation = int(input("Enter the choice\n"))
    if operation == 1:
        number1= float(input("Please Enter your temperture in Celcius\n"))
        result = select(operation, number1)
        print("Computing... \n")
        print ("The temperture in Fahrenheit is", result)
        print()
        menu()
    elif operation == 2:
        number1= float(input("Please Enter your temperture in Fahrenheit\n"))
        result = select(operation, number1)
        print("Computing... \n")
        print ("The temperture in Celsius is", result)
        print()
        menu()
    elif operation == 3:
        print("Exiting...\n")
        print("Thank you for using the temperture convertor Application")
    
    else:
        print("This is not an option")
