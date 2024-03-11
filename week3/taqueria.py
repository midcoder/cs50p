menu = {"Baja Taco": 4.25, 
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}
def get_price():
    while True:
        try: 
            key = input("Item: ").title().strip()
            if key in menu.keys():
                item = menu[key]
                print(f'Total: ${item:.2f}')
            
                
        except (EOFError, KeyError):
            break 
        
get_price()