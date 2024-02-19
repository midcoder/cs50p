#make a variable to start 
amount_due = 50
#loop until amount_due is greater than 0

while amount_due > 0 :
    #print the amount_due
    print("Amount due: ", amount_due)
    #ask the user to insert coin
    coin = int(input("Insert coin: "))
    #check if the coin is 25, 10 or 5 cents
    if coin in [5, 10 , 25]:
        #substract value from amount_due
        amount_due -= coin
#calculate change_owed
change_owed = abs(amount_due)

#print the result
print("Change owed: ", change_owed)
