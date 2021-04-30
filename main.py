import random
from words import *
from ascii import *

def mer_str(s): # function to merge string
    emp_str=""
    for i in s:
        emp_str+=i
    return emp_str
print(logo) # from ascii 
dis=[] # a empty list for blanks
lives=6 #number of chances
word_list_length=len(word_list) #word_list is from words
rand_num=random.randint(0,word_list_length)
rand_word=word_list[rand_num]
word_len=len(rand_word)

win_var=True # variable that determines the end of the game

for j  in range (0,word_len):
        dis.append("_")

while win_var:  # games loop starts here
    if lives!=0:
        guess=input("Guess a letter:\n").lower()
        for i in range (word_len):
            if guess==rand_word[i]:
                dis[i]=rand_word[i]
        if guess not in rand_word:
            lives-=1
        final_str=mer_str(dis)
        if "_" not in final_str:
            win_var=False
            print("\nYou won")
        if lives==0:
            print("\nYou lost")
        if guess in final_str:
            print(f"You already guessd {guess}")
        print(final_str)
        print(stages[lives]) #stages is from ascii
