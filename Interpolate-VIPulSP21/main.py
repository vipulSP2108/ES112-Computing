def yourCodeHere(ip):
  #write you code in this function only
  
  ip=list(ip)
  for q in range(len(ip)):
    if ip[q]== -1 :
      c=(ip[q+1]+ip[q-1])//2
      ip[q]=c
  ip=tuple(ip)
  return ip
  pass

# don't edit the code below this line
n = int(input())
temp = []
while n>0:
  temp.append(int(input()))
  n -= 1
temp = tuple(temp)
assert isinstance(yourCodeHere(temp), tuple) == True
print(yourCodeHere(temp))
