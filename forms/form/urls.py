from django.urls import path
from form.views import upload
urlpatterns = [
    path('', upload),
]
