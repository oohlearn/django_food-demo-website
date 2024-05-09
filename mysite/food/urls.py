from django.urls import path
from . import views


app_name = "food"
# 如果在這裡有使用命名空間的話，在使用動態url的時候，要變成【app_name】:【name】

urlpatterns = [ 
    path('', views.ItemListView.as_view(), name='index'),
    # /food/2
    path("<int:pk>/", views.ItemDetailView.as_view(), name="detail"),
    # food/add
    path("add/", views.ItemCreateView.as_view(), name="create_item"),
    # food/edit
    path("edit/<int:pk>", views.ItemUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", views.ItemDeleteView.as_view(), name="delete"),
    ]

