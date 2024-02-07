def even(i,j):
    print(f"{i} * {j} = {i*j}",end = "\n")
def odd(i,j):
    if j==19:
        print(f"{i} * {j} = {i*j}",end = " ")
    else:
        print(f"{i} * {j} = {i*j}",end = " / ")

for i in range(1, 20):
    for j in range(1, 20):
        if j%2==0:
            even(i,j)
        else:
            odd(i,j)
    print()

# 1,1   1,2     1,3     1,4     1,5     
# 1,6   1,7     1,8     1,9     1,10
# 1,19