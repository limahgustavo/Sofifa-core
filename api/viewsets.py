from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api import models, actions
from api import serializers


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

    @action(detail=False, methods=['GET'])
    def get_data_from_excel_file(self, request, *args, **kwargs):
        data = actions.ExtractExcelData()
        data.import_data()
        return Response(data={'detail': True})
