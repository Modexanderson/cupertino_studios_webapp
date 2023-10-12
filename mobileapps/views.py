from django.shortcuts import redirect, render, get_object_or_404

from .models import MobileApp


# Create your views here.
def index(request):
    # Fetch featured apps or other data you want to display on the homepage
    featured_apps = MobileApp.objects.all()[:3]  # Example: Fetch the first 3 apps
    return render(request, "mobileapps/index.html", {"featured_apps": featured_apps})


def app_list(request):
    apps = MobileApp.objects.all()
    return render(request, "mobileapps/app_list.html", {"apps": apps, "is_app_list_page": True})


def app_detail(request, app_id, os):
    app = get_object_or_404(MobileApp, pk=app_id)
    screenshots = [url.strip() for url in app.screenshots.split("\n") if url.strip()]
    reviews = app.reviews.all()
    
    # Get the download link for the selected OS
    download_link = getattr(app, f'{os.lower()}_download_link', None)
    return render(
        request,
        "mobileapps/app_detail.html",
        {"app": app, "screenshots": screenshots, "reviews": reviews, "os": os,  "download_link": download_link, "is_app_detail_page": True},
    )


def os_selection(request, app_id):
    app = get_object_or_404(MobileApp, id=app_id)
    os_logos = app.os_logos
    return render(
        request, "mobileapps/os_selection.html", {"os_logos": os_logos, "app": app, "is_os_selection_page": True}
    )


# def os_selection(request, app_id):
#     app = get_object_or_404(MobileApp, id=app_id)

#     if request.method == "POST":
#         form = OSSelectionForm(request.POST)
#         if form.is_valid():
#             user_selection = form.save(commit=False)
#             user_selection.user = request.user  # Assign the current user
#             user_selection.app = app
#             user_selection.save()
#             return redirect(
#                 "app_detail", app_id=app_id
#             )  # Redirect to the app detail page
#     else:
#         form = OSSelectionForm()

#     return render(request, "mobileapps/os_selection.html", {"form": form, "app": app})
