### 1

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("demo/", include("pmt_hostel_site.urls")),
]
```

Error

```
...
...
...
RecursionError: maximum recursion depth exceeded
```

Fix it as follows

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("demo/", include("pmt_hostel_app.urls")),
]
```

### 2