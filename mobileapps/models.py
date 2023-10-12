from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    app = models.ForeignKey(
        "MobileApp", related_name="review_entries", on_delete=models.CASCADE
    )
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    )
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.app.name} by {self.user.username}"


class MobileApp(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    icon = models.URLField(
        max_length=200,
    )
    app_image = models.URLField(
        max_length=200,
    )
    highlightsIcon1 = models.CharField(
        max_length=30,
    )
    highlightsIcon2 = models.CharField(
        max_length=30,
    )
    highlightsIcon3 = models.CharField(
        max_length=30,
    )

    highlightsTitle1 = models.CharField(
        max_length=30,
    )
    highlightsTitle2 = models.CharField(
        max_length=30,
    )
    highlightsTitle3 = models.CharField(
        max_length=30,
    )

    highlightsDescrition1 = models.TextField()
    highlightsDescrition2 = models.TextField()
    highlightsDescrition3 = models.TextField()

    phoneImage = models.URLField(
        max_length=200,
    )
    privacyPolicyUrl = models.URLField(
        max_length=200,
    )
    shortDescription = models.CharField(
        max_length=30,
    )

    playStoreUrl = models.URLField(
        blank=True,
        null=True,
    )
    appGalleryUrl = models.URLField(
        blank=True,
        null=True,
    )
    featureImage = models.URLField(
        max_length=200,
    )

    installs = models.CharField(
        max_length=10,
    )
    rating = models.CharField(
        max_length=10,
    )
    whatsNew = models.CharField(
        max_length=200,
    )
    dataSafety = models.CharField(
        max_length=200,
    )
    shortIDescription = models.CharField(
        max_length=200,
    )
    longDescription = models.TextField(
        max_length=1000,
    )
    category = models.CharField(
        max_length=20,
    )

    # screenshots = models.ManyToManyField("Screenshot")
    # reviews = models.ManyToManyField("Review")
    # screenshots = models.ManyToManyField(Screenshot, blank=True)
    screenshots = models.TextField(
        blank=True, help_text="Enter screenshot URLs separated by newlines"
    )
    version = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    os_logos = models.JSONField(
        default=dict,
    )  # Dictionary to store OS logos
    reviews = models.ManyToManyField(
        Review,
        blank=True,
    )
    android_download_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    ios_download_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    windows_download_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    macos_download_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    linux_download_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    # os_logos = models.JSONField(default=dict)
    # Add any other fields you need, such as release date, developer info, etc.

    def __str__(self):
        return self.name


class UserAppSelection(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming you have a User model for authentication
    selected_os = models.CharField(
        max_length=10, choices=[("iOS", "iOS"), ("Android", "Android")]
    )

    app = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
