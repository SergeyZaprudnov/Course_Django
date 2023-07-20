from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from my_work.forms import MessageForm
from my_work.models import Message


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'my_work/messages/messaje_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'my_work/messages/message_detail.html'
    success_url = reverse_lazy('my_work:messages')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('my_work:message_update', kwargs={'pk': pk})


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'my_work/messages/message_form.html'
    success_url = reverse_lazy('my_work:messages')


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = 'my_work/messages/message_delete.html'
    success_url = reverse_lazy('my_work:messages')

    def test_func(self):
        return self.request.user.is_superuser
