# >= 75 — Distinction
# >= 60 — First Class
# >= 50— Second Class
# <= 50— Fail

def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")

    elif marks >= 60:
        print("First Class")
    
    elif marks >= 50:
        print("Second Class")

    else:
        print("Fail")

def main():
    print("Enter Marks: ")
    Marks=int(input())

    DisplayGrade(Marks)

if __name__=="__main__":
    main()