from django.views.generic import DetailView
from django.http import JsonResponse

from posts.models import Post


class PostDetailView(DetailView):
    """"""

    def get(self, request, *arg, **kwargs):
        """"""
        try:
            offset = abs(int( request.GET.get("offset", 0)))
            limit = abs(int(request.GET.get("limit", 5)))
            order = request.GET.get("order",'id')
            data = Post.objects.all().order_by(order)[offset:limit]
        except Exception:
            return JsonResponse({'error':'bad request parameters'})

        return JsonResponse(list(data.values()), safe=False)

