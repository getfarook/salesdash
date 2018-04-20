from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
    # url(r"^$", views.ListGroups.as_view(), name="all"),
    url(r"^datetest/$", views.DateTestView.as_view(), name="datetest"),
    url(r'^ajax/gtcustarea/$', views.CreateInvoice.get_customer_area, name='get_cust_area'),
    url(r"^jstest/$", views.JsTestView.as_view(), name="jstest"),
    url(r"^new/$", views.CreateInvoice.as_view(), name="create"),
    url(r"^newcn/$", views.CreateCreditNote.as_view(), name="createcn"),
    url(r"^invoice/(?P<pk>\d+)/$", views.InvoiceDetail.as_view(), name="single"),
    url(r"^cn/(?P<pk>\d+)/$", views.CreditNoteDetail.as_view(), name="cndetail"),
    path('list/', views.ListInvoice.as_view(),name='invoicelist'),
    path('cnlist/', views.ListCreditNote.as_view(),name='creditnotelist'),
    url('update/(?P<pk>\d+)/$', views.UpdateInvoice.as_view(),name='updateinvoice'),
    url('delete/(?P<pk>\d+)/$', views.DeleteInvoice.as_view(),name='deleteinvoice'),
    # url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    # url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    # url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
