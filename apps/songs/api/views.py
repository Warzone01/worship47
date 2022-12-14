from datetime import datetime

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.db.models import QuerySet

from ..models import Song
from .serializers import SongSerializer


class SongViewSetRO(ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer

    def get_queryset(self) -> QuerySet:
        qs = self.queryset
        updated_from = self.request.query_params.get('update_from')
        if updated_from is not None:
            updated = datetime.strptime(updated_from, "%d%m%Y").date()
            qs = qs.filter(modified__gte=updated)
        return qs
