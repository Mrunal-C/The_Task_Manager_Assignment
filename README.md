***Task Manager Project- by Mrunal Choudhari***

***Overview***

The Task Manager Project is a Django-based web application designed to handle task management through a RESTful API. It supports user authentication and task operations, including creation, retrieval, updating, and deletion.

***Project Structure***

task_manager_project/

│

├── api/

│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── models.py

│   ├── serializers.py

│   ├── urls.py

│   ├── views.py

│   └── tests.py

│

├── task_manager_project/

│   ├── __init__.py

│   ├── settings.py

│   ├── urls.py

│   ├── wsgi.py

│   └── asgi.py

│

├── manage.py

├── Dockerfile

├── docker-compose.yml

└── requirements.txt

***Setup***

1. Clone the Repository:

   git clone <repository_url>
   -> cd task_manager_project

2. Install Dependencies:

   -> pip install -r requirements.txt

3. Set Up the Database:
Make sure MySQL is running as specified in docker-compose.yml. Run:

   -> docker-compose up -d

4. Apply Migrations:

   -> python manage.py migrater

5. Run the Development Server:

   -> python manage.py runserver

6. Run Tests:
   To ensure everything is working correctly, you can run the test suite:

   -> python manage.py test

***Approach and Assumptions***

***1. Approach:***

- Django Framework: Chosen for its comprehensive features and ease of use in building web applications.

- Django REST Framework: Utilized to develop a RESTful API, allowing for straightforward CRUD operations on tasks and user management.

- MySQL: Selected as the database backend for its reliability and compatibility with Django.

- JWT Authentication: Implemented for secure authentication, ensuring that API endpoints are protected and only accessible to authenticated users.

- Docker: Used for containerization, making it easier to manage dependencies and ensure a consistent environment across different stages of        development and deployment.

***2. Assumptions:***

- Database Configuration: The MySQL database configuration in docker-compose.yml assumes the credentials and database setup are correct. Adjust the MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, and MYSQL_ROOT_PASSWORD values as needed.

- Development Environment: Assumes Docker and Docker Compose are installed and configured. Docker Compose handles both the application and database setup, simplifying the process.

- Security: Basic security measures are implemented. For a production environment, additional configurations and security enhancements would be required, including managing sensitive information and environment-specific settings.

***Code Explanation***

1. models.py:
Defines the Task model with fields for title, description, status, priority, due date, and timestamps. The user field links each task to a specific user.

2. serializers.py:
Contains serializers for converting model instances to JSON and vice versa. UserSerializer handles user data, and TaskSerializer manages task data. The UserSerializer also includes user creation logic with hashed passwords.

3. views.py:
Implements viewsets for handling API requests. UserViewSet manages user-related operations, while TaskViewSet handles task-related operations and ensures that tasks are filtered by the authenticated user.

4. urls.py:
Configures API routing using Django REST Framework’s DefaultRouter, setting up routes for user and task endpoints.

5. settings.py:
Configures project settings, including database settings, installed apps, middleware, and REST framework settings. The database configuration uses SQLite for development but can be changed to MySQL.

6. Dockerfile:
Defines the Docker image for the application. It installs dependencies and sets the command to run the Django development server.

7. docker-compose.yml:
Specifies services for the application and database, setting up MySQL and the Django app in separate containers.

8. requirements.txt:
Lists the Python dependencies needed for the project.
