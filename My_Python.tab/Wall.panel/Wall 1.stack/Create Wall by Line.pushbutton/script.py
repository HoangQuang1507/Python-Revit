"Create wall"
from Autodesk.Revit.UI.Selection.Selection import PickObjects
from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import Element
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,BuiltInParameter,Location,Curve,ElementMulticategoryFilter
from Autodesk.Revit.DB import Transaction,Wall,Line,XYZ,WallType
from System.Collections.Generic import List 
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

#pick Object
pick = uidoc.Selection.PickObjects(ObjectType.Element)

#filter wall
list_curve = []
for i in pick:
    eleid = i.ElementId
    ele = doc.GetElement(eleid)
    #print(ele)

    #get loacation
    loca = ele.Location
    #print(loca)

    #create line
    curve = loca.Curve
    #print(curve)
    list_curve.append(curve)


    #get level
    ownerid = ele.OwnerViewId
    #print(ownerid)

    view = doc.GetElement(ownerid)
    #print(view)

    genlevel = view.GenLevel
    #print(genlevel)
    levelid = genlevel.Id
    #print(levelid)

t = Transaction(doc,"Creat Wall")
t.Start()

#creat wall
for profile in list_curve:
    wall = Wall.Create(doc,profile,levelid,True)

t.Commit()

