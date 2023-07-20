from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from my_work.forms import NewsletterForm
from my_work.models import Newsletter
from my_work.services import send_newsletter


class NewsletterListView(LoginRequiredMixin, generic.ListView):
    model = Newsletter
    template_name = 'my_work/newsletter/newsletter_list.html'
    extra_context = {
        'title': 'Список рассылок'
    }


class NewsletterDetailView(generic.DetailView):
    model = Newsletter
    template_name = 'my_work/newsletter/newsletter_detail.html'


class NewsletterCreateView(generic.CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'my_work/newsletter/newsletter_form.html'
    success_url = reverse_lazy('main:newsletters')

    def form_valid(self, form):
        form.instance.status = 'running'
        response = super().form_valid(form)
        send_newsletter(self.object)
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        message_item = self.object
        message_item.status = 'running'
        message_item.save()
        send_newsletter(message_item)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletters_count'] = Newsletter.objects.count()
        return context


class NewsletterUpdateView(generic.UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'my_work/newsletter/newsletter_update.html'
    success_url = reverse_lazy('my_work:newsletters')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:newsletter_update', kwargs={'pk': pk})


class NewsletterDeleteView(generic.DeleteView):
    model = Newsletter
    template_name = 'my_work/newsletter/newsletter_delete.html'
    success_url = reverse_lazy('main:newsletters')

    def test_func(self):
        return self.request.user.is_superuser
