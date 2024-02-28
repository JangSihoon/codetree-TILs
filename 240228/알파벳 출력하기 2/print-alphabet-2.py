# ?? -> 이게뭐지? -> 나 뭘해야되지? -> 대답 -> 나 뭘한거지? -> 대답
n = int(input())
cnt = 64
for i in range(1,n+1):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(n-i+1):
        cnt += 1
        if chr(cnt)==83:
            cnt==64
        print(chr(cnt),end = " ")
    print()


#