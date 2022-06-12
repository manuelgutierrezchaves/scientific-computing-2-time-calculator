from time_calculator import add_time


print(add_time("3:30 PM", "2:12")) # Expected "5:42 PM"

print(add_time("11:55 AM", "3:12")) # Expected "3:07 PM"

print(add_time("9:15 PM", "5:30")) # Expected "2:45 AM (next day)"

print(add_time("11:40 AM", "0:25")) # Expected = "12:05 PM"

print(add_time("2:59 AM", "24:00")) # Expected = "2:59 AM (next day)"

print(add_time("11:59 PM", "24:05")) # Expected = "12:04 AM (2 days later)"

print(add_time("8:16 PM", "466:02")) # Expected = "6:18 AM (20 days later)"

print(add_time("5:01 AM", "0:00")) # Expected = "5:01 AM"

print(add_time("3:30 PM", "2:12", "Monday")) # Expected = "5:42 PM, Monday"

print(add_time("2:59 AM", "24:00", "saturDay")) # Expected = "2:59 AM, Sunday (next day)"
    
print(add_time("11:59 PM", "24:05", "Wednesday")) # Expected = "12:04 AM, Friday (2 days later)"

print(add_time("8:16 PM", "466:02", "tuesday")) # Expected = "6:18 AM, Monday (20 days later)"
    