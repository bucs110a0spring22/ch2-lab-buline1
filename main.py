import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class,type(cost_per_class))
print("The cost per class at this particular school happens to be", cost_per_class, ":)")
#Part B
number_list = [5,15,22,7,31]
random_result = random.choice(number_list)
print(random_result)