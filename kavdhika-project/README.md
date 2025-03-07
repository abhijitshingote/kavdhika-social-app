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

1. Clone the repository
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
7. Access the admin interface at http://127.0.0.1:8000/admin/ to create users for family members

## Usage

1. Log in with your credentials
2. Browse the family feed on the home page
3. Create new posts using the "Create Post" button
4. React to posts with emoji buttons
5. Comment on posts to engage in conversations
6. Delete your own comments if needed

## Security Considerations

This application is designed for private use by a small group of family members. It's recommended to:

1. Use strong passwords for all accounts
2. Keep the application on a secure server
3. Regularly update Django and dependencies
4. Consider enabling HTTPS for production deployment

## License

This project is for private use only and not licensed for public distribution. 