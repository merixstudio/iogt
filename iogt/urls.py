from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from iogt_users import urls as users_urls
from search import views as search_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from home import views as pwa_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),
    path('users/', include(users_urls), name='users_urls'),
    path('accounts/', include('allauth.urls'), name='allauth-urls'),
    path(
        'sw.js',
        pwa_views.ServiceWorkerView.as_view(),
        name=pwa_views.ServiceWorkerView.name,
    ),
    path("test/", include("home.urls"), name="test")
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + [path(r"__debug__/", include(debug_toolbar.urls))]

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
]
