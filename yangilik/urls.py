from django.urls import path


from .views import home,get_yangiliklar,get_yangilik

urlpatterns = [
    path('',home,name='home'),
    path('get_yangiliklar/<int:pk>',get_yangiliklar,name='get_yangiliklar'),
    path('get_yangilik/<int:pk>',get_yangilik,name='get_yangilik')

]