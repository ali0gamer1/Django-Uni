from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("", include("daneshgah.urls"))
=======
    path('', include('daneshgah.urls'))
>>>>>>> 408a1e705243924c1b12c477a7020c13628c2d4a
]
