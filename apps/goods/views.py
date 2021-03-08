from django.shortcuts import render
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.
from goods.myfilter import GoodsFilter
from goods.models import Goods, GoodsCategory

# class GoodsListView(View):
#     def get(self, request):
#         # 返回前所有商品的前10条数据
#         goods_list = Goods.objects.all()[:10]
#         json_list = []
#         print(goods_list)
#         for goods in goods_list:
#             json_item = {}
#             json_item["name"] = goods.name
#             json_item["market_price"] = goods.market_price
#             json_item["sold_num"] = goods.sold_num
#             # json_item["add_time"] = goods.add_time#该行代码报错
#
#             json_list.append(json_item)
#
#         from django.http import HttpResponse
#         import json
#
#         print(type(json_list))
#         # 转换成字符串
#         content = json.dumps(json_list)
#         # str
#         print(type(content))
#         # ，在转换成json
#         return HttpResponse(content, "application/json")
from goods.serializer import GoodsSerializer, GoodsCategorySerializer


class GoodsListView(APIView):
    """
       返回商品列表页1
       """
    def get(self, request):
        # 返回前所有商品的前10条数据
        goods_list = Goods.objects.all()[:10]
        serializer = GoodsSerializer(goods_list, many=True)
        return Response(serializer.data)


class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
   """
   返回商品列表页
   """
   #得到所有的商品
   queryset = Goods.objects.all()[:10]
   #序列化器
   serializer_class = GoodsSerializer

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

class GoodsListView(generics.ListAPIView):
   """
   返回商品列表页
   """
   #得到所有的商品
   # queryset = Goods.objects.all()[:10]
   queryset = Goods.objects.all()
   #序列化器
   serializer_class = GoodsSerializer

   # def get(self, request, *args, **kwargs):
   #    return self.list(request, *args, **kwargs)


class CategoryResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'p'
    max_page_size = 1000

class CategoryListView(generics.ListAPIView):
   """
   返回商品列表页
   """
   #得到所有的商品
   # queryset = Goods.objects.all()[:10]
   queryset = GoodsCategory.objects.all()
   #序列化器
   serializer_class = GoodsCategorySerializer
   # 分页
   pagination_class = CategoryResultsSetPagination


class CategoryListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
   """
   返回商品列表页
   """
   #得到所有的商品
   # queryset = Goods.objects.all()[:10]
   queryset = GoodsCategory.objects.all()
   #序列化器
   serializer_class = GoodsCategorySerializer
   # 分页
   pagination_class = CategoryResultsSetPagination


class GoodsListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
   """
   返回商品列表页
   """
   #得到所有的商品
   # queryset = Goods.objects.all()[:10]
   queryset = Goods.objects.all()
   # queryset = Goods.objects.filter(name__icontains='茶')
   #序列化器
   serializer_class = GoodsSerializer
   # 分页
   pagination_class = CategoryResultsSetPagination

   def get_queryset(self):
       print('我是get_queryset')
       queryset = self.queryset
       query_c = self.request.query_params.get('name')
       query_price = self.request.query_params.get('price')

       print('query_c',query_c)
       if query_c:
           queryset = queryset.filter(name__icontains=query_c)

       if query_price:
           queryset = queryset.filter(shop_price__gte=query_price)
       return queryset


class GoodsListView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
   """
   返回商品列表页
   """
   #得到所有的商品
   # queryset = Goods.objects.all()[:10]
   queryset = Goods.objects.all()
   # queryset = Goods.objects.filter(name__icontains='茶')
   #序列化器
   serializer_class = GoodsSerializer
   # 分页
   pagination_class = CategoryResultsSetPagination

   filter_backends = (DjangoFilterBackend,)
   # filter_fields = ('name', 'shop_price')

   filter_class =  GoodsFilter