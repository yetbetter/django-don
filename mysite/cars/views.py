from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView

from cars.forms import CarForm
from cars.models import Car


class CarListView(LoginRequiredMixin, ListView):
    model = Car

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset


class CarCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Car
    form_class = CarForm
    success_message = 'Автомобиль создан!'
    success_url = reverse_lazy('car-list')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateOnlyOwnerMixin:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user_id == request.user.id:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        raise Http404()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user_id != request.user.id:
            raise Http404()

        form = self.get_form()

        if form.is_valid():
            self.object.number = request.POST['number']
            self.object.mark = request.POST['mark']
            self.object.model = request.POST['model']
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CarUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateOnlyOwnerMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('car-list')
    success_message = 'Автомобиль обновлен!'


class DeleteOnlyOwnerMixin:
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user_id == request.user.id:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        else:
            raise Http404()


class CarDeleteView(LoginRequiredMixin, DeleteOnlyOwnerMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('car-list')


class CarSearchView(LoginRequiredMixin, View):
    model = Car

    def get(self, request):
        if self.request.GET:
            number = self.request.GET['number']
        else:
            number = ''

        car = self.model.objects.filter(number=number).first()

        context = {'car': car}

        return render(request, 'cars/car_search.html', context)




