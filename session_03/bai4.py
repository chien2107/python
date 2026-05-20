print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
num_employees = 0
while num_employees <= 0:
    num_employees = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    if num_employees <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {num_employees} nhân sự mới!")
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")