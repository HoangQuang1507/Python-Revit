from Autodesk.Revit.DB.JoinGeometryUtils import SwitchJoinOrder,AreElementsJoined
from Autodesk.Revit.DB import Transaction ,ElementMulticategoryFilter,FilteredElementCollector,BuiltInCategory
from System.Collections.Generic import List
from Autodesk.Revit.DB import Outline,BoundingBoxIntersectsFilter
from Autodesk.Revit.Exceptions import ArgumentException
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

#filter
collector = FilteredElementCollector(doc)
category = List[BuiltInCategory]([BuiltInCategory.OST_Walls,BuiltInCategory.OST_Floors])
filter = ElementMulticategoryFilter(category)
#print(filter)
familyInstances = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
#print(familyInstances)
categorywall = "Walls"
categoryfloor = "Floors"
#filter wall,floor
listfloor = []
listWall = []
for elementwall in familyInstances:
    elementid = elementwall.Id
    #print(eleid)
    element = doc.GetElement(elementid)
    #print(ele)
    elementCategory = element.Category
    #print(elecate)
    categoryName = elementCategory.Name
    #print(type(categoryName))
    if categorywall == categoryName:
        listWall.append(elementwall)
    if categoryfloor == categoryName:
        listfloor.append(elementwall)
#print(listWall)
#print(listfloor)
t = Transaction(doc,"JoinGeometry")
t.Start()


#join geometry
for ele1 in listWall:
	bb = ele1.BoundingBox[doc.ActiveView]
	outline = Outline(bb.Min, bb.Max)
	bbfilter = BoundingBoxIntersectsFilter(outline)
	for e2 in listfloor:
            SwitchJoinOrder(doc, ele1, e2)
t.Commit()