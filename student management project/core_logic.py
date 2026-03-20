import csv
import os

CSV_FILE = 'students.csv'

def load_data():
    """Load data from CSV to a Dictionary of Dictionaries."""
    students = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Key: ID, Value: Dict of details
                students[row['ID']] = {
                    'Name': row['Name'],
                    'Age': int(row['Age']),
                    'Subject': row['Subject'],
                    'Marks': int(row['Marks'])
                }
    return students

def save_data(students):
    """Save data from Dictionary to CSV using a List for rows."""
    # List is used to prepare rows
    rows = []
    for sid, details in students.items():
        rows.append({
            'ID': sid,
            'Name': details['Name'],
            'Age': details['Age'],
            'Subject': details['Subject'],
            'Marks': details['Marks']
        })
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Age', 'Subject', 'Marks'])
        writer.writeheader()
        writer.writerows(rows)

def add_student(students, sid, name, age, subject, marks):
    """Add a new student using Dictionary."""
    if sid in students:
        return False, "Student ID already exists."
    students[sid] = {'Name': name, 'Age': age, 'Subject': subject, 'Marks': marks}
    save_data(students)
    return True, "Student added successfully."

def delete_student(students, sid):
    """Delete a student from Dictionary."""
    if sid in students:
        del students[sid]
        save_data(students)
        return True, "Student deleted successfully."
    return False, "Student ID not found."

def search_student(students, query):
    """Search for a student using Dictionary keys or Iteration for names. Returns a List."""
    # List is used to return multiple matches if searching by name
    results = []
    query_lower = query.lower()
    
    if query in students: # O(1) Dictionary Lookup
        results.append((query, students[query]))
        
    for sid, details in students.items():
        if query_lower in details['Name'].lower() and sid != query:
            results.append((sid, details))
            
    return results

def analyze_data(students):
    """Analyze data using Set and Tuple."""
    if not students:
        return None
        
    total_marks = 0
    min_marks = float('inf')
    max_marks = 0
    # Set is used to store unique subjects
    subjects = set()
    
    for details in students.values():
        marks = details['Marks']
        total_marks += marks
        min_marks = min(min_marks, marks)
        max_marks = max(max_marks, marks)
        subjects.add(details['Subject'])
        
    avg_marks = total_marks / len(students)
    
    # Tuple is used to return aggregate results immutably
    return (min_marks, max_marks, avg_marks, subjects)
