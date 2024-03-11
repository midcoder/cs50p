#create an empty dict
groceries = {}
#create a fucntion that prompts the user to make a list
def grocery():
#Use while to catch any errors and set when to stop the list
    while True:
        try: 
            #ask the user for input
            key = input().strip().upper()
            #check if key in groceries and add 1 to the count
            if key in groceries:
                groceries[key] += 1
            #else if not in dict set the count to 1
            else:
                groceries[key] = 1


        except (EOFError, KeyError):
            break

grocery()
#use a loop to print every item on the dictionary 
for item, count in groceries.items():
    print(f'{count} {item}')