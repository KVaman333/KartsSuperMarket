from django.urls import path, include


urlpatterns = [ #  dashboard/daily-reports/
    path('Scan-Coordinator/', include('reports.urlsPatterns.scUrls')),
]
