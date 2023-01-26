from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon name",["pikachu", "Charmendor", "Squirtle"])
table.add_column("Type", ["Elecric", "fire", "water"])
table.align= "l"
print(table)