l,d=input().split(" ")
l=int(l)
d=int(d)
count=0
all=[]
while count<d:
  i=input()
  all.append(i)
  count=count+1
# print(all)

i1=input()
nn=0
all1=[]
while nn<len(i1):
  if i1[nn]=="(":
    nn=nn+1
    new=[]
    while i1[nn]!=")":
      new.append(i1[nn])
      if i1[nn]==")":
        break
      else:
        nn=nn+1
    all1.append(new)
  elif i1[nn]==")":
    nn=nn+1    
  else:
    new=[]
    new.append(i1[nn])
    all1.append(new)
    nn=nn+1
# print(all1)

# (as)(zx)(cv)
aa=0
count=0
count1=0
while aa<len(all):
  bb=0
  while bb<len(all[aa]):
    if all[aa][bb] in all1[bb]:
      count=count+1
      bb=bb+1
    else:
      count=count
      bb=bb+1
    
  if count==len(all[aa]):
    count1=count1+1
  else:
    count1=count1
  count=0
  aa=aa+1

print(count1)
# aa=0
# while aa<len(all1):
#   bb=0
#   while bb<len(all1[aa]):
#     bbb=0
#     while bbb<len(all):
#       if all1[aa][bb]==all[bbb][aa]:
#         bbb=bbb+1
#       else:
#         break


# # (as)(zx)(cv)
# # as(asd)




# l,d=input().split(" ")
# l=int(l)
# d=int(d)
# count=0
# set1=set([])
# while count<d:
#   i=input()
#   set1.add(i)
#   count=count+1
# i1=input()
# nn=0
# all=[]
# while nn<len(i1):
#   if i1[nn]=="(":
#     nn=nn+1
#     new=[]
#     while i1[nn]!=")":
#       new.append(i1[nn])
#       if i1[nn]==")":
#         break
#       else:
#         nn=nn+1
#     all.append(new)
#   elif i1[nn]==")":
#     nn=nn+1    
#   else:
#     new=[]
#     new.append(i1[nn])
#     all.append(new)
#     nn=nn+1

# #TEST ALL PASS CHANGE
# new1=[]
# var11=0
# var21=0
# var13=2
# var23=0
# var12=1
# var22=0
# # (as)(zx)(cv)
# # as(asd)
# while var21<len(all[var11]):
#   if var22>=len(all[var11]):
#     var21=var21+1
#   while var21<len(all[var11]):
#     new=[]
#     new.append(all[var11][var21])
#     # var12=1
#     if var22>=len(all[var11]):
#       var22=0
#     if var23>=len(all[var13]):
#       var22=var22+1
#     while var22<len(all[var12]):
#       new.append(all[var12][var22])
#       # var13=2
#       if var23>=len(all[var13]):
#         var23=0
#       while var23<len(all[var13]):
#         new.append(all[var13][var23])
#         var23=var23+1
#         new="".join(new)
#         new1.append(new)
#         # print(new)
#         break
#       break
#     break

# new1=set(new1)
# final=new1.intersection(set1)
# final=list(final)
# print(len(final))
