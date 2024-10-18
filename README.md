# Item Management Application

This is a basic Django application that allows users to manage items. Users can create, view, sort, and paginate items.

## Features

- Add items via the Django admin interface
- View list of items with pagination
- Sort items by name, price, or creation date

## Requirements

- Python 3.x
- Django 5.x or later

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ananthu303/Item-Project.git
   cd ItemProject

2. Create a virtual environment and activate it:

    python -m venv venv

    # On macOS/Linux : `source venv/bin/activate`  
    
    # On Windows : `venv\Scripts\activate`

3. Install the required packages:

    pip install -r requirements.txt

4. Run the migrations:

    python manage.py makemigrations
    python manage.py migrate

5. Create a superuser to access the admin site:

    python manage.py createsuperuser

6. Run the development server:

    python manage.py runserver

    
# Usage
Access the admin panel at `http://127.0.0.1:8000/admin/` using superuser credentials and add items.

Open your browser and navigate to `http://127.0.0.1:8000/`

Use the sorting options provided in the UI to sort items.
