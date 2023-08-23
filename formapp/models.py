from django.db import models
import datetime
#from .forms import MultipleFileField

RESULT_CHOICES = [
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
        ("PENDING", "Pending"),
]


# Create your models here.
class FormEntry(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now().replace(microsecond=0))
    case_num = models.CharField(max_length=20, default='')
    inspector = models.CharField(max_length=30, default='')
    customer_supplier = models.CharField(max_length=50, default='')
    model_partname = models.CharField(max_length=30, default='')
    lanner_part_no = models.CharField(max_length=20, default='', blank=True)
    nonconf_quantity = models.CharField(max_length=10, default='')
    tot_lot_size = models.CharField(max_length=10, default='')
    wo_po_number = models.CharField(max_length=20, default='', blank=True)
    serial_nums = models.CharField(max_length=50, default='', blank=True)
    inspection_result = models.CharField(max_length=10, choices=RESULT_CHOICES, default='')
    ncmr = models.CharField(max_length=16, default='', blank=True)
    insp_report_if_rej = models.CharField(max_length=1000, default='', blank=True)

class FilesEntry(models.Model):
    file = models.FileField(upload_to="%Y%m%d-%H%M%S", null=True, blank=True)
    associated_entry = models.ForeignKey(FormEntry, on_delete=models.CASCADE)