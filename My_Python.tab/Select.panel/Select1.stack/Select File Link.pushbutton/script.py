
from rpw.ui.forms import Button, FlexForm, CheckBox, Label,  Separator
from rpw import doc
from Autodesk.Revit.DB import ElementId,RevitLinkInstance
from Autodesk.Revit.DB import FilteredElementCollector,BuiltInCategory
from Autodesk.Revit.DB import Transaction
from System.Collections.Generic import List 
#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
#filter file link

collectorLink = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RvtLinks).OfClass(RevitLinkInstance)
listElementId = List[ElementId]()

components = [Label('File Link:'), Separator()]
for linkFile in collectorLink:
    newKey = "R" + linkFile.Id.ToString()
    components.append(CheckBox(newKey,linkFile.Name))
components.append(Separator())
components.append(Button('Select'))
ff = FlexForm("Hide Or UnHide Links", components)
ff.show()

#get value from check box
result = ff.values
listKey = result.keys()
keyT =[]
for key in listKey:
    if result[key] == True:
        keyT.append(key)
t = Transaction(doc,'hiden unhide')
t.Start()
for linkedFile in collectorLink:
    if  "R" + linkedFile.Id.ToString() in  keyT:
        linkedFileId = linkedFile.Id
        listElementId.Add(linkedFileId)
        if(True == doc.GetElement(linkedFileId).IsHidden(doc.ActiveView)):
            if(True == doc.GetElement(linkedFileId).CanBeHidden(doc.ActiveView)):
                    doc.ActiveView.UnhideElements(listElementId)
        else:
            doc.ActiveView.HideElements(listElementId)
t.Commit()
