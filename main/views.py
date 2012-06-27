# Create your views here.
from forms import SSLForm
from models import SSL
from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    data = SSL.objects.all()
    if request.method == 'POST': # If the form has been submitted...
        form = SSLForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = SSLForm() # An unbound form
        #import pdb;pdb.set_trace()

    return render(request, 'main.html', {
        'form': form,
        'start': [1,5,9],
        'end': [4,8,12],
        'data': data,
    })

def delete(request, id_entry = None):
    if id_entry:
        SSL.objects.filter(id=id_entry).delete()
        return HttpResponseRedirect('/')
    else:
        HttpResponseRedirect('/')


