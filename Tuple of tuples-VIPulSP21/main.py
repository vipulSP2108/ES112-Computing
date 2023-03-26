# Take input from the user, create the tuple x of ints
x=tuple(map(int,input().split()))
y=[]

# Create the new 'tuple of tuples' y from x as instructed
def func1(q):
  global y
  listx=list(x)
  def func2():
    nonlocal listx
    listx.remove(listx[q])
  func2()
  y.append(tuple(listx))
for i in range(len(x)):
  func1(i)

# Print the tuple y
y=tuple(y)
print(y)

### Do NOT change the code below this line! ###
exec('assert isinstance(x, tuple) == True')
exec('assert isinstance(y, tuple) == True')
