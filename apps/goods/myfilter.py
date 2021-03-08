from django_filters import rest_framework as filters
from .models import Goods


# 商品的过滤器
class GoodsFilter(filters.FilterSet):
    # 最低价格
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    # # # 最大价格
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Goods
        fields = ['name', 'min_price', 'max_price']
