#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "privstor.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    # Check private storage and create directory if necessary
    from django.conf import settings
    print('private storage location: {}'.format(settings.PRIVATE_STORAGE_ROOT))
    if not os.path.isdir(settings.PRIVATE_STORAGE_ROOT):
        os.mkdir(settings.PRIVATE_STORAGE_ROOT)
        print("private storage directory created")

    execute_from_command_line(sys.argv)
