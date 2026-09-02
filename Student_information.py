def student_information():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    department = input("Enter your department: ")   
    CGPA = float(input("Enter your CGPA: "))
    print("Student Information:")
    print("Name:", name)
    print("Age:", age)  
    print("Department:", department)
    print("CGPA:", CGPA)

student_information()