import random

otp = random.randint(0000,9999)
print(otp)

enter_otp = int(input("Enter the OTP: "))

if enter_otp == otp:
    print("Login successful!")
else:
    print("Invalid OTP. Please try again.")