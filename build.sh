 Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
python manage.py migrate
# Convert static asset files
python manage.py createsuperuser --no-input
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
