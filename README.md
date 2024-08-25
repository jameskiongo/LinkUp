# LinkUp

EventLinker is a web application that allows users to create and discover events. Users can pin locations on a map, RSVP to events, view prices, and make payments directly through the platform.

## Features

- **Event Creation:** Users can create events by providing a title, description, date, time, and location. They can also set a price for the event if applicable.
- **Map Integration:** Events are pinned on a map so that users can easily find and view events near them.
- **RSVP:** Users can RSVP to events they are interested in attending.
- **Payment Integration:** Users can view event prices and make payments directly within the app.
- **Event Discovery:** Browse events by location, date, or category to find something that suits your interests.

## Tech Stack

- **Frontend:** React.js (for building the user interface)
- **Backend:** Django (for handling the server-side logic and database)
- **Database:** PostgreSQL (for storing event data, user information, RSVPs, etc.)
- **Payment Gateway:** Stripe (for handling payments)
- **Map Integration:** Google Maps API (for displaying event locations)

## Setup Instructions

### Prerequisites

- Node.js (for running the frontend)
- Python 3.8+ (for running the backend)
- PostgreSQL (for database)
- Stripe account (for payment integration)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/eventlinker.git
    cd eventlinker
    ```

2. **Frontend Setup:**

    ```bash
    cd frontend
    npm install
    npm start
    ```

3. **Backend Setup:**

    ```bash
    cd backend
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

4. **Environment Variables:**

    Create a `.env` file in the backend directory and add the following:

    ```bash
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    STRIPE_API_KEY=your_stripe_api_key
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```

5. **Run the App:**

    - **Frontend:** `npm start` in the frontend directory.
    - **Backend:** `python manage.py runserver` in the backend directory.

6. **Access the App:**

    Open your browser and navigate to `http://localhost:3000` to access the frontend and `http://localhost:8000` for the backend API.

## Contributing

Feel free to submit issues and pull requests to contribute to the project. 

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
