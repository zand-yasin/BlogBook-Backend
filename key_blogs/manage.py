#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from colorama import Fore, Style


def main():
    print(Fore.MAGENTA, Style.BRIGHT, '\n\b\b[#]', Fore.RED, 'Starting Server', Style.RESET_ALL)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'key_blogs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, 'Stopping Server', Style.RESET_ALL)


if __name__ == '__main__':
    main()
