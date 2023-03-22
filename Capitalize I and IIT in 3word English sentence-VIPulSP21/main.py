(word1,word2,word3)=input().split()

word1=word1.lower()
word2=word2.lower()
word3=word3.lower()

if(word1=="i" or word2=="i" or word3=="i"):
  if(word1=="i"):
    word1="I"
  if(word2=="i"):
    word2="I"
  if(word3=="i"):
    word3="I"

word1=word1.replace("iit","IIT")
word2=word2.replace("iit","IIT")
word3=word3.replace("iit","IIT")

if(word3.endswith(".")):
  word3=word3
else:
  word3=word3+"."

print(word1, word2, word3)

#wthout using f, s, t = input().split()

# str=str(input())
# if (str.endswith(".")):
#   str=str
# else:
#   str=str+"."

# str=str.lower()
# str=str.replace("i ","I ")
# str=str.replace("iit","IIT")

# print(str)
