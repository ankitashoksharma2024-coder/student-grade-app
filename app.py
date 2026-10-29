def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return total, average, grade

def main():
    num_subjects = int(input("Enter number of subjects: "))
    
    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
        
    total, average, grade = calculate_grade(marks)
        
    print("\n--- Results ---")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
