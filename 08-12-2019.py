# Notes for class on the evening of August 12th, 2019

"""
Object Oriented Programming is great when you have lots of pieces of information with similar characteristics / functions

"""


class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = ""
        output += self.name + "\n"
        i = 1
        for c in self.categories:
            output += str(i) + ". " + c + "\n"
            i += 1

        return output


my_store = Store("The Dugout", ["Running", "Baseball", "Basketball"])


print(my_store)

selection = input("Please select the number of a department: ")

print("The user selected " + my_store.categories[int(selection) - 1])
