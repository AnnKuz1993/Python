user_time = int(input("Укажите время в секундах >>> "))
hour = user_time // 3600
minute = (user_time // 60) % 60
second = user_time % 60
if minute < 10:
    minute = str('0' + str(minute))
else:
    minute = str(minute)
if second < 10:
    second = str('0' + str(second))
else:
    second = str(second)
print("Время в привычном формате составит >>> ",str(hour) + ':' + str(minute) + ':' + str(second))
