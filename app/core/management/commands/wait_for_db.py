"""
Wait command for the database to be ready before starting the application.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Wait for the database to be ready."""
    def handle(self, *args, **options):
        pass

    