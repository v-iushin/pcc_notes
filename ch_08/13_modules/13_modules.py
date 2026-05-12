# FUNCTIONS IN MODULES



# its possible to store functions
# in a separate file (MODULE)
# then IMPORT them into program

# MODULE is file ending in .py



# to call MODULE:
# import module_name

# to call function from the MODULE:
# module_name.func_name(arg)



#! pizza.py MODULE
#! comments for selecting code



'''
import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mashroom", "green peppers", "extra cheese")
print()
'''



# IMPORTING SPECIFIC FUNCTIONS

# to call one:
# from module_name import func_name

# to call many:
# from module_name import func_0, func_1, ...

# to call SELECTED function in this case
# enough just func_name(arg)

'''
from pizza import make_pizza

make_pizza(16, "pepperoni")
make_pizza(12, "mashroom", "green peppers", "extra cheese")
print()
'''



# USING AS TO GIVE AN ALIAS
#! if renamed, cant use with old name

# FOR MODULE
# import module_name as mn
'''
import pizza as p

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mashroom", "green peppers", "extra cheese")
print()
'''

# FOR FUNCTION
# from module_name import func_name as fn
'''
from pizza import make_pizza as mp

mp(16, "pepperoni")
mp(12, "mashroom", "green peppers", "extra cheese")
print()
'''


# IMPORTING ALL FUNCTIONS

# from module_name import *

# to call ANY function in this case
# enough just func_name(arg)

from pizza import *

make_pizza(16, "pepperoni")
make_pizza(12, "mashroom", "green peppers", "extra cheese")
print()
