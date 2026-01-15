from soil import sample

def main():
    
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisture: {moisture}%")

    while moisture > 20:

        moisture = sample()
        days += 1 
        print(f"Day {days}: Moisture: {moisture}%")
    
    print("Time to water!")

main()