# AirBnB Clone

## Description
This project is a clone of the AirBnB web application built using Python. It provides a command-line interface for managing various entities like users, places, states, cities, amenities, and reviews.

## Command Interpreter

### How to Start
To start the command interpreter, run:
```bash
./console.py
```

### How to Use
The command interpreter provides an interactive shell with the following commands:

- `create <class_name>` - Creates a new instance of the specified class
- `show <class_name> <id>` - Displays the string representation of an instance
- `destroy <class_name> <id>` - Deletes an instance based on class name and id
- `all [class_name]` - Lists all instances or instances of a specific class
- `update <class_name> <id> <attribute_name> "<attribute_value>"` - Updates an instance attribute
- `quit` or `EOF` - Exits the program
- `help` - Shows available commands

### Examples

#### Creating a new BaseModel instance:
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

#### Showing an instance:
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

#### Listing all instances:
```bash
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

#### Updating an instance:
```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
```

#### Creating a User:
```bash
(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
```

## Project Structure
```
alu-AirBnB_clone/
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   ├── test_base_model.py
│   │   ├── test_user.py
│   │   ├── test_state.py
│   │   ├── test_city.py
│   │   ├── test_amenity.py
│   │   ├── test_place.py
│   │   └── test_review.py
│   └── test_engine/
│       ├── __init__.py
│       └── test_file_storage.py
├── console.py
├── file.json
├── README.md
└── AUTHORS
```

## Classes

### BaseModel
The base class for all other classes in the project. Provides common attributes and methods:
- `id`: Unique identifier (UUID4)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `save()`: Updates the `updated_at` attribute
- `to_dict()`: Returns dictionary representation

### User
Represents a user in the system:
- `email`: User's email address
- `password`: User's password
- `first_name`: User's first name
- `last_name`: User's last name

### State
Represents a state:
- `name`: State name

### City
Represents a city:
- `state_id`: ID of the state the city belongs to
- `name`: City name

### Amenity
Represents an amenity:
- `name`: Amenity name

### Place
Represents a place to stay:
- `city_id`: ID of the city
- `user_id`: ID of the user who owns the place
- `name`: Place name
- `description`: Place description
- `number_rooms`: Number of rooms
- `number_bathrooms`: Number of bathrooms
- `max_guest`: Maximum number of guests
- `price_by_night`: Price per night
- `latitude`: Latitude coordinate
- `longitude`: Longitude coordinate
- `amenity_ids`: List of amenity IDs

### Review
Represents a review:
- `place_id`: ID of the place being reviewed
- `user_id`: ID of the user who wrote the review
- `text`: Review text

## Storage
The project uses JSON file storage for persistence. All instances are automatically saved to `file.json` when created, updated, or deleted.

## Testing
Run the test suite with:
```bash
python3 -m unittest discover tests
```
