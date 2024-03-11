# Steps:
#  1. Finish dateToArray()
#  2. Finish isValidDate()
#  3. Finish dateToISO()
# See the tests for each function and understand what are the expected inputs and what should be the correct output for each one
# and why is the problem divided in such a way
# also, review the tests and add some more if you deem it necessary

# string -> [string]
# consumes a date string
# where the date has the format: MM/DD/YYYY or
#                                Month DD, YYYY
# and produces an array of strings with the format: [MM, DD, YYYY]
def dateToArray(input):
    # Hints:
    #   - You just need to turn a string made up form words and numbers, separated by spaces and commas,
    #     into an array that contains each word and number
    #   - It doesn´t matter what the string contains, just how it is separated
    #   - For convenience, remove all leading and trailing white space from your string; it will make your work easier
    #   - Option 1 [easier]: 
    #       - Does python have a built-in function that allows to *split* a string into separate values?
    #       - If so, which values should you choose to cut up the string? 
    #         Do you need to remove any characters before cutting the string?
    #         Does python have a built-in function for removing or *replacing* values within a string?
    dateArr = input.replace(",", " ").replace("/", " ").replace("  "," ").split(" ")
    #   - Option 2 [more labor intensive]:
    #       - How would you go through a string?
    #       - You want to check each character and if its a value you want to keep, save it somewhere (like a string)
    #         each item in the output array will be one of these sub-strings you form
    #       - Which character(s) in the string would help you to know where a word begins and ends? This is your delimiter
    #       - The number of unique delimiters you find inside your string should be 1 less 
    #         than the number of items in your output array, can you see why? 

    return dateArr 

# [string] -> boolean
# produces true if the given date array has the format [MM,DD,YYYY]
#          false otherwise 
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
def isValidDate(dateArr):
    # Hints:
    #   - Do you need to see every item in the array? or maybe just a couple of them? maybe just day and month
    #   - What takes for a month to be valid?         be 1-12 or jan-dec
    #   - What takes for a day to be valid?           1-31
    #   - The input array should have the format [MM,DD,YYYY] to be valid
    #     and only months can be a text value, so out of the 3 indexes in the array 
    #     only one could have a text value and still be a valid array
    #   - To know if a month in text form is valid you should check if it is in some set of values (maybe a list or a dictionary)

    #this contemplating that it uses the array from the function above which already has the array with the date
    #my logic is that the array is gonna be iterated to separate it and then check if the month and day are valid
    month, day, _ = dateArr
    if month in months.keys():
        month = months[month]
    try: 
        int_month = int(month)
        int_day = int(day)
    except:
        return False

    isValidMonth = int_month >= 1 and int_month <= 12
    isValidDay = int_day >= 1 and int_day <= 31

    return isValidMonth and isValidDay
    #first check in month is txt by checking months keys
    #if true check if day is valid
    #if month is a number then check months values and the check id day is valid 
    
    
# [string] -> string
# consumes a VALID date array with the format: [MM,DD,YYYY]
# produces a date string with the format: YYYY-MM-DD (ISO 8601)
def dateToISO(dateArr):
    # Hints:
        # At this point you're almost done, just need to do a few things more
        # You should replace any text value for a month with its numeric value (maybe use a dictionary, why?)
        # You should have an array that's ready to be *joined* into a string using the right delimiter 
        # find out if there is a built-in function to do this)
        # NOTE: here you might end up repeating the same logic you used in isValidDate() 
        #       to determine if a text valued month is valid or not
        #       Repetition should be avoided as much as possible, but in this case it is "simpler" to do it this way
        #       As a challenge you can try to avoid those repeated bits of logic (after you have finished the original problem)
        #       Hint: there are probably many ways to do this, one such way could be:
        #                       modify isValidDate() to produce False if the array isn't valid
        #                       and if the array is valid and it contains a month in text format then 
        #                       produce a new array with the value of the month replaced with its numeric value
        #                       Then you will need to modify the main() function to save the produced array if it was valid
        #                       and then pass that to the dateToISO() function
        #                       In the dateToISO() function you would need to remove the logic to replace the text formatted month
        #                       to its numeric value, since that functionality now lives in isValidDate()
        #                       Also you should update the tests to take these changes into account
    month, day, year = dateArr
    if month in months.keys():
        month = months[month]
        
    return (f'{year}-{month:>02}-{day:>02}')    

def main():
    try:
        while(True):
            dateStr = input("Date: ")
            dateArr = dateToArray(dateStr)
            if(isValidDate(dateArr)):
                break
        output = dateToISO(dateArr)
    except ValueError:
        raise ValueError("Error")
    
    print(output)

# Uncomment this after all tests pass
main()
    
# # Tests
# # Comment out this section after all tests pass
    
# ### Helper function for the tests, IGNORE THIS FUNCTION
# # [string] -> string
# # produces a string representation of the array
# def arrToStr(arr):
#     return f'{arr}'

# # To add new tests, just append your input strings to testInputs, testArrays, testValidArrays and testDates
# testInputs = ["8 September 1636", 
#               "Jan 1, 1984", 
#               "15/8/2015", 
#               "September 8, 1636", 
#               "January 1, 1984", 
#               "9/11/2001"]

# testArrays = [ ["8", "September", "1636"],
#                ["Jan", "1", "1984"],
#                ["15", "8", "2015"],
#                ["September", "8", "1636"],
#                ["January", "1", "1984"],
#                ["9", "11", "2001"] ]

# testValidArrays = [False, False, False, True, True, True]
# testDates = ["1636-09-08",
#              "1984-01-01",
#              "2001-09-11"]

# print("\n\nTests for dateToArray()")
# for i in range(len(testInputs)):
#     print(f'Input: {testInputs[i]:<17}, Expected: {arrToStr(testArrays[i]): <30}, Output: {arrToStr(dateToArray(testInputs[i])):<30}')

# print("\n\nTests for isValidDate()")
# for i in range(len(testArrays)):
#     print(f'Input: {arrToStr(testArrays[i]): <30}, Expected: {str(testValidArrays[i]): <5}, Output: {str(isValidDate(testArrays[i])):<30}')


# print("\n\nTests for dateToISO()")
# for i in range(len(testDates)):
#     print(f'Input: {arrToStr(testArrays[i+3]): <30}, Expected: {testDates[i]: <10}, Output: {dateToISO(testArrays[i+3]):<30}')

            
            
