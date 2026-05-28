expense=[]

print("<-------WELLCOME to Expense Tracker APP.------->")
while True:
  print("=============MENU============")
  print("1->Add Expense--------->")
  print("2->Viwe All Expense---->")
  print("3->Viwe Total Amount--->")
  print("3->Exit---------------->")

  choice=int(input("Enter your Choice:-->"))



  if(choice==1):
    Date=int(input("Enter your Date  (Whenyou buy something)==>"))
    category=input("Can you please tall me which product you buy . Like: Dress,Book==>")
    amount=float(input("Enter your amount==>"))

    Expense={
      "Date":Date,
      "category":category,
      "amount":amount
    }

    expense.append(Expense)

    print("Your all detailes are saved succesfully..Thank you so much. ")



  elif(choice==2):
     if(len(expense)==0):
        print("==NO Expense Add here .Please buy something And add here== ")
     else:
        print("Here your all Expense list")

        count=1
        for Each in expense:
           print(f" Number {count} ==-> The Date is {Each["Date"]} ,Your product is {Each["category"]} ,The Amount is {Each["amount"]}")
           count+=1
        
           print("THANK YOU ")



  elif(choice==3):
     
     total=0
     for Each in expense:
        total=total+Each["amount"]
     print( f" Your total amount is {total}.. " )



  elif(choice==4):
    print("......THANK YOU SO MUCH FOR THE USING MY APP.....")
    break
  else:
     print("Invalid Number.Please TRY AGAIN..!!!")  

     