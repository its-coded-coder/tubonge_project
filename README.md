
# Tubonge Project

## Project Objective
Create a comprehensive backend for a messaging application using Django and PostgreSQL. The application supports:
1. User authentication
2. Real-time messaging
3. Message history retrieval

## Technologies Used
- Django
- Django Rest Framework (DRF)
- Django Channels
- PostgreSQL
- WebSockets

## Setup Instructions

### Prerequisites
- Python 3.x
- PostgreSQL
- Node.js and npm

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/its-coded-coder/tubonge_project.git
    cd tubonge_project
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install the required Node.js packages**:
    ```bash
    npm install
    ```

5. **Configure PostgreSQL**:
    - Create a PostgreSQL database named `tubonge_db`.
    - Update the database credentials in `tubonge_backend/settings.py`.

6. **Apply database migrations**:
    ```bash
    python3 manage.py migrate
    ```

7. **Run the development server**:
    ```bash
    python3 manage.py runserver
    ```

### Usage

#### User Authentication
- **Register**: `POST /api/users/register/`
    ```json
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    ```

#### Real-time Messaging
- **WebSocket URL**: `ws://127.0.0.1:8000/ws/chat/<room_name>/`

### Testing WebSocket
1. **Install `wscat`**:
    ```bash
    npm install -g wscat
    ```

2. **Connect to WebSocket**:
    ```bash
    wscat -c ws://127.0.0.1:8000/ws/chat/testroom/
    ```

## Contributing
Feel free to submit issues, fork the repository and send pull requests.

## License
This project is licensed under the MIT License.
