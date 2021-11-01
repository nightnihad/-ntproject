from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import  VehicleAddForm,VehicleUpdateForm
from Vehicle.models import Vehicle
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.

class VehicleList(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name ='vehiclelist.html'
    paginate_by = 4

class VehicleDetail(DetailView):
    template_name='vehicledetail.html'
    context_object_name ='vehicle'
    model = Vehicle
    def get_object(self):
        vehicle = get_object_or_404(
            self.model,
            id=self.kwargs.get('id'),
        )
        return vehicle

class VehicleAdd(CreateView):
    template_name = 'vehicleaddform.html'
    form_class = VehicleAddForm

    def get_success_url(self):
        return reverse('vehicledetail',kwargs={
            'id': self.object.id
        })
class VehicleDelete(DeleteView):
    template_name = 'vehicledelete.html'
    success_url = reverse_lazy('vehiclelist')
    def get_object(self):
        vehicle = Vehicle.objects.filter(id=self.kwargs['id'])
        return vehicle

class VehicleUpdate(UpdateView):
    template_name='vehicleupdateform.html'
    form_class=VehicleUpdateForm
    
    def get_success_url(self):
            return reverse('vehicledetail',kwargs={
            'id': self.object.id
        })

    def get_object(self,queryset=None):
        vehicle=Vehicle.objects.filter(id=self.kwargs['id']).first()
        return vehicle