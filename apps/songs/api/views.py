from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import SongSerializer
from ..models import Song


class SongViewSetRO(ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer

    def get_queryset(self):
        qs = self.queryset
        updated_from = self.request.query_params.get('update_from')
        if updated_from is not None:
            updated = datetime.strptime(updated_from, "%d%m%Y").date()
            qs = qs.filter(modified__gte=updated)
        return qs
