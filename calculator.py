number_one = int(input("Enter a number: "))
operand = input("Choose an operand (+, -, *, /):")
number_two = int(input("Enter another number:"))
if operand == "+":
  print(number_one + number_two)
if operand == "-":
  print(number_one - number_two)
if operand == "*":
  print(number_one * number_two)
if operand == "/":
  print(number_one / number_two)