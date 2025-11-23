Social Activity Feed API
REST API built with Django and Django REST Framework. This project implements a social network backend featuring user management, an automated activity feed, and role-based blocking and permissions.

Submission Links:
Source Code: https://github.com/lavdeep2332/inkle-Social-Assignment

Live Deployment: https://inkle-social-assignment.onrender.com/api/register/

DOCS API Documentation: https://documenter.getpostman.com/view/50284284/2sB3dHVsSY

# Project Requirements Checklist

This API fulfills all requirements specified in the assignment:

**User Auth:** Signup, Login (JWT), and Profile management.

**Social Actions:** Create posts, Like content, Follow users.

**Activity Feed:** Global wall tracking all network actions (via Signals).

**Blocking System:** Blocked users disappear entirely from the feed and API.

**Role-Based Access:**
Admin: Can delete any post or user.
Owner: Can manage Admins.

**Feed Logs:** Tracks "Post deleted by Admin" and "User deleted by Owner".

# Project Approach & Architecture

I designed this system to be modular and scalable. Instead of a monolithic structure, I separated the logic into four distinct apps: accounts, content, social, and feed. This ensures separation of concerns and makes the codebase easier to maintain.

# Key Technical Decisions

Automated Feed (Signals): I implemented the Observer Pattern using Django Signals. Instead of writing feed logic inside every View, a background listener automatically creates an Activity entry whenever a Post, Like, or Follow occurs. This keeps the controllers clean and ensures data consistency.

Polymorphic Relationships: The Activity Feed uses Generic Foreign Keys. This allows a single Activity table to link dynamically to different types of objects (a User or a Post) without creating messy database schemas.

Privacy by Design (Blocking): Blocking is handled at the QuerySet level. By overriding the get_queryset method, I ensure that if User A blocks User B, User B’s content is filtered out of the API response immediately. This is more secure than filtering in the frontend or serializer.

# Local Setup Guide
If you wish to run this locally instead of using the live link, follow these steps:

1. Clone the Repository
git clone [Your GitHub Link]
cd social-feed-api

3. Create Virtual Environment
python -m venv venv
**Windows**
venv\Scripts\activate
**Mac/Linux**
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Create Admin User (To test Admin features)
python manage.py createsuperuser
6. Start Server
python manage.py runserver

# Testing with Postman
I have included a comprehensive Postman collection to make testing easy.

Option A: View Online Docs Click the "API Documentation" link at the top of this Readme.
Option B: Import Collection

Find the Social_Feed_Collection.json file in this repository.

Import it into your Postman.

Note on Auth: The collection is configured to automatically handle tokens.

Run the Login request first.

The script automatically saves the token.

All subsequent requests will work immediately without manual copying.

**Common Issues / Notes:**
Debug Mode: Debug is set to False for the production (Render) build for security. It is True for local development.

Database: The local setup uses sqlite3 for simplicity. The production deployment uses PostgreSQL
