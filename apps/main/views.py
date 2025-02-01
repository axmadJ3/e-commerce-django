from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME - Главная'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME - О нас'
        context['text_on_page'] = 'И о том почему этот магазин класный и т.д.'
        return context


# def index(request):
#     context = {
#         'title': 'HOME - Главная',
#     }
    
#     return render(request, template_name='main\index.html', context=context)


# def about(request):
#     context = {
#         'title': 'HOME - О нас',
#         'text_on_page': 'И о том почему этот магазин класный и т.д.'
#     }
    
#     return render(request, template_name='main\\about.html', context=context)
