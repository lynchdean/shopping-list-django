from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .forms import NewListForm
from .models import List


class IndexView(generic.ListView):
    template_name = 'lists/index.html'
    context_object_name = 'all_lists'

    def get_queryset(self):
        return List.objects.order_by('name')


class DetailView(generic.DetailView):
    model = List
    template_name = 'lists/list_detail.html'
    context_object_name = 'list_detail'


def new_list(request):
    if request.method == 'POST':
        form = NewListForm(request.POST)
        if form.is_valid():
            lst = List(name=request.POST.get('name'), items=[])
            lst.save()
            return redirect('list view', lst.id)
    return HttpResponseRedirect(reverse('index'))


def delete_list(request, list_id):
    if request.method == 'POST':
        lst = get_object_or_404(List, pk=list_id)
        lst.delete()
    return HttpResponseRedirect(reverse('index'))


def new_item(request, list_id):
    if request.method == 'POST':
        lst = get_object_or_404(List, pk=list_id)
        lst.items.append(request.POST.get('item name'))
        lst.save()
    return redirect('list view', list_id)


def delete_item(request, list_id, item_idx):
    if request.method == 'POST':
        lst = get_object_or_404(List, pk=list_id)
        lst.items.pop(item_idx)
        lst.save()
    return redirect('list view', list_id)
