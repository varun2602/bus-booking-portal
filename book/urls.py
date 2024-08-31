from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/register/', views.UserRegistrationView.as_view(), name='user_registration'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/search-buses/', views.SearchBusesView.as_view(), name='search_buses'),
    path('api/block-seats/', views.BlockSeatsView.as_view(), name='block_seats'),
    path('api/book-tickets/', views.BookTicketsView.as_view(), name='book_tickets'),
]
