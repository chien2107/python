import random
patient_id = f"BN{random.randint(100, 999)}"
temperature = float(input("Nhiệt độ cơ thể: "))
heart_rate = int(input("Nhịp tim: "))
print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {patient_id}")
print(f"Nhiệt độ cơ thể: {temperature}")
print(f"Kiều dữ liệu hệ thống ghi nhận: {type(temperature)}")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f"Kiều dữ liệu hệ thống ghi nhận: {type(heart_rate)}")
print("----------------------------------------------------------------")
print("Thông báo: Dữ Liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")