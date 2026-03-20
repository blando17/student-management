import streamlit as st
from core_logic import load_data, add_student, delete_student, search_student, analyze_data

st.set_page_config(page_title="Student Management System", layout="wide")

st.title("🎓 Student Management System")
st.markdown("A GUI wrapper built with Streamlit utilizing underlying CUI core principles and Python's Dictionary, List, Set, and Tuple data structures.")

# Load Data Once per Session
if 'students' not in st.session_state:
    st.session_state.students = load_data()

students = st.session_state.students

menu = ["Add Student", "Delete Student", "Search Student", "Analyze Data"]
choice = st.sidebar.selectbox("Main Menu", menu)

if choice == "Add Student":
    st.subheader("Add New Student")
    with st.form("add_student_form"):
        sid = st.text_input("Student ID (e.g., STU051)")
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=5, max_value=100, step=1)
        subject = st.text_input("Subject")
        marks = st.number_input("Marks", min_value=0, max_value=100, step=1)
        submit = st.form_submit_button("Add to System")
        
        if submit:
            if not sid or not name or not subject:
                st.error("Please fill in all textual fields.")
            else:
                success, msg = add_student(students, sid, name, age, subject, marks)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
                    
elif choice == "Delete Student":
    st.subheader("Delete Student Record")
    
    # Display current students in a simple format
    with st.expander("View All Student IDs (Dictionaries Keys)"):
        st.write(list(students.keys()))
        
    sid_delete = st.text_input("Enter Student ID to Delete:")
    if st.button("Delete Record"):
        if not sid_delete:
            st.warning("Please provide an ID.")
        else:
            success, msg = delete_student(students, sid_delete)
            if success:
                st.success(msg)
            else:
                st.error(msg)
                
elif choice == "Search Student":
    st.subheader("Search Student Database")
    st.info("Searching uses $O(1)$ Dictionary Lookup for IDs and List/Iteration for Names.")
    
    query = st.text_input("Enter Student ID or Name:")
    if st.button("Search"):
        if not query:
            st.warning("Please provide search criteria.")
        else:
            results = search_student(students, query)
            if not results:
                st.warning("No students found matching your query.")
            else:
                st.success(f"Found {len(results)} match(es)")
                display_results = [{'ID': sid, **details} for sid, details in results]
                st.table(display_results)
                
elif choice == "Analyze Data":
    st.subheader("System Data Analysis")
    st.info("Analysis relies on iteration, unique Set insertions for subjects, and returns an immutable Tuple.")
    
    results = analyze_data(students)
    if not results:
        st.warning("No data fundamentally exists for numerical analysis.")
    else:
        min_marks, max_marks, avg_marks, subjects_set = results
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Students", len(students))
        col2.metric("Minimum Marks", min_marks)
        col3.metric("Maximum Marks", max_marks)
        col4.metric("Average Marks", f"{avg_marks:.2f}")
        
        st.write("---")
        st.write(f"### Unique Subjects ({len(subjects_set)})")
        st.write(", ".join(subjects_set))
        
        # Display Leaderboard using List Sorting
        st.write("### Top 10 Leaderboard 🏆")
        leaderboard = sorted(
            [{'ID': sid, **details} for sid, details in students.items()],
            key=lambda x: x['Marks'],
            reverse=True
        )[:10]
        st.table(leaderboard)
