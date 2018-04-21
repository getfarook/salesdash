from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [

    #Sales Invoice
    url(r'^ajax/gtcustarea/$', views.CreateInvoice.get_customer_area, name='get_cust_area'),
    url(r"^new/$", views.CreateInvoice.as_view(), name="create"),
    url(r"^invoice/(?P<pk>\d+)/$", views.InvoiceDetail.as_view(), name="single"),
    path('list/', views.ListInvoice.as_view(),name='invoicelist'),
    url('update/(?P<pk>\d+)/$', views.UpdateInvoice.as_view(),name='updateinvoice'),
    url('delete/(?P<pk>\d+)/$', views.DeleteInvoice.as_view(),name='deleteinvoice'),

    #Receipt

    #Credit Note
    url(r"^newcn/$", views.CreateCreditNote.as_view(), name="createcn"),
    url(r"^cn/(?P<pk>\d+)/$", views.CreditNoteDetail.as_view(), name="cndetail"),
    path('cnlist/', views.ListCreditNote.as_view(),name='creditnotelist'),
    url('updatecn/(?P<pk>\d+)/$', views.UpdateCreditNote.as_view(),name='updatecreditnote'),
    url('deletecn/(?P<pk>\d+)/$', views.DeleteCreditNote.as_view(),name='deletecreditnote'),
    #Debit Note


    #Test-to-be-deleted
    url(r"^datetest/$", views.DateTestView.as_view(), name="datetest"),
    url(r"^jstest/$", views.JsTestView.as_view(), name="jstest"),









]
