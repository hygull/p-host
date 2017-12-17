```
WARNINGS:
?: (urls.W002) Your URL pattern '/' [name='index'] has a route beginning with a '/'. Remove this slash as it is unnecessary. If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.

```

Reason

```
from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("demo/", include("pmt_hostel_app.urls")),
    
    path("", include("pmt_hostel_app.urls")),
]
```

```
# URLconf file named urls.py

from django.urls import path
from . import views


urlpatterns = [
	path("/", views.index, name="index")
]
```

Solution

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("demo/", include("pmt_hostel_app.urls")),
    
    path("/", include("pmt_hostel_app.urls")),
]
```

```
# URLconf file named urls.py

from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name="index")
]
```


But both the above are wrong, 404 page

```
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/
Using the URLconf defined in pmt_hostel_site.urls, Django tried these URL patterns, in this order:

admin/
/
The empty path didn't match any of these.

You're seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
```

Final fix to do to visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and see it working

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("demo/", include("pmt_hostel_app.urls")),
    
    path("", include("pmt_hostel_app.urls")),
]
```

```
# URLconf file named urls.py

from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name="index")
]
```
