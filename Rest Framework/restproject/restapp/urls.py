"""
URL configuration for restproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
 
    path('students/',StudentAPI.as_view()),
    path('products/',ProductAPI.as_view()),
    path('category/',CategoryAPI.as_view()),
    path("register/",RregisterUser.as_view()),    
    path('author/',AuthorAPI.as_view()),
    path('publisher/',PublisherAPI.as_view()),
    path("book/",BookAPI.as_view()),
    path('country/',CountryAPI.as_view()),
    path('state/',StateAPI.as_view()),
    path("city/",CityAPI.as_view()),
    path("area/",AreaAPI.as_view()),
    path("register/",RregisterUser.as_view()),
    path("age/",AgeAPI.as_view()),
    path('people/', PersonCreate.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getaccesstoken/', GetAccessTokenView.as_view(), name='get-access-token'),
     # path('addStudent',views.add_student),
    # path('updateStudent/<id>',views.update_student),
    # path('deleteStudent/<id>',views.delete_student)
    #   path("book-generic/",BookAPIGeneric1.as_view(),name="bookgeneric"),
    # path("book-generic/<id>",BookAPIGeneric.as_view(),name="bookgeneric1")
]
