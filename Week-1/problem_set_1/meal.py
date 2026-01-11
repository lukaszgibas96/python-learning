# Problem Set 1 - 

def main():
    user_time = input("What time is it? ").strip().lower()

    float_time = convert(user_time)

    if 7.0 <= float_time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("Lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("Dinner time") 

def convert(time):
    
    if "a.m" in time or "p.m" in time:
        hours_minutes, am_pm = time.split(" ")
        hours, minutes = hours_minutes.split(":")
        hours = float(hours)
        minutes = float(minutes)
        minutes = minutes / 60

        if am_pm == "p.m":
             hours = hours + 12.0

        return hours + minutes

    else:

        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        minutes = minutes/60

        return hours + minutes
    
if __name__ == "__main__":

    main()