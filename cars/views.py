from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .models import CarModel,CategoryModel

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify your template here
    success_url = reverse_lazy('home')  # Redirect after successful login

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        news_cars_list = CarModel.objects.all().order_by('-publish_time')[:3]
        cars_list = CarModel.objects.all().order_by('-publish_time')
        category_list = CategoryModel.objects.all()

    
        context = {
            'news_cars_list': news_cars_list ,
            'category_list': category_list,
            'cars_list' : cars_list,
        }

        return render(request, 'home.html', context=context)


class CustomLogoutView(LogoutView):
    next_page = 'login'  # Set your next page here


class DetailView(View):
    def get(self, request, pk):
        category_list = CategoryModel.objects.all()
        car_detail = CarModel.objects.get(pk=pk)
        
        context = {
            'category_list': category_list,
            'car_detail': car_detail     
        }
        
        return render(request, 'detail.html', context=context)
