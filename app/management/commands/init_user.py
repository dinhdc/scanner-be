from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


fake = Faker()


class Command(BaseCommand):
    help = "Create new n users"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="Number of users to create")

    def handle(self, *args, **options):
        number_of_schools = options["number"]  # Correctly get the number from options

        try:
            for _ in range(number_of_schools):
                username = fake.user_name()
                password = fake.password()
                first_name = fake.first_name()
                last_name = fake.last_name()
                email = fake.email()
                User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                         last_name=last_name)

            self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_schools} users.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
