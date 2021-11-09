from Autodesk.Revit.DB.JoinGeometryUtils import JoinGeometry,AreElementsJoined
from Autodesk.Revit.DB import Transaction ,ElementMulticategoryFilter,FilteredElementCollector,BuiltInCategory
from System.Collections.Generic import List
from Autodesk.Revit.DB import Outline,BoundingBoxIntersectsFilter
from Autodesk.Revit.Exceptions import ArgumentException
import rpw
from rpw.ui.forms import Button, ComboBox, FlexForm, CheckBox, Label, TextBox, Separator
from rpw import doc
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
#filter
collector = FilteredElementCollector(doc)
category = List[BuiltInCategory]([BuiltInCategory.OST_Walls,
                                    BuiltInCategory.OST_Floors,
                                    BuiltInCategory.OST_Ceilings,
                                    BuiltInCategory.OST_StructuralFraming,
                                    BuiltInCategory.OST_Columns])
filter = ElementMulticategoryFilter(category)
#print(filter)

familyInstances = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
#print(familyInstances)
categoryWall = "Walls"
categoryFloor = "Floors"
categoryCeiling = "Ceilings"
categoryStructuralFraming = "StructuralFraming"
categoryColumn = "Columns"
filter = ElementMulticategoryFilter(category)
#filter wall,floor
listFloor = []
listWall = []
listCeiling = []
listStructuralFraming = []
listColum = []
for element1 in familyInstances:
    elementid = element1.Id
    #print(eleid)
    element = doc.GetElement(elementid)
    #print(ele)
    elementCategory = element.Category
    #print(elecate)
    categoryName = elementCategory.Name
    #print(type(categoryName))
    if categoryWall == categoryName:
        listWall.append(element1)
    if categoryFloor == categoryName:
        listFloor.append(element1)
    if categoryCeiling == categoryName:
        listCeiling.append(element1)
    if categoryStructuralFraming == categoryName:
        listStructuralFraming.append(element1)
    if categoryColumn == categoryName:
        listColum.append(element1)

#print(listWall)
#print(listFloor)
#print(listCeiling)
#print(listStructuralFraming)
#print(listColum)

components = [Label('Elements:'),
            ComboBox('cut_element', {'Floors': 'floor',
                                     'Columns': 'column',
                                     'Structural Framing': 'beam',
                                     'Walls': 'wall',
                                     'Ceilings': 'ceiling',}),
            Separator(),
            Label('Elements:'),
            CheckBox('join_floor', 'Floors'),
            CheckBox('join_column', 'Columns'),
            CheckBox('join_beam', 'Structural Framing'),
            CheckBox('join_wall', 'Walls'),
            CheckBox('join_ceiling', 'Ceilings'),
            Button('Join')]

if rpw.ui.Selection():
    selected = True
else:
    selected = False

ff = FlexForm("Join Geometry", components)
ff.show()


t = Transaction(doc,"JoinGeometry")
t.Start()


#join geometry
for ele1 in listWall:
	bb = ele1.BoundingBox[doc.ActiveView]
	outline = Outline(bb.Min, bb.Max)
	bbfilter = BoundingBoxIntersectsFilter(outline)
	for e2 in listFloor:
            JoinGeometry(doc, ele1, e2)
t.Commit()
