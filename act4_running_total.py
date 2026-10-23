#Jeffrey G BUCO
#BAET 2B 2102
#RUNNING TOTAL

count = 0
total = 0
while True:
    price = float(input("Price (0 to stop): "))
    if price == 0:
        break
    total += price
    count += 1
if count > 0:
    average = total / count
    print(f"Items: {count} Total: {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No items.")
