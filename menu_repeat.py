def menu_is_boring(meals):
   
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
meals = [1,1,2,3,4]
menu_is_boring(meals)
