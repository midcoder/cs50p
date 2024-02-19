def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    for char in range(len(s)-1):
        if s[char].isnumeric():
            if s[char+1].isalpha():
                return False
    return True 

main()
    
    
