from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.urls import reverse

from .forms import NewListForm
from .models import List


def index(request):
    all_lists = get_list_or_404(List.objects.order_by('name'))
    return render(request, 'lists/index.html', {'all_lists': all_lists})


def list_view(request, list_id):
    lst = get_object_or_404(List, pk=list_id)
    return render(request, 'lists/list_view.html', {'lst': lst})


def new_list(request):
    if request.method == 'POST':
        form = NewListForm(request.POST)
        if form.is_valid():
            lst = List(name=request.POST.get('name'), items="")
            lst.save()
            return redirect('list view', lst.id)
    return HttpResponseRedirect(reverse('index'))


def delete_list(request, list_id):
    if request.method == 'POST':
        lst = get_object_or_404(List, pk=list_id)
        lst.delete()
    return HttpResponseRedirect(reverse('index'))