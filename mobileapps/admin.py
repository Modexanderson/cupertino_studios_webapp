from django import forms
from django.contrib import admin
from .models import MobileApp


@admin.register(MobileApp)
class MobileAppAdmin(admin.ModelAdmin):
    list_display = ("name", "version", "release_date")

    fieldsets = (
        (
            "App Information",
            {
                "fields": (
                    "name",
                    "description",
                    "icon",
                    "app_image",
                    "highlightsIcon1",
                    "highlightsIcon2",
                    "highlightsIcon3",
                    "highlightsTitle1",
                    "highlightsTitle2",
                    "highlightsTitle3",
                    "highlightsDescrition1",
                    "highlightsDescrition2",
                    "highlightsDescrition3",
                    "phoneImage",
                    "privacyPolicyUrl",
                    "shortDescription",
                    "playStoreUrl",
                    "appGalleryUrl",
                    "featureImage",
                    "installs",
                    "rating",
                    "dataSafety",
                    "shortIDescription",
                    "longDescription",
                    "category",
                    "screenshots",
                    "version",
                    "release_date",
                    "os_logos",
                    "reviews",
                ),
            },
        ),
        (
            "OS Download Links",
            {
                "fields": (
                    "android_download_link",
                    "ios_download_link",
                    "windows_download_link",
                    "macos_download_link",
                    "linux_download_link",
                ),
            },
        ),
    )


# admin.site.register(MobileApp)
