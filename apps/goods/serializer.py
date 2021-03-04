from rest_framework import serializers


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     # 点击数
#     click_num = serializers.IntegerField(default=0)
#     # 销售量
#     sold_num = serializers.IntegerField(default=0)
#     # 封面，自动帮我在图片的路径前面加上media
#     goods_fron_image = serializers.ImageField(default="")
#     add_time = serializers.DateTimeField()
#     # is_new = serializers.BooleanField()
#     is_new = serializers.IntegerField()
from goods.models import Goods, GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
   class Meta:
      #Model
      model = GoodsCategory
      #把所有的属性都用上的写法
      fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        # fields = ['name', 'is_new']
        fields = '__all__'


class GoodsCreatSerializer(serializers.ModelSerializer):
    # category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        # fields = ['name', 'is_new']
        fields = '__all__'