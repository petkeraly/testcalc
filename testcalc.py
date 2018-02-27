print("Test calculator.\nThis is an example project made by Peter Dobosi.\n")
print("Type\n\nfor addition:\n   add or ADD or 1 or +\n\nfor substraction:\n   sub or SUB or 2 or -\n\nfor multiplication\n   mul or MUL or 3 or *\n\nfor division\n   div or DIV or 4 or /\n")
stri=input("What would you like to do?\n")
if stri=="ADD" or stri=="add" or stri=="1" or stri=="+":
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\nType\n yes or no\n")
      numsum=float(num1+num2)
      while booi=="yes" or booi=="y":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum+szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
if stri=="SUB" or stri=="sub" or stri=="2" or stri=="-":
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\n Type true or false: ")
      numsum=float(num1-num2)
      while booi=="true":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum-szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
