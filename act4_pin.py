#Jeffrey G BUCO
#BAET 2B 2102
#PIN LOCK

correct_pin = "1234"
for attempt in range(3):
    pin = input("PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    if attempt == 2:
        print("Card blocked")