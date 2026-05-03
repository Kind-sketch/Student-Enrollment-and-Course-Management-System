from helper import get_db_connection

class EnrollmentDBHandler:
    @staticmethod
    def _create_table():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ENROLLMENT_INFO (
                ENROLLMENT_ID TEXT PRIMARY KEY,
                STUDENT_NAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                COURSE_TITLE TEXT NOT NULL,
                DURATION_WEEK INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def generate_enrollment_id(course_title):
        EnrollmentDBHandler._create_table()
        upper_course = course_title.upper()
        prefix_chars = [c for c in upper_course if c.isalpha()][:3]
        prefix = ''.join(prefix_chars)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ENROLLMENT_ID FROM ENROLLMENT_INFO WHERE ENROLLMENT_ID LIKE ?", (f"{prefix}%",))
        rows = cursor.fetchall()
        max_suffix = 1000
        for row in rows:
            eid = row[0]
            suffix_str = eid[len(prefix):]
            if suffix_str.isdigit():
                suffix = int(suffix_str)
                if suffix > max_suffix:
                    max_suffix = suffix
        next_suffix = max_suffix + 1
        conn.close()
        return f"{prefix}{next_suffix}"

    @staticmethod
    def save_enrollment(student_obj):
        EnrollmentDBHandler._create_table()
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO ENROLLMENT_INFO (ENROLLMENT_ID, STUDENT_NAME, EMAIL, COURSE_TITLE, DURATION_WEEK)
                VALUES (?, ?, ?, ?, ?)
            """, (student_obj.enrollment_id, student_obj.name, student_obj.email, student_obj.course_title, student_obj.duration))
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            return False
        finally:
            conn.close()
