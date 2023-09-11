
# ___Django ToDo App - Backend___


## __Definition__

Welcome to the Todo project! This project is designed to help you manage your tasks and stay organized. It is built using Django, a high-level Python web framework. With this application, you can create tasks, assign categories, track progress, and more.


## __Features__
- __Task Management:__ Create, edit, and delete tasks.
- __Task Categories:__ Categorize tasks for better organization.
- __Task Status:__ Mark tasks as completed or pending.
- __Flexible Data Model:__ Easily extend the application with additional fields or features



## __Installation__
To run the Todo project on your local machine, follow these steps:
1. Clone the repository:
    `git clone https://github.com/Anano24/todo-app-backend.git`
2. Navigate to the project directory:
    `cd todo-project`
3. Create a virtual environment (optional but recommended):
    `python -m venv venv`
4. Activate the virtual environment:
- On Windows:
    `venv\Scripts\activate`
- On macOS and Linux:
    `source venv/bin/activate`
5. Install the project dependencies:
    `pip install -r requirements.txt`
6. Apply database migrations:
    `python manage.py migrate`
7. Create a superuser (an admin user) to manage the application:
    `python manage.py createsuperuser`
8. Start the development server:
    `python manage.py runserver`
9. Access the application in your web browser at `http://localhost:8000/admin/` to log in as the superuser and start managing tasks.



- After installation, you can use the Django admin interface to manage tasks, authors, and categories.


