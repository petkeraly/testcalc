print("\n\nTest calculator.\nThis is an example project made by Peter Dobosi.\n")
print("Type\n\nfor addition:\n   add or ADD or 1 or +\n\nfor substraction:\n   sub or SUB or 2 or -\n\nfor multiplication\n   mul or MUL or 3 or *\n\nfor division\n   div or DIV or 4 or /\n\nto quit\n quit or QUIT or 5\n")
stri=input("What would you like to do?\n")
if stri=="ADD" or stri=="add" or stri=="1" or stri=="+":
      print("You chose addition.\n")
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\nType\n yes or no\n")
      numsum=float(num1+num2)
      while booi=="yes" or booi=="y":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum+szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
elif stri=="SUB" or stri=="sub" or stri=="2" or stri=="-":
      print("You chose substraction.\n")
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\n Type yes or no\n")
      numsum=float(num1-num2)
      while booi=="true":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum-szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
elif stri=="MUL" or stri=="mul" or stri=="3" or stri=="*":
      print("You chose multipication.\n")
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\n Type yes or no\n")
      numsum=float(num1*num2)
      while booi=="true":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum*szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
elif stri=="DIV" or stri=="div" or stri=="4" or stri=="/":
      num1=float(input("Please enter the first operand: "))
      num2=float(input("Please enter the second operand: "))
      booi=input("Would you like to use more operands?\n Type yes or no\n")
      numsum=float(num1/num2)
      while booi=="true":
            szam=float(input("What\'s your operand?\n"))
            numsum=numsum/szam
            booi=input("Would you like to use another operand?\n")
      print (numsum)
elif stri=="quit" or stri=="QUIT" or stri=="5":
      print("You have selected the option to quit.\nGoodbye, have a nice day!")
else:
      print("Unknown input")
print("Program finished.\nQuitting...")

