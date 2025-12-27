from student import student_details

def test_student_details():
    expected_output = (
        "student.usn=01fe24bca280\n"
        "student.name=alice\n"
        "division=E\n"
        "age=14\n"
    )
    assert student_details("01fe24bca280", "alice", "E", 14) == expected_output