### README 

# Art Finder

## Introduction
Art Finder is a dynamic web application designed to enhance the experience of art enthusiasts by simplifying the process of discovering galleries, museums, and art-related events in their vicinity. This platform not only provides tailored information about various art locations and events but also allows users to organize and plan their art journeys with ease.

## Features

- **User Authentication**: Secure registration and login process.
- **User Service**: Full CRUD (Create, Read, Update, Delete) operations for user profiles.
- **Wishlist Service**: Users can add or remove items to a personal wishlist for future visits.
- **Venue Service**: Browse and search functionalities for finding galleries and museums.
- **Event Service**: Explore upcoming art-related events.
- **Explore Service**: Customized search options to discover venues and events based on categories.
- **Mailing Service**: Automated emails for updates and reminders.

## Pages

- **Explore**: Discover venues and events.
- **My Plans**: Manage and plan upcoming visits and itineraries.
- **Wishlist**: Keep track of favorite venues and events.

## Tech Stack

- **Frontend**: React.js, CSS, Redux Toolkit
- **Backend**: Python, Django
- **Database**: SQLite
- **Authentication**: JWT

## Getting Started

### Prerequisites

- Node.js
- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```
   git clone https://github.com/talehafandi/art-finder-django-react.git
   cd art-finder-django-react
   ```

2. **Install Backend Dependencies**
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **Migrate the Database**
   ```
   python manage.py migrate
   ```

4. **Run the Backend Server**
   ```
   python manage.py runserver
   ```

5. **Install Frontend Dependencies**
   ```
   cd ../frontend
   npm install
   ```

6. **Run the Frontend Development Server**
   ```
   npm start
   ```

The application should now be running on `localhost:3000` for the frontend and `localhost:8000` for the backend.
