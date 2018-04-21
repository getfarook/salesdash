from django.shortcuts import render,redirect
import pickle
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse,reverse_lazy
from braces.views import SelectRelatedMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic,View
from sales.models import SalesInvoice, SalesInvoiceLine
from sales.models import Partner
from . import models
from sales.forms import ( InvoiceForm, InvoiceFormSet, DateTestForm,
                            CreditNoteForm, DebitNoteForm, ReceiptForm )
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


class JsTestView(generic.TemplateView):
    template_name = 'sales/jstest.html'

class DateTestView(generic.TemplateView):
    form_class = DateTestForm
    template_name = 'sales/datetest.html'

################ INVOICE VIEWS BEGINS#############

class CreateInvoice(LoginRequiredMixin, generic.CreateView):

    form_class = InvoiceForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:invoicelist')


    def get_customer_area(request):
        customer = request.GET.get('customer', None)
        partner = Partner.objects.get(pk=customer)
        data = {
            'area': partner.area.name
        }
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super(CreateInvoice, self).get_context_data(**kwargs)
        if self.request.POST:
            context['invoiceline_formset'] = InvoiceFormSet(self.request.POST)
        else:
            context['invoiceline_formset'] = InvoiceFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['invoiceline_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UpdateInvoice(LoginRequiredMixin, generic.UpdateView):

    form_class = InvoiceForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:invoicelist')



    def get_context_data(self, **kwargs):
        context = super(UpdateInvoice, self).get_context_data(**kwargs)
        if self.request.POST:
            context['invoiceline_formset'] = InvoiceFormSet(self.request.POST, instance=self.object)
            context['invoiceline_formset'].full_clean()
        else:
            context['invoiceline_formset'] = InvoiceFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['invoiceline_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class InvoiceDetail(LoginRequiredMixin, generic.DetailView):
    model = SalesInvoice

class ListInvoice(LoginRequiredMixin, generic.ListView):
    model = SalesInvoice

class DeleteInvoice(LoginRequiredMixin, generic.DeleteView):
    model = SalesInvoice
    success_url = reverse_lazy('sales:invoicelist')

################ INVOICE VIEWS ENDS#############


################ CREDITNOTE VIEWS BEGINS#############


class CreateCreditNote(LoginRequiredMixin, generic.CreateView):

    form_class = CreditNoteForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:creditnotelist')
    template_name = 'sales/creditnote_form.html'

class UpdateCreditNote(LoginRequiredMixin, generic.UpdateView):
    form_class = CreditNoteForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:creditnotelist')
    template_name = 'sales/creditnote_form.html'

class ListCreditNote(LoginRequiredMixin, generic.ListView):
    model = SalesInvoice
    template_name = 'sales/creditnote_list.html'

class CreditNoteDetail(LoginRequiredMixin, generic.DetailView):
    model = SalesInvoice
    template_name = 'sales/creditnote_detail.html'

class DeleteCreditNote(LoginRequiredMixin, generic.DeleteView):
    model = SalesInvoice
    success_url = reverse_lazy('sales:creditnotelist')
    template_name = 'sales/creditnote_confirm_delete.html'

################### END OF CREDITNOTE VIEWS ######



################ DEBITNOTE VIEWS BEGINS#############
class CreateDebitNote(LoginRequiredMixin, generic.CreateView):

    form_class = DebitNoteForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:debitnotelist')
    template_name = 'sales/debitnote_form.html'

class UpdateDebitNote(LoginRequiredMixin, generic.UpdateView):
    form_class = DebitNoteForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:debitnotelist')
    template_name = 'sales/debitnote_form.html'

class ListDebitNote(LoginRequiredMixin, generic.ListView):
    model = SalesInvoice
    template_name = 'sales/debitnote_list.html'

class DebitNoteDetail(LoginRequiredMixin, generic.DetailView):
    model = SalesInvoice
    template_name = 'sales/debitnote_detail.html'

class DeleteDebitNote(LoginRequiredMixin, generic.DeleteView):
    model = SalesInvoice
    success_url = reverse_lazy('sales:debitnotelist')
    template_name = 'sales/debitnote_confirm_delete.html'

################### END OF DEBITNOTE VIEWS ######

################ RECEIPT VIEWS BEGINS#############


class CreateReceipt(LoginRequiredMixin, generic.CreateView):

    form_class = ReceiptForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:receiptlist')
    template_name = 'sales/receipt_form.html'

class UpdateReceipt(LoginRequiredMixin, generic.UpdateView):
    form_class = ReceiptForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:receiptlist')
    template_name = 'sales/receipt_form.html'

class ListReceipt(LoginRequiredMixin, generic.ListView):
    model = SalesInvoice
    template_name = 'sales/receipt_list.html'

class ReceiptDetail(LoginRequiredMixin, generic.DetailView):
    model = SalesInvoice
    template_name = 'sales/receipt_detail.html'

class DeleteReceipt(LoginRequiredMixin, generic.DeleteView):
    model = SalesInvoice
    success_url = reverse_lazy('sales:receiptlist')
    template_name = 'sales/receipt_confirm_delete.html'

################### END OF RECEIPT VIEWS ######

    # def get_absolute_url(self):
    #     return reverse("sales:single",kwargs={"pk": self.pk})
