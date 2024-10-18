from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from .models import Item


class ItemListView(View):
    template_name = "item_list.html"
    paginate_by = 5

    def get(self, request):
        sort_by = request.GET.get("sort", "name")
        items = Item.objects.all().order_by(sort_by)
        paginator = Paginator(items, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj,
            "sort": sort_by,
        }
        return render(request, self.template_name, context)
