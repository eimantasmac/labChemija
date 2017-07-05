import TableScrapper
import re
from sklearn import tree
import wikipedia

table = TableScrapper.Table.GetTable('https://en.wikipedia.org/wiki/Gold')

feature = 'Covalent radius'
for line in table:
    print(line)
    match = re.search('Covalent radius(\d+)', line)
    if match:
        print(match.group(1))

# print(table)





features = [[140, 1, 1], [130, 1, 1], [150, 0, 1], [170, 0, 1], [190, 0, 1], [800, 0, 0], [900, 0, 0]]  # dalykai
labels = [0, 0, 1, 1, 1, 2, 2]  # elementu numeris
clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

x = clf.predict([[90000, 1, 0]])
# print(x)
#
# for i in x:
#     if i == 1:
#         print("Vandenilis")
#     elif i == 2:
#         print("Helis")
#     else:
#         print("Litis")



