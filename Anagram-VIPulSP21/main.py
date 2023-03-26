def IsAnagram(s1, s2):
  a="True"
  s1=s1.lower()
  s2=s2.lower()
  s_1=[]
  for count in range(len(s1)):
    s_1.append(s1[count])
  s_2=[]
  for count in range(len(s2)):
    s_2.append(s2[count])

  s_1.sort()
  s_2.sort()
  if s_1==s_2:
    return a
  else:
    return not a
  pass

input1 = input()
input2 = input()
result = IsAnagram(input1, input2)
print(result)
