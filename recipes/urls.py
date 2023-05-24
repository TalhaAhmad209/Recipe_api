from django.urls import path
from .views import RecipeListCreateAPIView, RecipeRetrieveAPIView, RecipeDestroyAPIView

urlpatterns = [
    path('recipes/', RecipeListCreateAPIView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveAPIView.as_view(), name='recipe-retrieve'),
    path('recipes/<int:pk>/delete/', RecipeDestroyAPIView.as_view(), name='recipe-delete'),
]

