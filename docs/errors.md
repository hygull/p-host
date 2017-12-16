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

OperationalError (If things are not working, you have to try other methods too)

```
delete/rename db.sqlite3
```

```
python3 manage.py migrate
```

