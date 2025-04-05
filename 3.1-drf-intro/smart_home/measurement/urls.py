from django.urls import path
from measurement.views import SensorsViewList, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsViewList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
      
]
