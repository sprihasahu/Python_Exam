'''Question 4: Employee Salary Analysis 
   A company stores employee salaries in a list.
   Write a function to calculate the average salary, 
   display salaries above the average, 
   and increase every salary by 10%.
''' 
salaries=[10000,20000,30000,40000,50000]
def salary_analysis(salaries):
    avg=sum(salaries)/len(salaries)
    for i in salaries:
        if i>=avg:
            print(f"salary above the average sal{i}")
    for i in salaries:
        
        increase_sal=i*1.10
        print(f"increase every sal by 10% {increase_sal}")
    print(f"average sal{avg}")

salary_analysis(salaries)
    
            
        
