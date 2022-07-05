distance = int(input("Distance(km): "))
time = int(input("Time(h): "))
avg_speed = distance/time

if distance >= 1 and time >= 1:
    print("Average Speed: ", int(avg_speed), "km/h")

if distance < 1 or time < 1:
    print("Distance and Time must be greater than 1.")
    print("Try again")
