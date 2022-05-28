from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),

    #CRUD FUNCTION
    path('question/', views.QuestonlistView.as_view(), name="question-list"),
    path('question/new', views.QuestonCreateView.as_view(), name="question-create"),
    path('question/<int:pk>/', views.QuestonDetailView.as_view(), name="question-detail"),
    path('question/<int:pk>/update/', views.QuestonUpdateView.as_view(), name="question-update"),
    path('question/<int:pk>/delete/', views.QuestonDeleteView.as_view(), name="question-delete"),
    path('question/<int:pk>/comment/', views.AddCommentView.as_view(), name="question-comment"),
]
