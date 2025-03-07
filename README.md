# Kavdhika Family Social Platform

A private social media platform designed specifically for small family groups. This application allows family members to share posts, react with emojis, and comment on each other's content in a secure, private environment.

## Features

- **User Authentication**: Secure login for family members
- **Post Creation**: Share text and images with your family
- **Reactions**: React to posts with various emojis (👍, ❤️, 😄, 😢, 😠)
- **Comments**: Engage in conversations through comments
- **Mobile-Friendly Design**: Responsive interface that works on all devices

## Technical Stack

- **Backend**: Django 5.1
- **Frontend**: Bootstrap 5, jQuery
- **Database**: SQLite (default), can be configured for PostgreSQL
- **Media Storage**: Local file system

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/kavdhika-social-app.git
   cd kavdhika-social-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 