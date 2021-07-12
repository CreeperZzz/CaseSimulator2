# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import case
import tools
import sqlConnect


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    res = [tools.randItem() for i in range(1000)]
    # print(res)
    print(res.count('a'), res.count('b'), res.count('c'))

