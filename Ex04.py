number = int(input("nhap vao so nguyen duong"))
count = 0
if number > 0:
    for i in range(1,number+1):
        count += i
    print(f"tong cac so tu 0 den {number} la: {count}")
else: 
    print("so vua nhap khong phai so nguyen duong")



