# ?? -> 이게뭐지? -> 나 뭘해야되지? -> 대답 -> 나 뭘한거지? -> 대답
n = int(input())
alpha_idx = ord("A")-1
for i in range(1,n+1):
    for j in range(i):
        alpha_idx += 1
        if alpha_idx > ord("Z"):
            alpha_idx = ord("A")
        print(chr(alpha_idx),end = "")
    print()


# 이건 abc 순서대로 나열하여 삼각형을 만드는 것이다.
# 난 삼각형을 만들고 abc순서대로 채워넣어야한다.
# 난 삼각형을 만들고 abc순서대로 채워넣었다.