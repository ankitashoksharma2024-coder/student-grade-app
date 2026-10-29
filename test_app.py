from app import calculate_grade

def test_metrics_case_one([80,60,70]):
    total, average, grade = calculate_grade()
    assert total == 240
    assert average == 80.0
    assert grade == "B"

def test_metrics_case_two([60,50]):
    total, average, grade = calculate_grade()
    assert total == 110
    assert average == 55.0
    assert grade == "F"
