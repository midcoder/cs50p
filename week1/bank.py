greet = input("Greeting: ")
greet = greet.lower()
if greet == "hello" :
    print("$0")
elif greet.startswith("h") :
    print("$20")
else :
    print("$100")