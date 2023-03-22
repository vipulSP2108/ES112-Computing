q,w,e= input().split("/")
q=int(q)
e=int(e)
k=int(w)
# if q>31 or k>12:
#   print("Invalid Format")

## only to add this 2 lines,
if k<=00 or q<=00:
  print("Invalid Format")

if k>12:
  print("Invalid Format")
elif w=="01" and q> 31:
  print("Invalid Format")
# elif w=="02" and q> 29:
#   print("Invalid Format")
elif w=="03" and q> 31:
  print("Invalid Format")
elif w=="04" and q> 30:
  print("Invalid Format")
elif w=="05" and q> 31:
  print("Invalid Format")
elif w=="06" and q> 30:
  print("Invalid Format")
elif w=="07" and q> 31:
  print("Invalid Format")
elif w=="08" and q> 31:
  print("Invalid Format")
elif w=="09" and q> 30:
  print("Invalid Format")
elif w=="10" and q> 31:
  print("Invalid Format") 
elif w=="11" and q> 30:
  print("Invalid Format")
elif w=="12" and q> 31:
  print("Invalid Format")
else:
  y=0
  count=0
  while y< e:
    if(y<=0):
      count=count
    elif(y%4==0):
      if y%100==0 and y%400==0:
        count=count+1
      elif y%400!=0 and y%100==0:
        count=count
      else:     
        count=count+1
    else:
      count=count
    y=y+1
  
  if(y<=0):
    i=28
  elif(y%4==0):
    if y%100==0 and y%400==0:
      i=29
    elif y%400!=0 and y%100==0:
      i=28
    else:     
      i=29
  else:
    i=28
  if w=="02" and q> i:
    print("Invalid Format")
  else:
    while q <= 365 :
      if w=="01":
        break
      q=q+31
      if w=="02":
        break
      q=q+i
      if w=="03":
        break
      q=q+31
      if w=="04":
        break
      q=q+30
      if w=="05":
        break
      q=q+31
      if w=="06":
        break
      q=q+30
      if w=="07":
        break
      q=q+31
      if w=="08":
        break
      q=q+31
      if w=="09":
        break
      q=q+30
      if w=="10":
        break
      q=q+31
      if w=="11":
        break
      q=q+30
      if w=="12":
        break
      q=q+31
      
    q=q+(e-1)*365 + count
    
    if q%7==1:
      print("Monday")
    if q%7==2:
      print("Tuesday")
    if q%7==3:
      print("Wednesday")
    if q%7==4:
      print("Thrusday")
    if q%7==5:
      print("Friday")
    if q%7==6:
      print("Saturday")
    if q%7==0:
      print("Sunday")

#for one year

# q,w,e= input().split("/")
# q=int(q)
# sun=1
# mon=2
# tue=3
# wed=4
# thus=5
# fri=6
# sat=7
# while q <= 365 :
#   if w=="01":
#     break
#   q=q+31
#   if w=="02":
#     break
#   q=q+28
#   if w=="03":
#     break
#   q=q+31
#   if w=="04":
#     break
#   q=q+30
#   if w=="05":
#     break
#   q=q+31
#   if w=="06":
#     break
#   q=q+30
#   if w=="07":
#     break
#   q=q+31
#   if w=="08":
#     break
#   q=q+31
#   if w=="09":
#     break
#   q=q+30
#   if w=="10":
#     break
#   q=q+31
#   if w=="11":
#     break
#   q=q+30
#   if w=="12":
#     break
#   q=q+31
  
# while True:
#   if q==sun:
#     print("Sunday")
#     break
#   sun=sun+7
#   if q==mon:
#     print("Monday")
#     break
#   mon=mon+7
#   if q==tue:
#     print("Tuesday")
#     break
#   tue=tue+7
#   if q==wed:
#     print("Wednesday")
#     break
#   wed=wed+7
#   if q==thus:
#     print("Thusday")
#     break
#   thus=thus+7
#   if q==fri: 
#     print("Friday")
#     break
#   fri=fri+7
#   if q==sat:
#     print("Saterday")
#     break
#   sat=sat+7  

#for one year

# q,w,e= input().split("/")
# q=int(q)
# if w=="01":
#   sun=1
#   mon=2
#   tue=3
#   wed=4
#   thus=5
#   fri=6
#   sat=7
#   while sun<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="02":
#   sun=5
#   mon=6
#   tue=7
#   wed=1
#   thus=2
#   fri=3
#   sat=4
#   while wed<28:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="03":
#   sun=5
#   mon=6
#   tue=7
#   wed=1
#   thus=2
#   fri=3
#   sat=4
#   while wed<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="04":
#   sun=2
#   mon=3
#   tue=4
#   wed=5
#   thus=6
#   fri=7
#   sat=1
#   while sat<30:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="05":
#   sun=7
#   mon=1
#   tue=2
#   wed=3
#   thus=4
#   fri=5
#   sat=6
#   while mon<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="06":
#   sun=4
#   mon=5
#   tue=6
#   wed=7
#   thus=1
#   fri=2
#   sat=3
#   while thus<30:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="07":
#   sun=2
#   mon=3
#   tue=4
#   wed=5
#   thus=6
#   fri=7
#   sat=1
#   while sat<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="08":
#   sun=6
#   mon=7
#   tue=1
#   wed=2
#   thus=3
#   fri=4
#   sat=5
#   while tue<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="09":
#   sun=3
#   mon=4
#   tue=5
#   wed=6
#   thus=7
#   fri=1
#   sat=2
#   while fri<30:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="10":
#   sun=1
#   mon=2
#   tue=3
#   wed=4
#   thus=5
#   fri=6
#   sat=7
#   while sun<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
# elif w=="11":
#   sun=5
#   mon=6
#   tue=7
#   wed=1
#   thus=2
#   fri=3
#   sat=4
#   while wed<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
#   sun=1
#   mon=2
#   tue=3
#   wed=4
#   thus=5
#   fri=6
#   sat=7
#   while sun<31:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#       tue=tue+7
#     if q==wed:
#       print("Wednesday")
#       wed=wed+7
#   if q==thus:
#       print("Thusday")
#       thus=thus+7
#   if q==fri: 
#       print("Friday")
#       fri=fri+7
#   if q==sat:
#       print("Saterday")
#       sat=sat+7 
# elif w=="12":
#   sun=3
#   mon=4
#   tue=5
#   wed=6
#   thus=7
#   fri=1
#   sat=2
#   while fri<30:
#     if q==sun:
#       print("Sunday")
#     sun=sun+7
#     if q==mon:
#       print("Monday")
#     mon=mon+7
#     if q==tue:
#       print("Tuesday")
#     tue=tue+7
#     if q==wed:
#       print("Wednesday")
#     wed=wed+7
#     if q==thus:
#       print("Thusday")
#     thus=thus+7
#     if q==fri: 
#       print("Friday")
#     fri=fri+7
#     if q==sat:
#       print("Saterday")
#     sat=sat+7 
