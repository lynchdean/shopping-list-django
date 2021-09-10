from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.urls import reverse
import json

from .forms import NewListForm
from .models import List


def index(request):
    all_lists = List.objects.order_by('name')
    return render(request, 'lists/index.html', {'all_lists': all_lists})


def list_view(request, list_id):
    lst = get_object_or_404(List, pk=list_id)
    return render(request, 'lists/list_view.html', {'lst': lst})


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