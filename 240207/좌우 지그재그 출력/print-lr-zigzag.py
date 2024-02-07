n = int(input())
cnt = 0
for i in range(1,n+1):
    if i%2==1:
        if i!=1:
            cnt+=n
        for j in range(1,n+1):
            
            cnt+=1    
            print(cnt,end = " ")

    else:
        cnt+=n
        for k in range(1,n+1):
            print(cnt,end = " ")
            cnt-=1
    print()