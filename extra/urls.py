from django.urls import path

# from .views import my_view, MyView, gallery_view
from .views import gallery_view



app_name = "extra"
urlpatterns = [
    # path(' ', my_view, name="my_view"),
#     path('class-based/', MyView.as_view(), name="another_view"),
    path("gallery/", gallery_view, name="gallery")
 ]