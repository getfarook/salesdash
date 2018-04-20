from django.db import models
from django.urls import reverse

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Partner(models.Model):
    CUSTOMER = 'CS'
    SUPPLIER = 'SP'
    BOTH = 'BT'
    PARTNER_TYPES = (
        (CUSTOMER,'Customer'),
        (SUPPLIER,'Supplier'),
        (BOTH,'Both'),
    )

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=2,choices=PARTNER_TYPES,default=CUSTOMER)
    area = models.ForeignKey(Area,on_delete=models.PROTECT,related_name='partners',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class ProductCat(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(ProductCat,on_delete=models.PROTECT,related_name='products')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.name


class SalesInvoice(models.Model):
    SALESINVOICE = 'SI'
    CREDITNOTE = 'CN'
    DEBITNOTE = 'DN'
    RECEIPT  = 'RC'
    #below snippet to be removed later as document type should be programmatically set..
    DOCUMENT_TYPES = (
        (SALESINVOICE,'SInvoice'),
        (RECEIPT,'Receipt'),
        (CREDITNOTE,'Credit Note'),
        (DEBITNOTE,'Debit Note'),
    )

    doc_type = models.CharField(max_length=2,choices=DOCUMENT_TYPES)
    date = models.DateField() #?? is this right type?
    doc_no = models.CharField(max_length=20, null=True,blank=True)  #for saving Tally or other ERP invoice no
    customer = models.ForeignKey(Partner, on_delete=models.PROTECT, related_name='invoices')
    total_discount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    details = models.CharField(max_length=250, null=True,blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    #company
    #created_time
    #edited_time
    #created_by
    #edited_by

    def get_absolute_url(self):
        return reverse("sales:single",kwargs={"pk": self.pk})


class SalesInvoiceLine(models.Model):
    salesinvoice = models.ForeignKey(SalesInvoice,on_delete=models.CASCADE, related_name='invoicelines')
    product = models.ForeignKey(Product,on_delete=models.PROTECT, related_name='pro_invoices')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total =  models.DecimalField(max_digits=10, decimal_places=2)
