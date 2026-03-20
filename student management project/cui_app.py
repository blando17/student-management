import sys
from core_logic import load_data, add_student, delete_student, search_student, analyze_data

def display_menu():
    print("\n--- Student Management System (CUI) ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Analyze Data")
    print("5. Exit")
    return input("Select an option (1-5): ")

def main():
    students = load_data()
    print(f"Loaded {len(students)} students from CSV.")
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            sid = input("Enter Student ID (e.g., STU051): ")
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
                marks = int(input("Enter Marks: "))
            except ValueError:
                print("Invalid input for Age or Marks. Must be integers.")
                continue
            subject = input("Enter Subject: ")
            
            success, msg = add_student(students, sid, name, age, subject, marks)
            print("---")
            print(msg)
            
        elif choice == '2':
            sid = input("Enter Student ID to delete: ")
            success, msg = delete_student(students, sid)
            print("---")
            print(msg)
            
        elif choice == '3':
            query = input("Enter Student ID or Name to search: ")
            results = search_student(students, query)
            print("---")
            if not results:
                print("No student found.")
            else:
                print(f"Found {len(results)} matching record(s):")
                for sid, details in results:
                    print(f"ID: {sid} | Name: {details['Name']} | Age: {details['Age']} | Subject: {details['Subject']} | Marks: {details['Marks']}")
                    
        elif choice == '4':
            results = analyze_data(students)
            print("---")
            if not results:
                print("No data available to analyze.")
            else:
                min_marks, max_marks, avg_marks, subjects = results
                print("--- Data Analysis ---")
                print(f"Total Students: {len(students)}")
                print(f"Minimum Marks: {min_marks}")
                print(f"Maximum Marks: {max_marks}")
                print(f"Average Marks: {avg_marks:.2f}")
                print(f"Unique Subjects Enrolled: {', '.join(subjects)}")
                
        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
