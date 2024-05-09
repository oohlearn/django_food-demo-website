from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # 索引原則:  【app名稱】【manager】【方法名稱】
    context = {
        'item_list': item_list,
    }
    return render(request, "food/index.html", context)
# render裡面放的兩個參數，順序不能改，會出錯


class ItemListView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


class ItemDetailView(DetailView):
    model = Item
    template_name = "food/detail.html"


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
    }
    return render(request, "food/detail.html", context)


class ItemCreateView(CreateView):
    model = Item
    template_name = "food/item_form.html"
    form_class = ItemForm
    # 如果沒有下面這塊def，user_name就不會存到資料，因為表單也沒有這格可以填
    # model也沒有相關設定
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    success_url = "/food/"


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "food/item_form.html"
    form_class = ItemForm
    success_url = "/food/"


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "food/item_delete.html"
    success_url = "/food/"

def create_item(request):
    form = ItemForm(request.POST)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item_form.html", context)


def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item_form.html", {'form': form, 'item': item})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/item_delete.html", {"item": item})
