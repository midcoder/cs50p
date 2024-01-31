#define main function 
def main() :
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7 and time <= 8 :
        print("breakfast time")
    elif time >= 12 and time <= 13 :
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
     

#define a function that converts the input time into a float
def convert(time) :
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes   


if __name__ == "__main__" :
    main()