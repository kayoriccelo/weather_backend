from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S',
                                     input_formats=['%d/%m/%Y', '%Y-%m-%dT%H:%M', '%Y-%m-%d'])
                                     
    class Meta:
        model = History
        fields = '__all__'
