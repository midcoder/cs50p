tweet = input("Input: ").lower()

def remove_vowels(twt) :
    vowels = 'aeiou'
    new_tweet = ""
    for t in twt :
        #loop to find where the vowels are and adding the rest to the new variable 
        if t not in vowels :
            new_tweet += t
    return new_tweet

print("Output: ", remove_vowels(tweet))
