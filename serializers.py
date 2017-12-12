from marshmallow import Serializer, fields


class HeartBeatSerializer(Serializer):

    class Meta:
        fields = ("id", "timestamp")
