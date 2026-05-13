# 8-15
import printing_functions as pf
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
print()

# 8-16
'''
import greeting
greeting.greet_user("jesse")

from greeting import greet_user
greet_user("jesse")

from greeting import greet_user as gu
gu("jesse")

import greeting as g
g.greet_user("jesse")
'''
from greeting import *
greet_user("jesse")
'''
'''