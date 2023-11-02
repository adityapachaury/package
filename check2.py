###Random module
import random

random_number = random.randint(1, 10)
random_choice = random.choice(['apple','banana','cherry'])

print(random_number,  random_choice)

###math module
import math

square_root = math.sqrt(25)
sine_value = math.sin(math.pi / 2)

print(sine_value)

##import string
import string

ascii_letters = string.ascii_letters
digits = string.digits
print(digits)

###datetime module

  
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)




###os module

import os

current_directory = os.getcwd()
list_of_files = os.listdir(current_directory)
print(list_of_files)




##sys module

import sys

command_line_arguments = sys.argv
python_version = sys.version

print(python_version)