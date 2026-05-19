name = input("Mời bạn nhập họ và tên : ")
age = int(input("Mời bạn nhập tuổi : "))
if name == " " or age < 0 or age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    exit()
if age < 6:
    result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám nhi"
elif age >= 80:
    result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám lão khoa"
else:
    result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh"
print("--- PHIẾU KHÁM BỆNH ---")
print("Tên :", name)
print("Tuổi :", age)
print("Kết quả phân luồng :", result)
