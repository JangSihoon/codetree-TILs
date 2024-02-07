for i in range(1, 20):
    for j in range(1, 20):
        print(f"{i} * {j} = {i * j}", end=" ")
        if j % 2 == 0:
            print(f"/ {i} * {j + 1} = {i * (j + 1)}", end=" ")
    print()