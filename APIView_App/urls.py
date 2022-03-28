
from django.urls import path,include

from APIView_App import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', views.Employee_ModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('employees/', views.EmployeeListView.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
]
