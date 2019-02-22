from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    path('snippetz/', views.SnippetList.as_view()),
    path('snippetz/<int:pk>/', views.SnippetDetail.as_view()),

    path('snippetzz/', views.SnippetListz.as_view()),
    path('snippetzz/<int:pk>/', views.SnippetDetailz.as_view()),

    path('snippetx/', views.SnippetListz.as_view()),
    path('snippetx/<int:pk>/', views.SnippetDetailz.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
