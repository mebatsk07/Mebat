from config.profiles.production import PROFILE


def get_profile():
    return PROFILE

from config.profile_loader import get_profile

profile = get_profile()

print(profile.premium_min)