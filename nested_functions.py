def talk (phrase):
    def say (word):
        print(word)

    words = phrase.split(' ')
    for word in words :
        say (word)

talk('I am going to Bali')    

print("\n" "\n")

def counter ():
    count =0
    def increment():
        nonlocal count  #nonlocal allows us to access thge vcariable that was locally asigned at the def (count)
        count = count+1
        return count
    return increment
increment = counter()
print (increment())
print (increment())

