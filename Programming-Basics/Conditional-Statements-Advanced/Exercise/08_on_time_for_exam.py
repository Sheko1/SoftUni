hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())

total_min_exam = (hour_exam * 60) + min_exam
total_min_arrive = (hour_arrive * 60) + min_arrive

if total_min_exam - 30 <= total_min_arrive <= total_min_exam:
    print("On time")
    if total_min_exam != total_min_arrive:
        diff = total_min_exam - total_min_arrive
        print(f"{diff} minutes before the start")


elif total_min_arrive > total_min_exam:
    time_late = total_min_arrive - total_min_exam
    print("Late")
    if time_late >= 60:
        hour = time_late // 60
        minn = time_late % 60
        if minn < 10:
            print(f"{hour}:0{minn} hours after the start")
        else:
            print(f"{hour}:{minn} hours after the start")
    else:
        print(f"{time_late} minutes after the start")

else:
    time_late = total_min_exam - total_min_arrive
    print("Early")
    if time_late >= 60:
        hour = time_late // 60
        minn = time_late % 60
        if minn < 10:
            print(f"{hour}:0{minn} hours before the start")
        else:
            print(f"{hour}:{minn} hours before the start")
    else:
        print(f"{time_late} minutes before the start")
