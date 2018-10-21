from django.urls import path

from cars.views import CarListView, CarCreateView, CarDeleteView, CarUpdateView, CarSearchView

urlpatterns = [
    path('list', CarListView.as_view(), name='car-list'),
    path('create', CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/update', CarUpdateView.as_view(), name='car-update'),
    path('<int:pk>/delete', CarDeleteView.as_view(), name='car-delete'),
    path('search', CarSearchView.as_view(), name='car-search')
]