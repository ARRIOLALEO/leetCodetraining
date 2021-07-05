def groupingDishes(dishes):
    ingredients = {}
    for i in range(len(dishes)):
        for j in range(1,len(dishes[i])):
            if dishes[i][j] not in ingredients:
                ingredients[dishes[i][j]] =[]
    
    for i in range(len(dishes)):
        dish = dishes[i][0]
        for j in range(1,len(dishes[i])):
            ingredients[dishes[i][j]].append(dish)
            
    solution = []
    for backet in ingredients:
        pre_solution = []
        if len(ingredients[backet]) >=2:
            pre_solution.append(backet)
            ingredients[backet].sort()
            for element in ingredients[backet]:
                pre_solution.append(element)
            solution.append(pre_solution)
    solution.sort()
    return solution
