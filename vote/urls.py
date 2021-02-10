from django.urls import path
from .views import home, DetailView, ResultView, vote

app_name = 'vote'

urlpatterns = [
    path('',home,name='home'),
    path('<int:pk>/',DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',ResultView.as_view(),name='results'),
    path('<int:question_id>/vote/',vote,name='vote'),
]
