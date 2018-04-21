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
from sales.forms import InvoiceForm, InvoiceFormSet,DateTestForm, CreditNoteForm
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
# test comment
#test comment 2
#test comment 3

class JsTestView(generic.TemplateView):
    template_name = 'sales/jstest.html'

class DateTestView(generic.TemplateView):
    form_class = DateTestForm
    template_name = 'sales/datetest.html'



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


################ CREDITNOTE VIEWS #############


class CreateCreditNote(LoginRequiredMixin, generic.CreateView):

    form_class = CreditNoteForm
    model = SalesInvoice
    success_url=reverse_lazy('sales:invoicelist')
    template_name = 'sales/creditnote_form.html'

class ListCreditNote(LoginRequiredMixin, generic.ListView):
    model = SalesInvoice
    template_name = 'sales/creditnote_list.html'

class CreditNoteDetail(LoginRequiredMixin, generic.DetailView):
    model = SalesInvoice
    template_name = 'sales/creditnote_detail.html'

################### END OF CREDITNOTE VIEWS ######
    # def get_absolute_url(self):
    #     return reverse("sales:single",kwargs={"pk": self.pk})
