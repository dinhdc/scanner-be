from django.core.management.base import BaseCommand
from faker import Faker

from app.models import School

fake = Faker()


class Command(BaseCommand):
    help = "Create new n schools"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="Number of schools to create")

    def handle(self, *args, **options):
        number_of_schools = options["number"]  # Correctly get the number from options

        try:
            for _ in range(number_of_schools):
                # Create fake school data
                fake_name = fake.company()  # Using company name for school
                code = ''.join([i[0] for i in fake_name.split()])  # Create a code from initials
                School.objects.create(name=fake_name, code=code)

            self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_schools} schools.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
