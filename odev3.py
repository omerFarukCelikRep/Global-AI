students = [];

for i in range(0,5):
    student = {};

    while True:
        try:
            if not "Name" in student.keys():
                student["Name"] = input("Please enter your name: ");


            if not "midterm" in student.keys():
                midterm = float(input("Please enter your midterm note: "));
                if not (0 <= midterm <= 100):
                    raise ValueError("Please enter a value between 0 and 100"); 
                student["midterm"] = midterm;


            if not "project" in student.keys():
                project = float(input("Please enter your project note: "));
                if not 0 <= project <= 100:
                    raise ValueError("Please enter a value between 0 and 100"); 
                student["project"] = project;



            if not "final" in student.keys():
                final = float(input("Please enter your final note: "));
                if not 0 <= final <= 100:
                    raise ValueError("Please enter a value between 0 and 100"); 
                student["final"] = final



            student["passingGerade"] = student["midterm"] * 0.3 + student["project"] * 0.3 + student["final"] * 0.4;

            break;
        except ValueError:
            print("Invalid Value");
        except:
            print("Error");

    students.append(student);


print(sorted(students, key = lambda i : i["passingGerade"], reverse=True));