# RealChat - A Django Real-Time Chat Web Application Using Websockets 

RealChat is a Django-based real-time chat web application that utilizes websockets for instant messaging. This README provides an overview of the project structure, setup instructions, and usage guidelines.


# Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- pip (Python package manager)
- Frontend (HTML, CSS, JAVASCRIPT)
- Database - MySQL

## Features

- Real-time messaging using websockets
- User authentication and authorization
- Chat room creation and management
- Private messaging between users
- Message history and retrieval


## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/stunner007-ir/realchat.git
   cd realchat

   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:

   ```bash
   python manage.py runserver

   ```

6. Access the API at http://localhost:8000/


### Contributors

- Backend - [Ishu Raj](https://github.com/stunner007-ir)
<!-- - [Contributor Name](https://github.com/contributor-username) -->

### License

This project is licensed under the [MIT License](LICENSE). 