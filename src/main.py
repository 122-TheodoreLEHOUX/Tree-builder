"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
"""

# from zeutek_python import example_module
# from common import submodule
import json

CONFIG_FILE_PATH = "config/config.json"

def main():
    """Program main loop"""
    # Read the config file
    with open(CONFIG_FILE_PATH) as json_file:
        config = json.load(json_file)

    # num = 29 + example_module.example_func(1, 2)
    num = 29
    # print(example_module.submodule.abc(1,2))

    # To take input from the user
    #num = int(input("Enter a number: "))

    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")

    else:
        print(num, "is a prime number")

    G = 10

if __name__ == "__main__": main()
