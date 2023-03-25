#######################################################################
# Do not erase this code
#matrix1, matrix2, matrix3 will be the inputs. Check one by one after writing the code for checking identity matrix
matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] 
matrix2 = [[1, 1, 0], [0, 1, 0], [0, 1, 1]] 
matrix3 = [[1, 0, 3], [0, 1, 2], [0, 0, 1]] 
#######################################################################
#Write your code below

if sum(matrix1[0])==1 and sum(matrix1[1]) and sum(matrix1[2]):
  print(True)
else:
  print(False)
  
if sum(matrix2[0])==1 and sum(matrix2[1]) and sum(matrix2[2]):
  print(True)
else:
  print(False)

if sum(matrix3[0])==1 and sum(matrix3[1]) and sum(matrix3[2]):
  print(True)
else:
  print(False)

