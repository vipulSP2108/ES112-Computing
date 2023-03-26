letter=input()
dictx={}
for i in range(len(letter)):
  dictx[letter[i]]=letter.count(letter[i])

listx=list(dictx.items())
listx.sort()
for a in range(len(listx)):
  tu=listx[a]
  print(tu[0],tu[1])
