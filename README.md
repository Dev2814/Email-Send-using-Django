# SendingEmail App

A Django-based web application for user authentication with email notifications.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Email Notifications**: Styled HTML emails for signup and login.
- **Responsive Design**: Clean and modern UI.
- **Form Validation**: Client-side and server-side validation.
- **Flash Messages**: Popup messages for success, error, and info.
- **Session Management**: Secure user session handling with Django's auth system.
- **Navbar Display**: Dynamic navbar greeting logged-in users.
- **Logout Button**: Stylish button with hover effects.
- **Error Handling**: Friendly user feedback on login failures.

## Technologies

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Email Sending**: Django's `send_mail` and `EmailMultiAlternatives`
- **Database**: SQLite (default Django database)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SendingEmailApp.git
   cd SendingEmailApp
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

## Folder Structure

```
SendingEmailApp/
├── SendingEmail/            # Django app
│   ├── templates/           # HTML templates
│   │   ├── index.html
│   │   └── Login.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── views.py             # App views
│   └── urls.py              # App-specific routes
├── manage.py                # Django entry point
└── db.sqlite3               # Default database
```

## Screenshots

> Add screenshots of your login page, popup messages, and dashboard here.

## Deployment

You can deploy this app on platforms like:
- **Heroku**
- **Render**
- **PythonAnywhere**

Make sure to configure environment variables and email settings in production.

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ using Django

