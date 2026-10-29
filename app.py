def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def main():
    num_subjects = int(input("Enter number of subjects: "))
    
    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
        
    total, average = calculate_grade(marks)
        
    print("\n--- Results ---")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}%")

if __name__ == "__main__":
    main()
