age = int(input("Nhập tuổi: "))
bp = int(input("Nhập huyết áp tâm thu: "))
sugar = int(input("Nhập đường huyết: "))
if age < 0 or bp < 0 or sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
else:
    if age >= 75:
        print("TỪ CHỐI PHẪU THUẬT: Tuổi phải dưới 75")
    else:
        if bp < 90 or bp > 140:
            print("TỪ CHỐI PHẪU THUẬT: Huyết áp phải từ 90-140 mmHg")
        else:
            if sugar >= 150:
                print("TỪ CHỐI PHẪU THUẬT: Đường huyết phải dưới 150 mg/dL")
            else:
                print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")