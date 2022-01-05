#choosing to write the mathematical operations as functions 

#addition function: accepts 2 variables to add together 
def add (x,y):
  #sum variable holds sum of x & y
  sumOf = x + y
  #print sum
  print(sumOf)

#multiply function: accepts 2 variables to multiply together 
def multi (x,y):
  
  product = x * y
  print(product)

#division function: accepts 2 variables to divide 
def div(x,y):
  division = x / y
  print(division)

#subtraction function: accepts 2 variables to subract from one another
def sub(x,y):
  subtract = x - y
  print(subtract)


print("Select operation.")
print("1.Add (+)")
print("2.Sub (-)")
print("3.Mul (*)")
print("4.Div ")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # if the choice is '1', simply add two numbers
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        # if the choice is '2', simply subtract two numbers
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        # if the choice is '3', simply multiply two numbers 
        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        # if the choice is '3', simply multiply two numbers 
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
        else:
          print("Invalid Input")