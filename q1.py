'''Question 1: Student Marks Analysis A college stores students' marks in a list. 
   Write a function that accepts a list of marks and displays the highest mark, lowest mark,
   average mark, and number of students who passed (marks of 40 or above). 
 '''
def analyze_marks(marks):
    mx=max(marks)
    mn=min(marks)
    avg=sum(marks)/len(marks)
    passed=0
    for i in marks:
        if i>40:
            passed=+1
    print(f"number of students passed{passed}")
    print(f"maximum marks{mx}")
    print(f"minimum marks{mn}")
    print(f"average marks{avg}")


marks=[45,56,67,78,89,40,39]
analyze_marks(marks)