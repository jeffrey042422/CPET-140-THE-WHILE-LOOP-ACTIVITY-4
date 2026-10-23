#Jeffrey G BUCO
#BAET 2B 2102
#COUNTDOWN TIMER

n = int(input("Enter n: "))

while n <= 0:
    n = int(input("Enter n: "))

print("Enter n:", n)

while n > 0:
    print(n, end=" ")
    n -= 1

print("Liftoff!")