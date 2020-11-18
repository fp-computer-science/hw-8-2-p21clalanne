# Author CL 11/16/2020 

word1 = input("What is your first word? ")
word2 = input("What is your second word? ")

list1 = list(word1)
list2 = list(word2)

list1.sort()
list2.sort()

if list1 == list2:
    print("Words are anagrams")
else:
    print("Word is not an anagram")


