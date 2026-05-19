from datetime import datetime
name = input("Mời bạn nhập tên bệnh nhân : ")
year_of_birth = int(input("Mời bạn nhập năm sinh : "))
day = int(input("Mời bạn nhập số ngày bị bệnh : "))
body_temperature = float(input("Mời bạn nhập nhiệt độ cơ thể : "))
cost = float(input("Mời bạn nhập chi phí khám : "))
if name == " ":
    print("Tên không được để trống")
    exit()
if 1900 < year_of_birth and year_of_birth > datetime.now().year:
    print("Năm sinh không hợp lệ")
    exit()
if day < 0:
    print("Số ngày không hợp lệ")
    exit()
if cost <= 0:
    print("Chi phí khám phải lớn hơn 0")
    exit()
age = datetime.now().year - year_of_birth
surcharge = cost * 0.1
total_cost = cost + surcharge
if body_temperature > 38 and day > 3:
    status = "Nguy hiểm"
elif body_temperature > 38:
    status = "Sốt cao"
elif body_temperature > 37.5:
    status = "Sốt nhẹ"
else:
    status = "Bình thường"
if status == "Nguy hiểm":
    if age > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
else:
    priority = "Bình thường"
cost_level = "Cao" if total_cost > 500000 else "Thấp"
print("--- KẾT QUẢ ---")
print("Tên :", name)
print("Tuổi :", age)
print("Nhiệt độ :", body_temperature)
print("Số ngày bệnh :" , day)
print("Tình trạng :", status)
print("Mức độ ưu tiên :", priority)
print("Tổng chi phí :", total_cost)
print("Mức chi phí :", cost_level)
