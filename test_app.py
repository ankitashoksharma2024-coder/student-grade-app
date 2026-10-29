from app import calculate_grade

def test_metrics_case_one():
    total, average = calculate_grade([80, 90, 70])
    assert total == 240
    assert average == 80.0

def test_metrics_case_two():
    total, average = calculate_grade([50, 60])
    assert total == 110
    assert average == 55.0
