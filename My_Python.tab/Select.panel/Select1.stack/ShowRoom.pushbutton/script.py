__doc__ = 'Show Room'
__author__ = 'https://github.com/HoangQuang1507'
__title__ = 'Show Room'

from Autodesk.Revit.DB.Architecture import Room
from Autodesk.Revit.DB import ElementId,RevitLinkInstance,Transaction
from Autodesk.Revit.DB import FilteredElementCollector,BuiltInCategory,ElementCategoryFilter,ElementMulticategoryFilter
from System.Collections.Generic import List 
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
#filter file room
collector = FilteredElementCollector(doc)
filterRoom = ElementCategoryFilter(BuiltInCategory.OST_Rooms)
#collectorRoom = collecter.OfCategory(BuiltInCategory.OST_Rooms)
room = collector.WherePasses(filterRoom).WhereElementIsNotElementType().ToElements()
listElementId = List[ElementId]()
#print(room)

t = Transaction(doc,'hiden unhide')
t.Start()

for idRoomm in room:
    linkedFileId = idRoomm.Id
    #print(linkedFileId)

    listElementId.Add(linkedFileId)
    if doc.GetElement(linkedFileId).IsHidden(doc.ActiveView):
        if doc.GetElement(linkedFileId).CanBeHidden(doc.ActiveView):
                doc.ActiveView.UnhideElements(listElementId)
    else:
        doc.ActiveView.HideElements(listElementId)
t.Commit()
