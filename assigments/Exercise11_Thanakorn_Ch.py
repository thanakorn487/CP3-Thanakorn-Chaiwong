N = int(input("Input rows : "))
for i in range(N):
    print(" " * (N-(i+1)), "*" * ((i + 1) + i), " " * (N-(i+1)))