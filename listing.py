name ="Alex"
age = 25 
budget = 45.75 
shopping_list= ["bread","milk","eggs"] 

def check_budget(money ,item_list):
    if money > 30: 
        print("You have enough Budget!!!!!!!!!!!..")
        item_list.append("juice")
    else:
        print("Your Budget Is tight today.")
    return item_list
print("Shopping List for" ,name)
print("Age:", age)
print("Budget: Kshs", budget)

update_list = check_budget(budget,shopping_list)
print("Updated Shopping List :", update_list)


