# Rec<>nnect Backend

**Rec<>nnect** is the backend service for the **Rec<>nnect** application, a Flutter-based platform designed to help alumni connect and engage with each other. This backend, built with Django, provides essential functionalities for user management, connections, messaging, and event management.

## Features

- **User Management**: Create, update, and manage alumni profiles.
- **Connection Handling**: Send, accept, and manage connection requests between alumni.
- **Messaging System**: Support for sending and receiving messages between connected alumni.
- **Event Management**: Organize and manage alumni events and gatherings.

## Requirements

- **Python 3.8** (or higher)
- **Django 4.x** (or higher)
- **Django REST Framework** (for API development)
- **pip** (for managing Python packages)

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher, pip, installed.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/angrezichatterbox/reconnect-backend1.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd recnnect-backend
   ```

3. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! To contribute, please fork the repository and submit a pull request. For significant changes, please open an issue to discuss the proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact [Me!!](mailto:gouthammohanraj@gmail.com).

---
