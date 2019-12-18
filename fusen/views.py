from django.shortcuts import render,redirect
from .models import Fusen
from django.shortcuts import get_object_or_404
from .forms import FusenForm
from django.views.decorators.http import require_POST

def index(request):
  fusens = Fusen.objects.all().order_by('-updated_datetime')
  return render(request, 'fusen/index.html', { 'fusens': fusens })

def detail(request, fusen_id):
  fusen = get_object_or_404(Fusen, id=fusen_id)
  return render(request, 'fusen/detail.html', {'fusen': fusen})

def new_fusen(request):
  form = FusenForm
  return render(request, 'fusen/new_fusen.html', {'form': form})
  if request.method == "POST":
    form = FusenForm(request.POST)
    if form.is_vaild():
      return redirect('app:index')
    else:
      form = FusenForm
    return render(request, 'app/new_fusen.gtml', {'form': form})

@require_POST
def delete_fusen(request, fusen_id):
  fusen = get_object_or_404(Fusen, id=fusen_id)
  fusen.delete()
  return redirect('fusen:index')
                        
def edit_fusen(request, fusen_id):
   fusen = get_object_or_404(Fusen, id=fusen_id)
   form = FusenForm(instance=fusen)
   return render(request, 'fusen/edit_fusen.html', {'form': form, 'fusen':fusen })
   if request.method == "POST":
      form = FusenForm(request.POST, instance=fusen)
      if form.is_valid():
        form.save()
        return redirect('fusen:index')
      else:
        form = FusenForm(instance=fusen)
      return render(request, 'fusen/edit_fusen.html', {'form': form, 'fusen':fusen })
