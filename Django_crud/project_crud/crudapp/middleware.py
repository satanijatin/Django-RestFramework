from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        user = request.user
        if user.is_authenticated:
            pass
            # return HttpResponse(status=200)
        else:
            login_exempt_views = ['login', 'signup']  # Add your views here

            # Check if the requested view is exempt from login
            if not any(view in request.path for view in login_exempt_views):

                redirect_url = reverse('login')
                return redirect(redirect_url)

        response = self.get_response(request)
        return response