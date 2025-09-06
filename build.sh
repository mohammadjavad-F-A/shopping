 Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
python manage.py migrate
# Convert static asset files
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
