choice = 0
raw_input = '   nGuyen vaN aN  ;  2004   '
while 1:
    choice = int(input("""
===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
1. Hiển thị chuổi dữ liệu gốc
2. Chuẩn hóa họ tên và tính tuổi
3. Tạo mã ID và Email tự động
4. THoát chương trình
====================================
Nhập lựa chọn của bạn (1-4): """))
    match choice:
        case 1:
            print(f"""
Chuỗi dữ liệu gốc hiện tại:
'{raw_input}'
""")
        case 2:
            age = 2026 - int((raw_input.strip().split(";")[1]).strip())
            new_name = raw_input.strip().split(";")[0].strip().lower().title()
            print(f"""
[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:
- Họ và tên: {new_name}
- Tuổi hiện tại: {age} tuổi 
""")
        case 3:
            ID = raw_input.strip().split(";")[0].strip().split(" ")[2].upper() + (raw_input.strip().split(";")[1]).strip()[2:4]
            new_name = raw_input.strip().split(";")[0].strip().lower().title()
            email = raw_input.strip().split(";")[0].strip().split(" ")[0][0] + raw_input.strip().split(";")[0].strip().split(" ")[1][0] + raw_input.strip().split(";")[0].strip().split(" ")[2][0] + "@company.com"
            print(f"""
=======================================
            THẺ THÀNH VIÊN 
=======================================
Họ và tên   : {new_name}
Mã ID       : {ID}
Email       : {email}
=======================================
""")
        case 4:
            print("Chương trình đã dừng!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")