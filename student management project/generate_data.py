import csv
import random

def generate_students():
    first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan",
                   "Shaurya", "Atharv", "Ananya", "Diya", "Sara", "Aadhya", "Saanvi", "Aditi", "Isha", "Riya",
                   "Neha", "Pooja", "Rahul", "Rohan", "Vikram", "Karan", "Ravi", "Suresh", "Ramesh", "Mahesh",
                   "Gita", "Sita", "Rita", "Kavita", "Sunita", "Anita", "Geeta", "Seeta", "Reeta", "Kaveeta",
                   "John", "David", "Michael", "Chris", "Paul", "Emma", "Olivia", "Sophia", "Isabella", "Mia"]
    
    last_names = ["Sharma", "Verma", "Gupta", "Malhotra", "Singh", "Kumar", "Das", "Bose", "Sen", "Yadav",
                  "Patel", "Shah", "Desai", "Mehta", "Bhat", "Iyer", "Nair", "Pillai", "Reddy", "Rao"]
    
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science"]
    
    students = []
    
    # Generate 50 unique students
    for i in range(1, 51):
        student_id = f"STU{i:03d}"
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 25)
        subject = random.choice(subjects)
        marks = random.randint(40, 100) # Assuming passing marks are 40 and total is 100
        
        students.append([student_id, name, age, subject, marks])
        
    return students

def main():
    students = generate_students()
    
    # Save to CSV
    filename = "students.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Subject", "Marks"])
        writer.writerows(students)
        
    print(f"Successfully generated {len(students)} students in {filename}")

if __name__ == "__main__":
    main()
