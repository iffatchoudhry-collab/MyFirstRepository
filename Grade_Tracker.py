import os
def input_store_grades():
    grades_dict={}
    print("--- Enter the Grades (Type 'done' when finished) ---")
    while True:
        subject=input("Enter subject Name: ").strip().lower()
        if subject=="done":
            break
        if not subject:
            print("Subject Name can not be empty")
            continue
        try:
            grade_input = input(f"Enter numerical grade for {subject}: ").strip()
            grade=float(grade_input)

            if grade<0 or grade>100:
                print("Error: Grade must be between 1-100 ")
                continue
            grades_dict[subject]=grade
        except ValueError:
            print("Please Enter Valid Input for the grade")
    return grades_dict

def grades_file(filename,grades_dict):
    try:
        with open(filename,'w')as file:
            for subject,grade in grades_dict.items():
                file.write(f"{subject},{grade}\n")
        print(f"\n[Success] Grades successfully saved to '{filename}'.")
    except IOError as e:
        print(f"File Error: Could Not write data to file. Details:",{e})

def cal_Average(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return
    grades_dict={}
    try:
        with open(filename,'r') as file:
            for line in file:
                if line.strip():
                    subject, grade_str = line.strip().split(',')
                    grades_dict[subject]= float(grade_str)
    except (ValueError, IndexError):
        print("Error: The file format is corrupt or incorrect.")
        return
    except IOError as e:
        print(f"File Error: Could not read file. Details: {e}")
        return

    #Calculate the average grade
    if not grades_dict:
        print("No Grades data found")
        return
    print("\n--- Saved Student Grades ---")
    for subject, grade in grades_dict.items():
        print(f" * {subject}: {grade}%")
        
    total_score = sum(grades_dict.values())
    total_subjects = len(grades_dict)
    average_grade = total_score / total_subjects
    
    print("----------------------------")
    print(f"Average Grade: {average_grade:.2f}%")

def main():
    data_file = "grades_data.txt"
    
    # 1. Collect user data
    student_grades = input_store_grades()
    
    if student_grades:
        # 2. Save data to file
        grades_file(data_file, student_grades)
        
        # 3. Read back from file and display calculations
        cal_Average(data_file)
    else:
        print("No data entered. Exiting application.")



main()




    


