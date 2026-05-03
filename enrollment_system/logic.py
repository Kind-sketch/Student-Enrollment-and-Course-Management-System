from helper import CourseNotAllowedException
from database import EnrollmentDBHandler

class EnrollmentManager:
    ALLOWED_COURSES = [
        "Python Essentials",
        "Full Stack Java",
        "Machine Learning with Python",
        "Cloud Fundamentals"
    ]

    def validate_course(self, course_title):
        if course_title not in self.ALLOWED_COURSES:
            raise CourseNotAllowedException(f"Course '{course_title}' is not allowed")

    def register_student(self, student_obj):
        if not student_obj.name or not isinstance(student_obj.name, str) or student_obj.name.strip() == "":
            return "INVALID INPUT"
        if not student_obj.email or not isinstance(student_obj.email, str) or student_obj.email.strip() == "":
            return "INVALID INPUT"
        if not student_obj.course_title or not isinstance(student_obj.course_title, str) or student_obj.course_title.strip() == "":
            return "INVALID INPUT"
        if not isinstance(student_obj.duration, int) or student_obj.duration <= 0:
            return "INVALID INPUT"
        try:
            self.validate_course(student_obj.course_title)
        except CourseNotAllowedException:
            return "INVALID COURSE"
        enrollment_id = EnrollmentDBHandler.generate_enrollment_id(student_obj.course_title)
        student_obj.enrollment_id = enrollment_id
        success = EnrollmentDBHandler.save_enrollment(student_obj)
        return "SUCCESS" if success else "FAILURE"
