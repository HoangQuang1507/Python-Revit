# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import FilteredElementCollector,BuiltInCategory,ElementCategoryFilter 
import os
from rpw.ui.forms import select_file
import pathlib
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
path_file = select_file('File Cad(*.dwg)|*.dwg',multiple = True)
#print(path_file)
listNameDwg = []
nlDwg = []
levelfileDwg = []

for fileName in path_file:
    fname = str(fileName).split('\\')[-1:][0]
    listNameDwg.insert(0,fname)

for levelDwg in listNameDwg:
    lname = str(levelDwg).split("_")[-1:][0]
    nlDwg.insert(0,lname)

for lDwg in nlDwg:
    levelnameDwg = str(lDwg).split(".")[0:][0]
    #print(levelnameDwg)
    levelfileDwg.insert(0,levelnameDwg)
levelfileDwg.reverse()
#print(levelfileDwg)

dictDwg = zip(path_file,levelfileDwg)
#print(dictDwg)
collector = FilteredElementCollector(doc)
filter = ElementCategoryFilter(BuiltInCategory.OST_Views)
#print(filter)
view = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
print(view)