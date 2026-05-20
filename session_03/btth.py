choice = 'y'
while choice == 'y':
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"Nhân viên thứ {i+1}:")
        name = input("Nhập tên nhân viên: ")
        days = int(input("Nhập số ngày đi làm: "))
        print("Thông tin nhân viên")
        print("Tên:", name)
        print("Số ngày đi làm:", days)
        if days < 20:
            print("Cần cải thiện chuyên cần\n")
        else:
            print("Nhân viên chuyên cần tốt")
    choice = input("Tiếp tục chương trình? (y/n):")
print("Chương trình kết thúc")