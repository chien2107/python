raw_data = " emp-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
while True:
    print("""
1. Hiển thị dữ liệu gốc
2. Hiển thị báo cáo
3. Tìm kiếm nhân viên
4. Thoát
""")
    try:
        choice = int(input("Nhập lựa chọn: "))
        if choice == 1:
            print(raw_data)
        elif choice == 2:
            print(f"\n{'ID':<10}{'HỌ TÊN':<20}{'PHÒNG':<15}{'SĐT'}")
            print("-" * 60)
            data = raw_data.replace("|", ";").strip()
            employees = [emp.strip() for emp in data.split(";") if emp.strip()]
            i = 0
            while i < len(employees):
                if i + 3 < len(employees):
                    emp_id = employees[i].strip()
                    name = employees[i+1].strip()
                    phone = employees[i+2].strip()
                    department = employees[i+3].strip()
                    emp_id = emp_id.upper()
                    name = name.title()
                    department = department.upper()
                    phone_clean = phone.replace("-", "").replace(" ", "")
                    if phone_clean.isdigit():
                        phone = "******" + phone_clean[-4:]
                    else:
                        phone = "Invalid Format"
                    print(f"{emp_id:<10}{name:<20}{department:<15}{phone}")
                    i += 4
                else:
                    break
        elif choice == 3:
            search_id = input("Nhập mã nhân viên: ").strip().upper()
            found = False
            data = raw_data.replace("|", ";").strip()
            employees = [emp.strip() for emp in data.split(";") if emp.strip()]
            i = 0
            while i < len(employees):
                if i + 3 < len(employees):
                    emp_id = employees[i].strip().upper()
                    if emp_id == search_id:
                        name = employees[i+1].strip().title()
                        phone = employees[i+2].strip()
                        department = employees[i+3].strip().upper()
                        phone_clean = phone.replace("-", "").replace(" ", "")
                        if phone_clean.isdigit():
                            phone_display = "******" + phone_clean[-4:]
                        else:
                            phone_display = "Invalid Format"
                        print("\n--- THÔNG TIN NHÂN VIÊN ---")
                        print("ID:", emp_id)
                        print("Tên:", name)
                        print("Phòng:", department)
                        print("SĐT:", phone_display)
                        found = True
                        break
                    i += 4
                else:
                    break
            if not found:
                print("Không tìm thấy nhân viên")
        elif choice == 4:
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ!")
    except:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")