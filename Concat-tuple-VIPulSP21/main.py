def yourCodeHere(tuple1, tuple2):
  #write you code in this function only
  tuple1=list(tuple1)
  tuple2=list(tuple2)
  tupleadd=tuple1+tuple2
  tupleadd=tuple(tupleadd)
  return tupleadd
  pass
# don't edit the code below this line
tuple1 = tuple(input().split())
tuple2 = tuple(input().split())
assert isinstance(yourCodeHere(tuple1, tuple2), tuple) == True
print(yourCodeHere(tuple1, tuple2))
  
