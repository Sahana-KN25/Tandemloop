class smallCalculator:

    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        print("Addition of number1 and number2 is: ", self.number1 + self.number2)

    def subtraction(self):
        print("Subtraction of two numbers is: ", self.number1 - self.number2)

    def multiplication(self):
        print("Multiplication of two numbers is: ", self.number1 * self.number2)

    def division(self):
        print("Division of given numbers is: ", self.number1 / self.number2)

number1 = float(input("Enter number1:"))
number2 = float(input("Enter number2:"))

operations = smallCalculator(number1, number2)

while True:

    print("List of operations: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")

    selected_operation = int(input("Select the operation you want to perform: ")) 

    if selected_operation == 1:
        operations.addition()

    elif selected_operation == 2:
        operations.subtraction()

    elif selected_operation == 3:
        operations.multiplication()

    elif selected_operation == 4:
        operations.division()

    else:
        print("Wrong selection..! Try again.")
        break

    break
