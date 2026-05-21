branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
for month in range(1, month_count + 1):
    print(f"\n--- THÁNG {month} ---")
    for branch in range(1, branch_count + 1):
        revenue = int(input(f"Nhập doanh thu chi nhánh {branch}, tháng {month}: "))
        while revenue < 0:
            print("Doanh thu không hợp lệ!")
            revenue = int(input(f"Nhập lại doanh thu chi nhánh {branch}, tháng {month}: "))
        print(f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng")