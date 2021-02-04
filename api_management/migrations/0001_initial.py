from django.db import migrations
from api_management.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(name="abhinav",email="amazed.abhi15@gmail.com",
                is_staff=True,
                is_superuser=True,
                is_active=True,
                phone="7834853995",
                gender="Male")
        
        user.set_password("12345")
        user.save()

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]