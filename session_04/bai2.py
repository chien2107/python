total = 0
count = 0
for i in range(1, 8):
    revenue = int(input(f"Nhập doanh thu Ngày {i}: "))
    total += revenue
    if revenue >= 5000000:
        count += 1
average = total / 7
print("---- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ----")
print(f"Tổng doanh thu cả tuần: {total} VND")
print(f"Doanh thu trung bình mỗi ngày: {int(average)} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): {count} ngày")