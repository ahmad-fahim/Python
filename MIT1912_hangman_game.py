#Name : Fahim Ahmad
#Batch : MIT19
#Class Roll : 12

import random

Bag_of_words = ["bag", "array", "game", "cricket", "football", "table",
                "information", "technology", "division", "chair", "flower",
                "calender", "laptop", "python", "computer", "engineering",
                "mouse", "pen", "pan", "light", "sun", "moon", "mobile",
                "massage", "message", "word", "world", "universe", "facebook",
                "twitter", "university"]

Bag_of_array_len = len(Bag_of_words)
#print(Bag_of_words)

user_input_string = ""

word_position = random.randint(0, Bag_of_array_len-1)

search_word = Bag_of_words[word_position]

search_word_len = len(search_word)
print("Length of word : ", search_word_len)

while search_word_len > 0 :
    user_input_string = user_input_string + "*"
    search_word_len -= 1
print(user_input_string)

try_counter = 0
correct_try = 0

while user_input_string != search_word :
    user_input = input("Input a letter : ")
    index = 0 
    flag = 0
    for word in search_word :
        if user_input == word :
            list1 = list(user_input_string)
            list1[index] = user_input
            user_input_string = ''.join(list1)
            flag = 1
        index += 1
    #else:
    if flag == 1 :
        correct_try += 1         
        
    print(user_input_string)
    try_counter += 1
    
print ("You Won !!!!!!")
print ("Numner of try =", try_counter)
print ("Numner of correct try =", correct_try  )
print ("Numner of wrong try =", try_counter - correct_try  )


