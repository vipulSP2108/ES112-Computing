def Upper_Lower(s):
  resultUpper=0
  resultLower=0
  A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for count in range(len(s)):
    if s[count] in A:
      resultUpper=resultUpper+1
    elif s[count] in a:
      resultLower=resultLower+1
      
  return resultUpper,resultLower
  
resultUpper,resultLower=Upper_Lower(input())
print(resultUpper)
print(resultLower)
