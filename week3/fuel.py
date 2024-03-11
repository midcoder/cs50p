while True:
    x = input('Fraction: ')

    try:
        str_numerator, str_denominator = x.split('/')
        numerator = int(str_numerator)
        denominator = int(str_denominator)
        fraction = numerator / denominator
        if fraction <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
percentage = int(fraction * 100)
if percentage <= 1 :
    print('E')
elif percentage >= 99:
    print('F')
else:
    print(f'{percentage}%')



            
             
           


    

