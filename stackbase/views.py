from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Question, Comment
from .forms import CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

#CRUD FUNCTION
class QuestonlistView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

class QuestonDetailView(DetailView):
    model = Question

class QuestonCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuestonUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content']

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class QuestonDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    success_url = '/question/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False

class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question-detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question-detail')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question-answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question-list')