
from pyrevit import revit, DB
from pyrevit import forms
from pyrevit import script


logger = script.get_logger()


def duplicableview(view):
    return view.CanViewBeDuplicated(DB.ViewDuplicateOption.Duplicate)


def duplicate_views(viewlist, num=1,with_detailing=True):
    with revit.Transaction('Duplicate selected views'):
        for el in viewlist:
            for i in range(num):
                if with_detailing:
                    dupop = DB.ViewDuplicateOption.WithDetailing
                else:
                    dupop = DB.ViewDuplicateOption.Duplicate

                try:
                    el.Duplicate(dupop)
                except Exception as duplerr:
                    logger.error('Error duplicating view "{}" | {}'
                                .format(revit.query.get_name(el), duplerr))

try:
    selected_views = forms.select_views(filterfunc=duplicableview)

    #num = int(forms.ask_for_string("Enter number of views"))

    if selected_views:
        selected_option = \
            forms.CommandSwitchWindow.show(
                ['Duplicate',
                'Duplicate with Detailing'],
                message='Select duplication option:'
                )

        if selected_option:
            duplicate_views(
                selected_views,1,
                with_detailing=True if selected_option == 'Duplicate with Detailing'
                else False)
except:
    pass