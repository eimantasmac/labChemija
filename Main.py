import TableScrapper
import FeatureFinder
import re
import wikipedia
from sklearn import tree
from tkinter import *


# --- GUI-------------------------------------------
root = Tk()
label_ats = Label(root, text="here")
label_cov = Label(root, text="Covalent radius")
label_melt = Label(root, text="Melting point (C)")
entryCovalent = Entry(root)
entryMelt = Entry(root)

# --- Machine Learning------------------------------
featuresML = []
labels = []
features = ["Covalent radius", "Melting"]



def MainLoop():
    Start_gui()

    urls = open("urls.txt", "r")
    for one_url in urls:
        el_features = ReadOneElement(one_url)
        featuresML.append(el_features)
        label = re.findall('[A-Z][a-z]+', one_url)
        labels.append(label)

    root.mainloop()


# --- atvaizdavimas ------------------------------
def Start_gui():
    entryCovalent.grid(row=0)
    entryMelt.grid(row=0, column=1)
    label_cov.grid(row=1)
    label_melt.grid(row=1, column=1)
    button_1 = Button(root, text="Calculate", command=Calculate)
    button_1.grid(row=3)
    label_ats.grid(row=4)


def Calculate():
    ml = tree.DecisionTreeClassifier()
    ml = ml.fit(featuresML, labels)
    cal = entryCovalent.get()
    melt = entryMelt.get()
    ats = ml.predict([cal, melt])
    print(labels)
    print(featuresML)
    label_ats.config(text=ats)





def ReadOneElement(url):
    ats = []
    table = TableScrapper.Table.GetTable(url)
    for i in features:
        feat = FeatureFinder.FindFeature(i, table)
        if feat:
            feat = float(feat[0])
            if i == "Melting":
                feat -= 273.15
            ats.append(feat)
        else:
            ats.append('-9999999999')
            print('***********ELEMENT HAS NO FEATURE ' + i + "  url: " + url)

    if (len(ats)!=len(features)):
        print('*********Err***ELEMENT HAS NOT ENOUGH FEATURES (PROB BAD PARSING)')
    return ats


def ReadElements():
    return 1


MainLoop()








# features = [[140, 1, 1], [130, 1, 1], [150, 0, 1], [170, 0, 1], [190, 0, 1], [800, 0, 0], [900, 0, 0]]  # dalykai
# labels = [0, 0, 1, 1, 1, 2, 2]  # elementu numeris
# clf = tree.DecisionTreeClassifier()
#
# clf = clf.fit(features, labels)
#
# x = clf.predict([[90000, 1, 0]])
# print(x)
#
# for i in x:
#     if i == 1:
#         print("Vandenilis")
#     elif i == 2:
#         print("Helis")
#     else:
#         print("Litis")



