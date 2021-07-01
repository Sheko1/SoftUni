from notes.profile_app.models import Profile


def get_profile():
    profile = Profile.objects.first()
    return profile
