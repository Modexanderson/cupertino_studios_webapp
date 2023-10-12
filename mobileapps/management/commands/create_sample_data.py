from django.core.management.base import BaseCommand
from mobileapps.models import MobileApp


class Command(BaseCommand):
    help = "Create sample data for mobile apps"

    def handle(self, *args, **kwargs):
        # Create sample mobile apps
        MobileApp.objects.create(
            name="Audify",
            description="A music streaming app.",
            icon="app_icons/audify.png",
            # Add other fields as needed
        )
        MobileApp.objects.create(
            name="Imagen",
            description="A photo editing app.",
            icon="app_icons/imagen.png",
            # Add other fields as needed
        )
        MobileApp.objects.create(
            name="Nyanya",
            description="A recipe app.",
            icon="app_icons/nyanya.png",
            # Add other fields as needed
        )

        self.stdout.write(self.style.SUCCESS("Sample data created successfully."))
