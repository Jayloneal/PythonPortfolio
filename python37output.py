class AttendanceTracker:
    def __init__(self, class_size):
        self.attendance = {i: {'present': 0, 'absent': 0} for i in range(1, class_size+1)}
    
    def mark_present(self, student_id):
        self.attendance[student_id]['present'] += 1
    
    def mark_absent(self, student_id):
        self.attendance[student_id]['absent'] += 1
    
    def get_attendance(self, student_id):
        return self.attendance[student_id]
    
    def get_class_attendance(self):
        return self.attendance
    
# Create an attendance tracker for a class of 20 students
attendance_tracker = AttendanceTracker(20)
# Student 1 is present
attendance_tracker.mark_present(1)
# Student 2 is present
attendance_tracker.mark_present(2)
# Student 3 is absent
attendance_tracker.mark_absent(3)
# Student 4 is also absent
attendance_tracker.mark_absent(4)
# Student 5 is present
attendance_tracker.mark_present(5)
# Student 6 is absent
attendance_tracker.mark_absent(6)
# Student 7 is absent
attendance_tracker.mark_absent(7)
# Student 8 is present
attendance_tracker.mark_present(8)
# Student 9 is present
attendance_tracker.mark_present(9)
# Student 10 is absent
attendance_tracker.mark_absent(10)
# Student 11 is absent
attendance_tracker.mark_absent(11)
# Student 12 is absent
attendance_tracker.mark_absent(12)
# Student 13 is present
attendance_tracker.mark_present(13)
# Student 14 is present
attendance_tracker.mark_present(14)
# Student 15 is absent
attendance_tracker.mark_absent(15)
# Student 16 is absent
attendance_tracker.mark_absent(16)
# Student 17 is absent
attendance_tracker.mark_absent(17)
# Student 18 is absent
attendance_tracker.mark_absent(18)
# Student 19 is present
attendance_tracker.mark_present(19)
# Student 20 is present
attendance_tracker.mark_present(20)

# Get the attendance record for a specific student
attendance_record_5 = attendance_tracker.get_attendance(5)
print(attendance_record_5)

# Get the attendance records for the entire class
class_attendance = attendance_tracker.get_class_attendance()
print(class_attendance)
