from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_create.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_update.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:blogs')


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogPost.objects.filter(is_active=True)  # по положительному признаку публикации


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


def increase_views(request, post_id):
    try:
        blog_post = BlogPost.objects.get(pk=post_id)
        blog_post.views += 1
        blog_post.save()
        return JsonResponse({'status': 'success', 'views': blog_post.views})
    except BlogPost.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Blog post not found'}, status=404)
