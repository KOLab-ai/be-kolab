from django.core.management.base import BaseCommand
from influencers.methods import proccess_influencer_data


class Command(BaseCommand):
    help = 'Import influencers from JSON file'

    def handle(self, *args, **options):
        self.stdout.write('Starting influencer import...')
        
        try:
            proccess_influencer_data()
            self.stdout.write(
                self.style.SUCCESS('Successfully completed influencer import!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during import: {str(e)}')
            )
