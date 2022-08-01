from django.shortcuts import render
from .models import Game
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class GameListView(ListView):
  template_name = 'games/game_list.html'
  model = Game

class GameDetailView(DetailView):
  template_name = 'games/game_detail.html'
  model = Game

class GameCreateView(CreateView):
  template_name = 'games/game_create.html'
  model = Game
  fields = ['title', 'developer', 'description']

class GameUpdateView(UpdateView):
  template_name = 'games/game_update.html'
  model = Game
  fields = ['title', 'developer', 'description']

class GameDeleteView(DeleteView):
  template_name = 'games/game_delete.html'
  model = Game
  success_url = reverse_lazy('game_list')



