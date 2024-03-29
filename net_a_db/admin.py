from django.contrib import admin
from .models import UserInfo
from .models import FishInfo
from .models import Favorite
from .models import History
from .models import Icon
from .models import FishPhoto
from .models import Profile

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(FishInfo)
admin.site.register(Favorite)
admin.site.register(History)
admin.site.register(Icon)
admin.site.register(FishPhoto)
admin.site.register(Profile)
