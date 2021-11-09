# -*- coding: utf-8 -*-


from rpw.ui.forms import select_file
import pathlib
path_file = select_file('Revit Model(*.dwg)|*.dwg',multiple = True)
print(path_file)
