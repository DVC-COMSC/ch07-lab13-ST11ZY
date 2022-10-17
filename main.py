numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

rnum = len(numbers)
cnum = len(numbers[0])
crosscount=0;
for i in range(rnum):
    for j in range(cnum):
        if i>0 and j>0 and i<rnum-1 and j<cnum-1:
            if numbers[i][j]==1 and numbers[i-1][j]==1 and numbers[i+1][j]==1 and numbers[i][j+1]==1 and numbers[i][j-1]==1:
                crosscount+=1;
    
print(crosscount)
# ******************************
# Make your Code
