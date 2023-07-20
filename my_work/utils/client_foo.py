from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from my_work.models import Client
from my_work.forms import CustomerForm


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'my_work/client/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class CustomerCreateView(generic.CreateView):
    model = Client
    form_class = CustomerForm
    template_name = 'my_work/client/client_form.html'
    success_url = reverse_lazy('my_work:customers')


class CustomerUpdateView(generic.UpdateView):
    model = Client
    form_class = CustomerForm
    template_name = 'my_work/client/client_detail.html'
    success_url = reverse_lazy('my_work:customers')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('my_work:customer_update', kwargs={'pk': pk})


class CustomerDeleteView(generic.DeleteView):
    model = Client
    template_name = 'my_work/client/client_delete.html'
    success_url = reverse_lazy('my_work:customers')

    def test_func(self):
        return self.request.user.is_superuser
