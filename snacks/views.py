from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
   template_name ='snack-list.html'
   model = Snack

class SnackDetailView(DetailView):
  template_name = 'snack-detail.html'
  model = Snack
  content_object_name = 'snack-detail'

class SnackCreateView(CreateView):
	template_name = 'snack-create.html'
	model = Snack
	fields = ['name', 'purchaser', 'description']
class SnackUpdateView(UpdateView):
	template_name = 'snack-update.html'
	model = Snack
	fields = ['name', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
	template_name = 'snack-delete.html'
	model = Snack
	success_url = reverse_lazy('snack-list')
