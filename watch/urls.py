from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/hood/', views.IndividualHood.as_view(), name='neighborhood'),
    path('api/business/',views.IndividualBusiness.as_view(),name='business'),
    path('api/users/',views.IndividualUser.as_view(),name='users'),
    path('api/profile/',views.IndividualProfile.as_view(),name='profile'),

    #Update
    path('api/hood/update/<int:pk>/',views.NeighborhoodList.as_view()),
    path('api/business/update/<int:pk>/',views.BusinessList.as_view()),
    path('api/users/update/<int:pk>/',views.UserList.as_view(),name='users'),
    path('api/profile/update/<int:pk>/',views.ProfileList.as_view(),name='profile'),

    #Delete
    path('api/hood/delete/<int:pk>/',views.NeighborhoodList.as_view()),
    path('api/business/delete/<int:pk>/',views.BusinessList.as_view()),
    path('api/users/delete/<int:pk>/',views.UserList.as_view(),name='users'),
    path('api/profile/delete/<int:pk>/',views.ProfileList.as_view(),name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

