print("welcome to Zumaana bank\n")
chances = 3
balance = 1000
restart = ('y')
while chances >= 0:
  pin = int(input("enter your four digit pin: \n"))
  if pin == (1234):
    print("pin is correct\n")
    while restart not in ('n', 'no', 'NO', 'N'):
      print("please press 1 to check the balance\n")
      print("please press 2 to withdrawal the money\n")
      print("please press 3 to pay \n")
      print("please press 4 to return the card\n")
      option = int(input("would you like to do other operation?\n"))
      if restart in ('n', 'no', 'NO', 'N'):
        print("thank you\n")
        break
      if option == 1:
        print("your current balance is :", balance)
        restart = input("would you like to do other opertion?\n")
        if restart in ('n', 'no', 'NO', 'N'):
          print("thank you\n")
          break
      elif option == 2:
        withdrawal = float(input("enter the amount going to withdrawal:"))
        if withdrawal in [10, 20, 30, 40, 50]:
          balance = balance - withdrawal
          print("your current balance is :", balance)
          restart = input("would you like to perform other opertaion? \n")
          if restart in ('n', 'no', 'NO', 'N'):
            print("thank you\n")
            break
        elif withdrawal not in [10, 20, 30, 40, 50]:
          print("enter the valid amount\n")
        elif withdrawal == 1:
          print("enter the restain amount\n")
        elif option == 3:
          pay_in = float(input("enter the amount to add into:\n"))
          if pay_in in [10, 20, 30, 40, 50]:
            balance = pay_in + balance
            print("your current balance is :", balance)
            if restart in ('n', 'no', 'NO', 'N'):
              print("thank you\n")
              break
            else:
              print("please enter the valid amount\n")
        elif option == 4:
          print("please wait your operation is on processing....\n")
          print("thank you \n")
          break
  elif pin != (1234):
    print("you have enter the incorrect pin\n")
    chances = chances - 1
    if chances == 0:
      print("no more tries") 
      break       

