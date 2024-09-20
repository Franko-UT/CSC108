def convert_time(hour_24: int) -> int:
    if hour_24 != 0:
        hour_12 = int ( ( hour_24 - 1 ) % 12 + 1 )
    elif  hour_24 == 0:
        hour_12 = 12
    return hour_12

print(convert_time(0)) 
