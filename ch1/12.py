a, b, c = map(int, input().split())
2 <= a, b, c <= 10000
print(f"{(a+b) % c}\n{((a % c)+(b % c))%c}\n{(a*b) % c}\n{((a % c)*(b % c)) % c}")
