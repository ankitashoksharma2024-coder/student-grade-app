from app import calculate_grade

def test_metrics_case_one():
    total, average, grade = calculate_grade([90, 80, 70])
    assert total == 240
    assert average == 80.0
    assert grade == "B"

def test_metrics_case_two():
    total, average, grade = calculate_grade([50, 60])
    assert total == 110
    assert average == 55.0
    assert grade == "F"