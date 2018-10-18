from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Taco
from .forms import TacoAddForm

def index(request):
    context = {}
    tacos = map(lambda x: {'id': x.id, 'description': x.__str__}, Taco.objects.all())
    context['tacos'] = tacos
    context['add_form'] = TacoAddForm()
    return render(request, 'taquito/index.html', context)

def delete(request, id=None):
    instance = get_object_or_404(Taco, id=id)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('index')

def add(request):
    add_form = TacoAddForm(request.POST)
    if add_form.is_valid():
        shell = add_form.cleaned_data['shell']
        base_layer = add_form.cleaned_data['base_layer']
        mixin = add_form.cleaned_data['mixin']
        condiment = add_form.cleaned_data['condiment']
        seasoning = add_form.cleaned_data['seasoning']
        t = Taco.create(shell, base_layer, mixin, condiment, seasoning)
        t.save()
        messages.success(request, 'Your taco was successfully added')
    return redirect('index')

def add_random(request):
    t = Taco.create_random()
    t.save()
    messages.success(request, 'Your random taco was successfully added')
    return redirect('index')