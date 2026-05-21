n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    print()
    name = input("Nhập tên nhân viên: ")
    days = int(input("Nhập số ngày làm: "))
    if days < 0 or days > 22:
        print("Dữ liệu không hợp lệ")
        continue
    if days == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue
    print(name + ": ", end="")
    for j in range(days):
        print("*", end="")
    print()
    if days >= 18:
        print("Làm việc chăm chỉ")
    elif days < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")