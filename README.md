# Crypto API

A Django-based API for managing cryptocurrency data. This API allows you to list and retrieve information about cryptocurrencies and categories, perform health checks, and view version information.

## Features

- **List and Retrieve Coins**: Access details about all coins or individual coins.
- **List Categories**: Retrieve all cryptocurrency categories.
- **Retrieve Coins by Category**: Get all coins belonging to a specific category.
- **Health Check**: Check the health status of the API.
- **Version Information**: Get the current version and description of the API.

## Requirements

- Python 3.8 or higher
- Django 4.0 or higher
- Django REST Framework 3.14 or higher

## Installation

1. **Clone the Repository**
```
git clone https://github.com/yourusername/crypto-api.git
cd crypto-api
   ```

2. **Create and Activate a Virtual Environment**
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. **Install Dependencies**
```
pip install -r requirements.txt

```
4. **Apply Migrations**
```
python manage.py migrate

```
5. **Create a Superuser**
```
python manage.py createsuperuser

```
6. **Run the Development Server**
```
python manage.py runserver

```
## Running Tests
To run tests, use the following command:
```
coverage run manage.py test
```
To generate the coverage report, use:
```
coverage report
```
For HTML reports, use:
```
coverage html
```

## Docker Support
1. **Build the docker image**
```
docker build -t crypto-api .
```

2. **Run the docker container**
```
docker run -p 8000:8000 crypto-api
```

## Linting and Quality Control
Ensure your code meets quality standards by running:
```
flake8
```

## Coverage report
![Coverage report of 97%](https://drive.google.com/file/d/1anDKtwpEf6MWyTKw2tKp3eIQtFS6MCnS/view?usp=sharing)
