from django.urls import path
from .views import GameCreateView, GameDeleteView, GameDetailView, GameListView, GameUpdateView

urlpatterns = [
    path('game/', GameListView.as_view(), name='game_list'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('game/create/', GameCreateView.as_view(), name='game_create'),
    path('game/<int:pk>/update', GameUpdateView.as_view(), name='game_update'),
    path('game/<int:pk>/delete', GameDeleteView.as_view(), name='game_delete'),
]
