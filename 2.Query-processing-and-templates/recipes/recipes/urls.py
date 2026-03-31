"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from calculator.views import recipe

# Список URL-маршрутов (адресов), которые обрабатывает Django
urlpatterns = [
    # Регистрируем маршрут для обработки запросов

    # '<str:name>/' — это динамический URL:
    # - <str:name> означает, что сюда будет подставляться строка
    # - name — это имя переменной, которая передастся в view
    # - например:
    #   /omlet/  → name = "omlet"
    #   /pasta/  → name = "pasta"

    # recipe — это функция-представление (view), которая будет вызвана,
    # когда пользователь перейдет по данному URL

    # Django:
    # 1. принимает URL от пользователя
    # 2. сопоставляет его с этим шаблоном
    # 3. извлекает параметр name
    # 4. вызывает функцию recipe(request, name)

    path('<str:name>/', recipe)
]
