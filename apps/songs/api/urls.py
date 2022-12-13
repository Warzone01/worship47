from rest_framework import routers
from songs.api.views import SongViewSetRO

router = routers.SimpleRouter()
router.register(r'songs-ro', SongViewSetRO)
urlpatterns = router.urls
