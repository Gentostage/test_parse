from django.views.generic import View
from django.http import JsonResponse

from posts.models import Post


class PostlView(View):

    def get(self, request, *arg, **kwargs):
        try:
            offset = abs(int( request.GET.get("offset", 0)))
        except Exception:
            return JsonResponse({'error':'parametr offset is wrong'}, status=400)
        try:
            limit = abs(int(request.GET.get("limit", 5)))
        except Exception:
            return JsonResponse({'error':'parametr limit is wrong'}, status=400)   
        
        order = request.GET.get("order",'id')
        if order not in [field.name for field in Post._meta.get_fields()]:
            return JsonResponse({'error':'sort by non-existing field'}, status=400)

        data = Post.objects.all().order_by(order)[offset:limit]
        return JsonResponse(list(data.values()), safe=False, status=200)

