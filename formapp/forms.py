from django import forms
from .models import FormEntry, FilesEntry
from django.utils.translation import gettext_lazy as _


class EntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        exclude = ['date','case_num']
        labels = {
            "inspector": _("Inspector"),
            "customer_supplier": _("Customer / Supplier"),
            "model_partname": _("Model / Part Name"),
            "lanner_part_no": _("Lanner Part No. "),
            "nonconf_quantity": _("Nonconforming Quantity"),
            "tot_lot_size": _("Total Lot Size"),
            "wo_po_number": _("Work Order / Purchase Order No. "),
            "serial_nums": _("Serial Numbers (Enter as comma separated values)"),
            "inspection_result": _("Inspection Result"),
            "ncmr": _("NCMR"),
            "insp_report_if_rej": _("Inspection Report if Rejected"),
        }
        widgets = {
            "nonconf_quantity": forms.TextInput(attrs={'placeholder': '0'}),
            "tot_lot_size": forms.TextInput(attrs={'placeholder':'0'}),
            "serial_nums": forms.TextInput(attrs={'placeholder':'123456, 789012, 345678'}),
            "insp_report_if_rej": forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }
        

class EntryFilesForm(forms.ModelForm):
    class Meta:
        model = FilesEntry
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }