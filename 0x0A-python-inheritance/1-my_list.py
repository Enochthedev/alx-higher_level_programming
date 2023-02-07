#!/usr/bin/python3
# 1-my_list.py
#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass
    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)