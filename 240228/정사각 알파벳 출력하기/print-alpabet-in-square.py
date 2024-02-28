n = int(input())
cnt = 64
for i in range(n):
    for j in range(n):
        cnt += 1
        if chr(cnt)==90:
            cnt==64
        print(chr(cnt),end = "")
    print()