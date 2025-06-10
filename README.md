# Fitness Booking API

A Django REST API for managing fitness classes, booking slots, and retrieving user bookings.

##  Features

List all upcoming fitness classes
Book a slot in a fitness class
View bookings by user email
Cancel a booking
Auto-updates available slots
Prevents overbooking

## Setup Instructions

### Prerequisites

Python 3.9+
pip

### Installation
```bash
# Clone the repository
git clone https://github.com/khuntia1994/fitness_project.git
cd fitness_project

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# (Optional) Load seed data
python manage.py shell < seed.py

# Run the development server
python manage.py runserver

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/classes/` | GET | Get all upcoming fitness classes |
| `/api/bookings/` | POST | Book a slot in a class |
| `/api/bookings/<email>/` | GET | Get bookings by email |
| `/api/bookings/<id>/` | DELETE | Cancel a booking |


## Sample cURL Requests

### View All Upcoming Classes

bash
curl http://127.0.0.1:8000/api/classes/

###  Book a Class

bash


### View Bookings by Email

bash
curl -X POST http://127.0.0.1:8000/api/book/ -H "Content-Type: application/json" -d "{\"Class_Id\": 1, \"Client_name\": \"sumanta\", \"Client_email\": \"sumanta@example.com\"}"

curl -X POST http://127.0.0.1:8000/api/book/ -H "Content-Type: application/json" -d "{\"Class_Id\": 2, \"Client_name\": \"sumanta\", \"Client_email\": \"sumanta@example.com\"}"


curl http://127.0.0.1:8000/api/bookings/john@example.com/


### Cancel a Booking

bash
curl -X DELETE http://127.0.0.1:8000/api/bookings/1/

curl -X DELETE http://127.0.0.1:8000/api/cancel/29/ 

## Project Structure

fitness_project/
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── seed.py
├── fitness_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt


##  Contact

For any queries, contact [sumantakhuntia@gmail.com](mailto:sumantakhuntia@gmail.com)
