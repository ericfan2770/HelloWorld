# modules: files to break up our code into multiple files (each file is a module)
# can import specific functions/methods as well

import converters  # imports entire module
from converters import kg_to_lbs  # imports specific function/class
from utils import find_max

print(converters.kg_to_lbs(70))  # need the "converters" prefix

print(kg_to_lbs(100))

# Exercise
numbers = [1, 2, 3, 5, 7, 2, 4, 6, 4, 8]
maximum = find_max(numbers)
print(maximum)
