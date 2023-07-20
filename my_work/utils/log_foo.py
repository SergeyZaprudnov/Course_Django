from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from my_work.models import Log
from my_work.services import get_cached_log_data


class LogListView(LoginRequiredMixin, generic.ListView):
    model = Log
    template_name = 'my_work/log/log_list.html'
    extra_context = {
        'title': 'Список логов'
    }


class LogDetailView(generic.DetailView):
    model = Log
    template_name = 'my_work/log/log_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_data'] = get_cached_log_data(self.object)
        return context
