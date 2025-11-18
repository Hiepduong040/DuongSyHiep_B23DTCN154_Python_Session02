number = int(input("nhap mot so nguyen"))

if (number % 3 == 0  ) and (number  % 5 == 0  ):
    print("ban vua nhap so chia het cho 3 va 5")
elif number  % 3 == 0:
    print("ban vua nhap so chia het cho 3")
else :
    print("ban vua nhap so chia het cho 5")