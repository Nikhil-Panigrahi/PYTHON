done = "True" #string returns true value all the times except when empty or 0

if done:
    print ("yes")
else :
    print("no")


done2 = 0
if done2:
    print ("yes")
else :
    print("no")


book_1_read = True
book_2_read = False
read_any_book =any([book_1_read , book_2_read])
print(read_any_book)

ingredients_purchased = True
meal_cooked = False
ready_to_serve =all([ingredients_purchased , meal_cooked])
print(ready_to_serve)