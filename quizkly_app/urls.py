from django.urls import path
from django.conf.urls import include
from quizkly_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('contacts/', views.ContactList.as_view()),
    path('contact/<int:pk>/', views.ContactDetail.as_view()),
    # path('users/<int: pk>', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
