#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import root

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todowoo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("Sys Argument:", str(sys.argv))
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    rook.start(token='4825f25e6e246075e7a5bd1f514cca2b6cc47a9e19a9625f0ad95b38419133ac',
               labels={"env":"dev"}) # Optional,see Labels page below Projects
    main()
