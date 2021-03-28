import unittest
from Testing.Exercise.student.project.student import Student


class TestStudent(unittest.TestCase):
    name = "Test"
    courses = None

    def setUp(self):
        self.student = Student(self.name, self.courses)

    def test_student_init__when_courses_are_none__expect_courses_to_be_dict(self):
        self.assertEqual({}, self.student.courses)

    def test_student_enroll__when_course_is_already_added__expect_to_change_notes(self):
        self.student.courses["test"] = ["test_notes"]
        self.assertEqual("Course already added. Notes have been updated.", self.student.enroll("test", ["test_notes2"]))
        self.assertEqual(["test_notes", "test_notes2"], self.student.courses["test"])

    def test_student_enroll__when_course_is_not_added_and_add_notes_is_empty__expect_add_course_with_notes(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll("test", ["test_note"]))
        self.assertEqual(["test_note"], self.student.courses["test"])

    def test_student_enroll__when_course_is_not_added_and_add_notes_is_Y__expect_add_course_with_notes(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll("test", ["test_note"], "Y"))
        self.assertEqual(["test_note"], self.student.courses["test"])

    def test_student_enroll__when_add_notes_is_not_empty_or_Y__expect_course_to_be_added_with_empty_list(self):
        self.assertEqual("Course has been added.", self.student.enroll("test", ["test"], "N"))
        self.assertEqual([], self.student.courses["test"])

    def test_student_add_notes__when_course_is_not_in_courses__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("test", ["test"])

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_student_add_notes__when_course_is_in_courses__expect_to_update_notes(self):
        self.student.courses["test"] = ["test1"]
        self.assertEqual("Notes have been updated", self.student.add_notes("test", "test2"))
        self.assertEqual(["test1", "test2"], self.student.courses["test"])

    def test_student_leave_course__when_course_is_not_in_courses__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("test")

        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_student_leave_course__when_course_is_in_courses__expect_course_to_be_removed(self):
        self.student.courses["test"] = ["test"]
        self.assertEqual("Course has been removed", self.student.leave_course("test"))
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    unittest.main()
