import numpy as np

#common recipe format is:
# Flour, Sugar, Eggs, Milk, Butter

cupcakes = np.array([2., .75, 2., 1., .5])

"""recipes are:
cupcakes
pancake
cookie
bread"""
recipes = np.genfromtxt('myfiles/3/d3-recipes.csv', delimiter=',')
print recipes

eggs = recipes[:,2]

one_egg_recipes = recipes[:,2] == 1
print one_egg_recipes

# extract cookies
cookies = recipes[2,:]
print cookies

#making 2 batches of cupcakes
double_batch = cupcakes * 2
print double_batch

grocery_list = cookies + double_batch
print "grocery list"
print grocery_list