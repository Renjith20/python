


word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")

x = word1[0:1]

word1 = word1.replace(x,word2[0:1])

word2 = word2.replace(word2[0:1] , x)

print("first word : " , word1)
print("second word : " , word2)