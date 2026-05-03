from model import StudentEnrollment
from logic import EnrollmentManager

def display_menu():
    print("\n=== Student Enrollment System ===")
    print("1. Register New Student (Interactive)")
    print("2. Run Predefined Test Cases")
    print("3. Exit")
    return input("Select an option (1-3): ").strip()

def interactive_registration(manager):
    print("\n--- New Student Registration ---")
    name = input("Enter Student Full Name: ").strip()
    email = input("Enter Email Address: ").strip()
    
    print("\nAvailable Courses:")
    for idx, course in enumerate(manager.ALLOWED_COURSES, 1):
        print(f"  {idx}. {course}")
    
    course_input = input("Select Course (enter number 1-4): ").strip()
    try:
        course_idx = int(course_input) - 1
        if course_idx < 0 or course_idx >= len(manager.ALLOWED_COURSES):
            print("Invalid course selection.")
            return
        course_title = manager.ALLOWED_COURSES[course_idx]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    try:
        duration = int(input("Enter Course Duration (in weeks): ").strip())
    except ValueError:
        print("Invalid duration. Please enter a number.")
        return
    
    student = StudentEnrollment(name, email, course_title, duration)
    result = manager.register_student(student)
    print(f"\nResult: {result}")
    if result == "SUCCESS":
        print(f"Enrollment ID: {student.enrollment_id}")
        print(f"Student: {student.name}")
        print(f"Course: {student.course_title}")
        print(f"Duration: {student.duration} weeks")

def run_tests(manager):
    print("\n--- Running Predefined Test Cases ---")
    print("\nTest 1: Valid Enrollment")
    student1 = StudentEnrollment("John Doe", "john@example.com", "Machine Learning with Python", 12)
    res1 = manager.register_student(student1)
    print(f"Result: {res1}")
    if res1 == "SUCCESS":
        print(f"Enrollment ID: {student1.enrollment_id}")
    
    print("\nTest 2: Invalid Course")
    student2 = StudentEnrollment("Jane Doe", "jane@example.com", "Invalid Course", 10)
    res2 = manager.register_student(student2)
    print(f"Result: {res2}")
    
    print("\nTest 3: Invalid Input (Empty Email)")
    student3 = StudentEnrollment("Bob Smith", "", "Python Essentials", 8)
    res3 = manager.register_student(student3)
    print(f"Result: {res3}")
    
    print("\nTest 4: Invalid Duration")
    student4 = StudentEnrollment("Alice Lee", "alice@example.com", "Cloud Fundamentals", -5)
    res4 = manager.register_student(student4)
    print(f"Result: {res4}")

def main():
    manager = EnrollmentManager()
    while True:
        choice = display_menu()
        if choice == "1":
            interactive_registration(manager)
        elif choice == "2":
            run_tests(manager)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
