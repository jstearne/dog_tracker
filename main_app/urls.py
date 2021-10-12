from django.urls import path, include
from . import views


urlpatterns = [ 
    path('', views.Home.as_view(), name="home"), # index
    path('dogs/', views.DogList.as_view(), name="dog_list"), # new home page
    path('about/', views.About.as_view(), name="about"),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('dogs/new/', views.DogCreate.as_view(), name="dog_create"),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name="dog_delete"),
    path('contact_us/', views.ContactUs.as_view(), name="contact_us"),
    # DOESN'T WORK path('admin/', admin.site.urls),
    # path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]


  # path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),