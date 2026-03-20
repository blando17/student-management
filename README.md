# Student Management System

This project is a complete Student Management System implemented in Python, offering a Command Line Interface (CUI) and a Graphical User Interface (GUI) powered by Streamlit.

## Data Structure Utilization

As per the requirements, we strictly use Python's built-in data structures to handle data efficiently in memory:

### 1. Dictionary (`dict`)
- **Purpose**: Used as the primary in-memory database to store all students. 
- **Implementation**: The keys are the unique `Student ID`s, and the values are nested dictionaries containing the student's details (Name, Age, Subject, Marks).
- **Advantage**: Provides $O(1)$ average time complexity for searching, adding, and deleting student records by ID.

### 2. List (`list`)
- **Purpose**: Used for ordered collections of data.
- **Implementation**: 
  - To store the headers and rows when reading from or writing to the CSV file.
  - To collect and return multiple student records when searching by name (since names might not be unique).
  - To sort and display a leaderboard based on student marks.
- **Advantage**: Maintains the order of elements and allows for sorting and iteration.

### 3. Set (`set`)
- **Purpose**: Used for storing unique collections of items for analysis.
- **Implementation**: To quickly determine and display all the unique subjects currently enrolled by the students.
- **Advantage**: Ensures uniqueness without duplicates and provides fast membership testing.

### 4. Tuple (`tuple`)
- **Purpose**: Used to represent immutable grouped data.
- **Implementation**: When performing statistical analysis, the analysis function returns multiple aggregated values (e.g., `(min_marks, max_marks, average_marks)`) as a tuple.
- **Advantage**: Protects the aggregated results from being accidentally modified and provides a clean way to return multiple values from a function.
