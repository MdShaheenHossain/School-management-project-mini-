class Teacher:
    def __init__(self,name):
        self.name=name

class Student:
    def __init__(self,name):
        self.name=name
        self.classroom=None

class Classroom:
    def  __init__(self,name):
        self.name=name
        self.students=[]

    def add_student(self,student):
        student.classroom=self
        self.students.append(student)

class School:
    def __init__(self,name):
        self.name=name
        self.classrooms={}
        self.teachers={}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher
    
    def student_admission(self,student,classname): #চেক করবা এখানে classname আছে কিনা যেটা তুমি দিচ্ছো। 
        if classname in self.classrooms: # if classname in classrooms.keys() দিলেও একই কাজ করবে, আসলে dictionary তে if in দিয়ে চেক করলে এটি অটোমেটিক keys এর সাথেই তুলনা করে,ভ্যালুর সাথে চেক করে না। 
            self.classrooms[classname].add_student(student)
        else:
            print(f"Class '{classname}' not found! Admission failed for {student.name}.")
    def print_school_info(self):
        print(f"******School Name: {self.name}******")
        print(" ======================================")
        print("Teachers List")
        for subject,teacher in self.teachers.items():
            print(f"{subject}---> {teacher.name}")
        
        print("Classrooms: ")
        for classname,classroom in self.classrooms.items():
            print(f"{classname} has {len(classroom.students)} student")
            for student in classroom.students:
                print(f"-{student.name}")


teacher1=Teacher('Mr. Romesh')
teacher2=Teacher('Mis Nasrin')

school1=School('Green School')

student1=Student('sadia')
student2=Student('Dighi')
student3=Student('Ensana')
student4=Student('Rajia')
student5=Student('Ehdina')

classroom1=Classroom('6A')
classroom2=Classroom('7A')
classroom3=Classroom('8A')
classroom4=Classroom('9A')

school1.add_classroom(classroom1)
school1.add_classroom(classroom2)
school1.add_classroom(classroom3)
school1.add_classroom(classroom4) 

school1.add_teacher('math',teacher1)
school1.add_teacher('English',teacher2)
school1.add_teacher('G.S',teacher1)

school1.student_admission(student1,'6A')
school1.student_admission(student2,'6A')
school1.student_admission(student3,'7A')
school1.student_admission(student4,'8A')
school1.student_admission(student5,'9A')

school1.print_school_info()










        