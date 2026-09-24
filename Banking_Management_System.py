user_name="kajal"
account_number=123456789
password=6070
upi_pin=9050
        
balance=0
def cash_deposit():
    while True:
       ac=int(input("enter your account number :"))
       pas=int(input("enter your password : "))
       up=int(input("enter your upi_pin : "))
       if ac!=account_number or pas!=password or up!=upi_pin:
          print("wrong try checking  your account number or password or upi pin your item should  matached")
          continue
       break
    print("loging sucessful")
    amount=0
    while True:
        money=int(input("enter your desired amount :"))
        if money == 0 or money == "" or money<0:
            print(" sorry please enter valid amount ")
            continue
        amount+=money
        with open("balance.txt","a") as file:
         file.write(f"Deposited:{money},Balance:{amount}\n")
        print("money DEPOSITED , congratulations now your account balance is :",amount)
        break
    return amount
def cash_withdraw():
    while True:
           ac=int(input("enter your account number :"))
           pas=int(input("enter your password : "))
           up=int(input("enter your upi_pin : "))
           if ac!=account_number or pas!=password or up!=upi_pin:
              print("wrong try checking  your account number or password or upi pin your item should  matached")
              continue
           break
    print("loging sucessful")
    amount=0
    while True:
            money=int(input("enter your desired amount :"))
            if money == "" or money== 0 or money<0:
                print("please enter a valid amount")
                continue
            amount-=money
            with open("balance.txt","a") as file:
                  file.write(f"Withdrawn:{money},Balance:{amount}\n")
            print("Amount of :",amount,"has been deduted from your acount ")
            break
    return amount
def check_balance():
      with open ("balance.txt","r") as file :
            history=file.read()
            print(history)
welcome=input("you can 'check your balance','cash deposit','cash withdraw' within your account : ").lower()
if welcome=="check":
    check_balance()
if welcome=="cash deposit":
    cash_deposit()
if welcome=="cash withdraw":
     cash_withdraw()