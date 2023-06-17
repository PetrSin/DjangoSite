from django.utils.cache import patch_cache_control

class DisableCachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Отключение заголовков кэширования
        patch_cache_control(response, no_cache=True)
        
        return response
    