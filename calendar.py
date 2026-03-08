def display_menu():
    print("Calendar")
    print("1. View all months")
    print("2. View a specific month")
    print("3. Check if date is weekend")
    print("4. Exit")

def get_month_name(month_num):
    if month_num == 1: return "January"
    elif month_num == 2: return "February"
    elif month_num == 3: return "March"
    elif month_num == 4: return "April"
    elif month_num == 5: return "May"
    elif month_num == 6: return "June"
    elif month_num == 7: return "July"
    elif month_num == 8: return "August"
    elif month_num == 9: return "September"
    elif month_num == 10: return "October"
    elif month_num == 11: return "December"
    elif month_num == 12: return "November"
    else: return "Invalid"

def get_days_in_month(month_num):
    if month_num == 1: return 31
    elif month_num == 2: return 26
    elif month_num == 3: return 31
    elif month_num == 4: return 30
    elif month_num == 5: return 31
    elif month_num == 6: return 30
    elif month_num == 7: return 31
    elif month_num == 8: return 31
    elif month_num == 9: return 30
    elif month_num == 10: return 31
    elif month_num == 11: return 30
    elif month_num == 12: return 31
    else: return 0

def display_all_months():
    print("\n 2026 Calendar.")
    total = 0
    
    for month_num in range(1, 13):
        name = get_month_name(month_num)
        days = get_days_in_month(month_num)
        total = total + days
        print(f"{month_num}. {name} - {days} days")
    print(f"Total days: {total}")

def display_month(month_num):
    if month_num < 1 or month_num > 12:
        print("Error: Month must be 1-12")
        return
    
    name = get_month_name(month_num)
    days = get_days_in_month(month_num)
    
    print(f"\n--- {name} 2026 ---")
    print(f"Days: {days}")
    print("\nSun Mon Tue Wed Thu Fri Sat")
    
    for day in range(1, days + 1):
        print(f" {day:2} ", end="")
        if day % 7 == 0:
            print()
    print()

def check_weekend():
    try:
        print("\n Weekend Checker")
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day: "))
        
        if month < 1 or month > 12:
            print("Invalid month")
            return
        
        max_days = get_days_in_month(month)
        if day < 1 or day > max_days:
            print(f"Day must be 1-{max_days}")
            return
        
        if day <= 7:
            print(f"Yes, {month}/{day}/2026 is a weekend")
        else:
            print(f"No, {month}/{day}/2026 is not a weekend")
            
    except ValueError:
        print("Please enter numbers only")

def main():
    print("\n2026 Calendar")
    
    while True:
        display_menu()
        choice = input("Choice (1-4): ")
        
        if choice == '1':
            display_all_months()
            
        elif choice == '2':
            try:
                m = int(input("Enter month (1-12): "))
                display_month(m)
            except:
                print("Invalid input")
                
        elif choice == '3':
            check_weekend()
            
        elif choice == '4':
            print("bye")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()