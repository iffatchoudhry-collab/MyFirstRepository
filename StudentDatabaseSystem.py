class Student:
    def __init__(self,name:str,age:int,grades:list):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def calculate_average(self)->float:
        if not self.grades:
            return 0.0
        return sum(self.grades)/len(self.grades)
    def display_info(self):
        avg_grade=self.calculate_average()
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades},Average: {avg_grade:.2f} ")



class StudentDatabase:
    def __init__(self):
        self.students=[]

    def add_student(self, student:Student):
        self.students.append(student)
        print("Successfully added Student", student.name)

    def display_all(self):
        if not self.students:
            print("The database is Empty")
            return
        print("\n--------Current Students Record---------")
        for student in self.students:
            student.display_info()
        print("--------------------------------------------\n")

def main():
    print("*******Initializing Student Database************\n")
    db=StudentDatabase()
    student1=Student("John Smith",20,[85,97,78])
    student2=Student("Peter Borough", 24,[99,89,91])
    db.add_student(student1)
    db.add_student(student2)

    # Display Records
    db.display_all()

    #Allow users to add new students to the database.
    try:

        st_name=input("Enter Student Name: ").strip()
        st_age=int(input("Enter Student's Age: "))
        st_grades=input("Enter Grades separated by spaces: ")
        st_gradesls=[float(g) for g in st_grades.split() if g.strip()]
        new_student=Student(st_name,st_age,st_gradesls)
        db.add_student(new_student)

    except ValueError:
        print("Invalid input format")
    db.display_all()

main()
        