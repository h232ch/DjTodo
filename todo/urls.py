from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),

    path('create/', views.TodoCV.as_view(), name='create'),
    path('list/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete') # <int:pk> 패스컨버터 : 숫자가 들어오면 해당 값을 뷰로 넘겨줌
    
]
