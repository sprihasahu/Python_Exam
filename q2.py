'''
Question 2: Online Mobile Store An online store maintains a list of mobile prices. 
Write a function to display all mobiles costing more than ₹20,000, calculate the total
 inventory value, and find the most expensive mobile price. 
'''
def mobile_store(prices):
    for i in prices:
        if i>20000:
            print(f"Rs{i}")
    total=sum(prices)
    expensive=max(prices)

    print(f"the total inventory value {total}")
    print(f"most expensive mobile {expensive}")
prices=[20000,30000,40000,50000,80000]
mobile_store(prices)
