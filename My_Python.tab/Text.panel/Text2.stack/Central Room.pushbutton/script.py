from Autodesk.Revit.DB import Transaction,FilteredElementCollector,BuiltInCategory,Reference,XYZ

#get UIDocument
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
# collect all rooms 
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
# room status list for output
elems = []
# output
# start transaction
t = Transaction(doc,"Central Room")
t.Start()
# loop elements
for e in rooms:
	# level elevation - unit millimeter 
	elevation = e.Level.Elevation 
	# get geo-objects of the element
	geoelem = e.GetGeometryObjectFromReference(Reference(e))
	# get enumerator to loop geo-objects
	geoobj = geoelem.GetEnumerator()
	#print(geoobj)
	# loop geo-objector
	for obj in geoobj:
		# get the centroid of the element
		point = obj.ComputeCentroid()
		#print(point)
		# create location point with level elevation
		center = XYZ(point.X,point.Y,elevation)
		#print(center)
		# current element location
		current = e.Location.Point
		#print(current)	
		# point convert to revit and minus from current location
		newloc = center - current
		# move to new location
		e.Location.Move(newloc)
# transaction done
t.Commit()


