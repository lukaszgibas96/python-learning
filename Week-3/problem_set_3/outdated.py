#Problem Set 3 - Outdated

# MM/DD/YYYY

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():

    while True:
        try:
            month, day, year = input("Date: ").split(" ")
            day = int(day.removesuffix(","))

            if month in months and day <= 31:
                month = int(months.index(month)) + 1 
                convert(year,month,day)
                break

        except ValueError:
            month, day, year = input("Date: ").split("/")
            day = int(day)
            month = int(month)
            if day <= 31 and 1 <= month <= 12:
                convert(year,month,day)
                break


def convert(yyyy, mm, dd):
    
    print(f"{yyyy}-{mm:02}-{dd:02}")



main()
