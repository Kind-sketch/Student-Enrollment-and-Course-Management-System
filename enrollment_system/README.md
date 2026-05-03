# Student Enrollment and Course Management System

## Overview
A console-based Python application for registering students in short-term technical courses. It uses SQLite for persistent data storage, auto-generates unique enrollment IDs, and enforces strict input validation and business rules.

## Features
- Register new student enrollments with name, email, course title, and duration (in weeks)
- Auto-generate unique enrollment IDs (format: first 3 uppercase letters of course + numeric suffix starting at 1001)
- Validate all inputs (non-empty fields, positive duration, allowed courses only)
- Lightweight SQLite storage with automatic table creation

## Project Structure
```
enrollment_system/
├── model.py          # StudentEnrollment data structure
├── database.py       # Database operations and enrollment ID generation
├── logic.py          # Business rules and input validation
├── helper.py         # DB connection and custom exceptions
├── app.py            # Console interface with test cases
└── enrollment.db     # Auto-generated SQLite database (created on first run)
```

## Prerequisites
- Python 3.x installed

## How to Run
### Linux/macOS
1. Open a terminal and navigate to the project directory:
   ```bash
   cd enrollment_system
   ```
2. Execute the application:
   ```bash
   python3 app.py
   ```

### Windows
1. Open Command Prompt (cmd) or PowerShell.
2. Navigate to the project directory:
   ```cmd
   cd enrollment_system
   ```
3. Run the application using one of the following commands (depending on your Python installation):
   ```cmd
   python app.py
   ```
   OR
   ```cmd
   py app.py
   ```
   *Note: The `py` command is the Python launcher for Windows (included with most Python installations). If `python` is not recognized, try `py`. Ensure Python is added to your system PATH if needed.*

The first run will automatically create `enrollment.db` (SQLite database). To reset all enrollment data, delete this file.

## Interactive Usage
When you run the app, you will see a menu with three options:
1. **Register New Student (Interactive)**: Enter your own details (name, email, select course by number, duration) to register for a course.
2. **Run Predefined Test Cases**: Run the built-in test cases to verify system functionality.
3. **Exit**: Close the application.

User input for new registrations is entered directly via the console prompts in the interactive mode.

## Allowed Courses
Only the following courses are accepted for enrollment:
- Python Essentials
- Full Stack Java
- Machine Learning with Python
- Cloud Fundamentals

## Business Rules
- All fields (name, email, course title, duration) must be non-empty and valid
- Course duration must be a positive integer
- Course title must exactly match an entry in the predefined allowed list

## Expected Outputs
| Output             | Condition |
|---------------------|-----------|
| `SUCCESS`           | Student registered and data stored successfully |
| `FAILURE`           | Data insertion failed |
| `INVALID COURSE`    | Course not in the allowed list |
| `INVALID INPUT`     | Missing or incorrect required fields |

## Database Schema
Table `ENROLLMENT_INFO`:
| Column Name       | Data Type | Constraints |
|-------------------|-----------|-------------|
| ENROLLMENT_ID     | TEXT      | Primary Key |
| STUDENT_NAME      | TEXT      | Not Null    |
| EMAIL             | TEXT      | Not Null    |
| COURSE_TITLE      | TEXT      | Not Null    |
| DURATION_WEEK     | INTEGER   | Not Null    |

## Module Responsibilities
| Module       | Responsibility |
|--------------|----------------|
| `model.py`   | Defines `StudentEnrollment` class with student and enrollment attributes |
| `database.py`| Handles SQLite table creation, enrollment ID generation, and data persistence |
| `logic.py`   | Enforces business rules, validates inputs and allowed courses |
| `helper.py`  | Manages SQLite connections and defines `CourseNotAllowedException` |
| `app.py`     | Console entry point with sample test cases |

## Example Output
```
Test 1: Valid Enrollment
Result: SUCCESS
Enrollment ID: MAC1001

Test 2: Invalid Course
Result: INVALID COURSE

Test 3: Invalid Input (Empty Email)
Result: INVALID INPUT

Test 4: Invalid Duration
Result: INVALID INPUT
```
