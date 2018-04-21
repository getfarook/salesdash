from django import forms
from sales.models import SalesInvoice, SalesInvoiceLine
from django.forms.models import inlineformset_factory
from bootstrap_datepicker.widgets import DatePicker
#from sales.models.SalesInvoice import SALESINVOICE, CREDITNOTE, DEBITNOTE, RECEIPT

class DateTestForm(forms.Form):

    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )

class InvoiceForm(forms.ModelForm):
    class Meta():
        model = SalesInvoice
        fields = ("doc_type", "date",'doc_no','customer','total_discount','total','details','debit')

        widgets = {
            'doc_type':forms.Select(attrs={'id':'idoctype','value':SalesInvoice.SALESINVOICE}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date','id':'idate'}),
            'doc_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Tally Inv No.','id':'idocno'}),
            'customer':forms.Select(attrs={'class':'form-control','placeholder':'Select Customer','id':'icustomer'}),
            'total_discount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Discount','id':'idiscount'}),
            'total':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total','id':'itotal'}),
            'details':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control','placeholder':'All misc details about bill','rows':'2','id':'idetails'}),
            'debit':forms.NumberInput(attrs={'class':'form-control','placeholder':'Grand Total','id':'gtotal'}),
        }

class DebitNoteForm(forms.ModelForm):
    class Meta():
        model = SalesInvoice
        fields = ("doc_type", "date",'doc_no','customer','details','debit')

        widgets = {
            'doc_type':forms.Select(attrs={'id':'idoctype'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date','id':'idate'}),
            'doc_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Tally Inv No.','id':'idocno'}),
            'customer':forms.Select(attrs={'class':'form-control','placeholder':'Select Customer','id':'icustomer'}),
            'details':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control','placeholder':'All misc details about bill','rows':'2','id':'idetails'}),
            'debit':forms.NumberInput(attrs={'class':'form-control','placeholder':'Grand Total','id':'amount'}),
        }


class CreditNoteForm(forms.ModelForm):
    class Meta():
        model = SalesInvoice
        fields = ("doc_type", "date",'doc_no','customer','details','credit')

        widgets = {
            'doc_type':forms.Select(attrs={'id':'idoctype'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date','id':'idate'}),
            'doc_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Tally Inv No.','id':'idocno'}),
            'customer':forms.Select(attrs={'class':'form-control','placeholder':'Select Customer','id':'icustomer'}),
            'details':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control','placeholder':'All misc details about bill','rows':'2','id':'idetails'}),
            'credit':forms.NumberInput(attrs={'class':'form-control','placeholder':'Grand Total','id':'amount'}),
        }


class ReceiptForm(forms.ModelForm):
    class Meta():
        model = SalesInvoice
        fields = ("doc_type", "date",'doc_no','customer','details','credit')

        widgets = {
            'doc_type':forms.Select(attrs={'id':'idoctype'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date','id':'idate'}),
            'doc_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Tally Inv No.','id':'idocno'}),
            'customer':forms.Select(attrs={'class':'form-control','placeholder':'Select Customer','id':'icustomer'}),
            'details':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control','placeholder':'All misc details about bill','rows':'2','id':'idetails'}),
            'credit':forms.NumberInput(attrs={'class':'form-control','placeholder':'Grand Total','id':'amount'}),
        }



InvoiceFormSet = inlineformset_factory(SalesInvoice, SalesInvoiceLine, fields=('__all__'))
