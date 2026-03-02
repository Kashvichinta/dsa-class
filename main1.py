#attendence Tracking System

#Dictionary to store attendance
attendance={}
def show_menu():
    print("Attendance Tracker")
    print("1.Add Attendance")
    print("2. View Attendance")
    print("3. Exit")
def add_attendance():
    name=input("Enter Student Name:")
    status=input("Enter status (Present/Absent):")
    attendance[name]=status
    print("Attendance Added Successfully")            
def view_attendance():
    if not attendance:
        print("No attendance records found")    
    else:
        print("-----attendance records------")  
        for name,status in attendance.items():
            print(f"{name}-{status}")
def main():
    while True:
        show_menu()
        choice=input("Enter your choice:")
        if choice=="1":
            add_attendance()
        elif choice =="2":
            view_attendance()
        elif choice=="3":
            print("Exiting program")
            break
        else:
            print("invalid choice")
main()                                    