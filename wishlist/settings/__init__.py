import os

if os.getenv('HEROKU') is not None:
    from .production import *
elif os.getenv('CI') is not None:
    from .testing import *
else:
    from .development import *
