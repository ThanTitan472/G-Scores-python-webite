from django.db import models

# Create your models here.
class Result(models.Model):
    sbd = models.CharField(max_length=8, unique=True, primary_key=True)
    toan = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ngu_van = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ngoai_ngu = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    vat_li = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    hoa_hoc = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sinh_hoc = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    lich_su = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    dia_li = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    gdcd = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ma_ngoai_ngu = models.CharField(max_length=2, null=True, blank=True)
