print("Tính chỉ số BMI")
cm = float(input("Nhập chiều cao của bạn:"))
cannang = float(input("Nhập cân nặng của bạn:"))


chieu_cao = cm/100
BMI = cannang/chieu_cao ** 2
if BMI < 16 :
    print("Suy dinh dưỡng nặng ")
elif 16 <=BMI<= 18.5 :
    print("Suy dinh dưỡng")
elif 18.5 <=BMI<= 25 :
    print("Bình thường")
elif 25 <=BMI<= 30:
    print("Lợn sữa")
else:
    print("Lợn lái")