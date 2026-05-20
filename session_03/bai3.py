print("--- HỆ THỐNG QUẢN LÝ HỒ SƠ NHÂN VIÊN ---")
for i in range(1, 4):
    print(f"\n--- Nhập thông tin nhân viên {i} ---")
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")
    if (employee_id == " " or employee_id.isspace() or full_name == " " or full_name.isspace()):
        print("LỖI: Mã nhân viên hoặc Họ tên không hợp lệ (bị bỏ trống hoặc chỉ chứa khoảng trắng).")
    else:
        print("\n--- PHIẾU HỒ SƠ NHÂN VIÊN ---")
        print("Mã nhân viên :", employee_id)
        print("Họ và tên    :", full_name)
        print("Phòng ban    :", department)
print("\nĐã hoàn tất nhập hồ sơ cho 3 nhân viên!")