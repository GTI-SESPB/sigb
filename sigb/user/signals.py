def create_superuser(sender, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            email='admin@ses.local',
            nome='admin',
            password='admin'
        )
