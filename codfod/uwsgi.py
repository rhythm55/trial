import os
import sys

sys.path.append('/usr/lib/python3/dist-packages')

## assuming your django settings file is at '/var/www/project/project/settings.py'
mypath = '/home/ubuntu/trial/'
if mypath not in sys.path:
    sys.path.append(mypath)

os.environ['DJANGO_SETTINGS_MODULE'] = 'codfod.settings'

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()
