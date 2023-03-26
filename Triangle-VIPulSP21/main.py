def IsTriangle(side_1, side_2, side_3):
  result="True"
  if side_1+side_2>side_3 and side_2+side_3>side_1 and side_3+side_1>side_2 :
    return result
  else:
    return not result
  
  pass


a, b, c = map(int, input().split())
result = IsTriangle(a, b, c)
print(result)
