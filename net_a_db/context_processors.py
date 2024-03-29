from .models import UserProfile
#全画面に適用
def user_profile(request):
    if request.user.is_authenticated:
        user_profile_instance = UserProfile.objects.filter(user=request.user).first()
        return {'user_profile': user_profile_instance}
    return {'user_profile': None}
