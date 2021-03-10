from django.utils.deprecation import MiddlewareMixin
class Middle1(MiddlewareMixin):
    def process_request(self,request):
        print("来了")
    def process_response(self, request,response):
        print('走了')
        return response