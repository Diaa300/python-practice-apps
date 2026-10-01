import time

orignal_num = float(input("Enter a number: "))
num = round(orignal_num)

if orignal_num != int(orignal_num):

    print(f'Rounded Number: {num}')

    time.sleep(1.5)

if num % 5 == 0:

    print(f"The number {num} is a multiple of 5")

if num % 2 == 0:

    print(f"The number {num} is a Even")

else:

    print(f"The number {num} is a Odd")
