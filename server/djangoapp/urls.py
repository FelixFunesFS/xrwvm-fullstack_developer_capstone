from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "djangoapp"

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.registration, name="register"),

    # path for dealer reviews view
    # path("dealer/<int:dealer_id>/reviews", views.get_dealer_reviews, name="dealer_reviews"),

    # path for add a review view
    # path("review", views.add_review, name="add_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
