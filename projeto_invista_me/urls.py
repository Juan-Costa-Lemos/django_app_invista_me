"""projeto_invista_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    #path('', views.pagina_inicial),
    path('', views.meus_investimentos,name='meus_investimentos'),
    path('/<int:id_investimento>',views.detalhe,name='detalhe'),
    path('contato/', views.pagina_contato, name='contato'),
    path('minha_historia/', views.minha_historia, name='minha_historia'),
    path('admin/', admin.site.urls),
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>',views.editar,name='editar'),
    path('confirmar_exclusao/<int:id_investimento>',views.excluir,name='excluir')
]
