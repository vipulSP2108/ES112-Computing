f, s, t = input().split()

i=1
new_f=""
while i <= len(f):
  new_f=new_f+(f[len(f)-i])
  i=i+1

i=1
new_s=""
while i <= len(s):
  new_s=new_s+(s[len(s)-i])
  i=i+1

i=1
new_t=""
while i <= len(t):
  new_t=new_t+(t[len(t)-i])
  i=i+1

if (new_f==f):
  print(new_f)
if(new_s==s):
  print(new_s)
if(new_t==t):
  print(new_t)
if new_f!=f and new_s!=s and new_t!=t :
  print("No palindrome")

#method 2

# a,s,t=input().split()

# no_a=len(a)
# var1=0
# new_a=""
# while no_a >0 and 0 <no_a:
#    z=a[no_a-1:no_a]
#    x=a[var1:var1+1]
#    if z==x :
#      new_a=new_a+z
#      no_a=no_a-1
#      var1=var1+1
#    else :
#      no_a=no_a-1
#      var1=var1+1

# no_s=len(s) 
# var2=0
# new_s=""
# while no_s >0 and 0 <no_s:
#    k=s[no_s-1:no_s]
#    l=s[var2:var2+1]
#    if k==l :
#      new_s=new_s+l
#      no_s=no_s-1
#      var2=var2+1
#    else :
#      no_s=no_s-1
#      var2=var2+1

# no_t=len(t)
# var3=0
# new_t=""
# while no_t >0 and 0 <no_t:
#    z=t[no_t-1:no_t]
#    x=t[var3:var3+1]
#    if z==x :
#      new_t=new_t+x
#      no_t=no_t-1
#      var3=var3+1
#    else :
#      no_t=no_t-1
#      var3=var3+1

# if (new_a==a):
#   print(new_a)
# if(new_s==s):
#   print(new_s)
# if(new_t==t):
#   print(new_t)
# if new_a!=a and new_s!=s and new_t!=t :
#   print("No palindrome")

#string slicing

# if (new_a==a):
#   print(new_a)
# if(new_s==s):
#   print(new_s)
# if(new_t==t):
#   print(new_t)
# if new_a!=a and new_s!=s and new_t!=t :
#   print("No palindrome")

# w1,w2,w3=str(input()).split()
# w11=w1[::-1]
# w22=w2[::-1]
# w33=w3[::-1]
# if(w1==w11):
#   print(w1)
# if(w2==w22):
#   print(w2)
# if(w3==w33):
#   print(w3)
# elif(w1!=w11 and w2!=w22 and w3!=w33):
#   print("No palindrome")
