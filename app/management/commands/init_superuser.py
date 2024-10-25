from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = "Create new superuser"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Username for the superuser")
        parser.add_argument("password", type=str, help="Password for the superuser")

    def handle(self, *args, **options):
        username = options['username'][0]  # Get the username
        password = options['password'][0]  # Get the password

        try:
            user = User.objects.create_superuser(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
