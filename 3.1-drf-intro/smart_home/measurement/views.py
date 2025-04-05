from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

from rest_framework.views import APIView


class SensorsViewList(ListCreateAPIView):
    """ Класс для реализации:
    GET - получить данные
    POST - записать новые данные """

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({'status', 'post - success'})

class SensorView(RetrieveUpdateAPIView):
    """ Класс для реализации:
    GET - получить детальную информацию,
    PATCH - частично обновить данные """

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        elif self.request.method == 'PATCH':
            return SensorSerializer

        return super().get_serializer_class()

    def perform_update(self, serializer):
        serializer.save()


class MeasurementView(CreateAPIView):
    """Класс для добавления измерения"""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer