import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    def cnv_to_24h(hour,period):
        if period ==  "PM" and hour != "12":
            hour = int(hour) + 12
            
        elif period ==  "AM" and hour == "12":
            hour = 0
        return int(hour)

    
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern,s)
    
    if match:
        start_hour = match.group(1)
        start_minutes = match.group(2)
        start_period = match.group(3)

        end_hour = match.group(4)
        end_minutes = match.group(5)
        end_period = match.group(6)

        if start_minutes == None:
            start_minutes = "00"
        if end_minutes == None:
            end_minutes = "00"  

        cnv_start_hour =  cnv_to_24h(start_hour,start_period)
        cnv_end_hour = cnv_to_24h(end_hour, end_period)

        return f"{cnv_start_hour:02}:{start_minutes} to {cnv_end_hour:02}:{end_minutes}"
    
    else:
        raise ValueError


if __name__ == "__main__":
    main()