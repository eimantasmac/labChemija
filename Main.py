import TableScrapper
import FeatureFinder
import re
from sklearn import tree
import wikipedia

table = TableScrapper.Table.GetTable('https://en.wikipedia.org/wiki/Gold')

ats = FeatureFinder.FindFeature('Covalent radius', table)
print(int(ats[0]))

# feature = 'Covalent radius'
# found = False
# for line in table.splitlines():
#     if found:
#         print(line)
#         found = False
#     match = re.search(feature, line)
#     if match:
#         #print(match.group(0))
#         found = True



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



