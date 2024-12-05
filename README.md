# **FastAPI Weather API **

A RESTful API built with FastAPI for weather data integration. This API allows users to fetch weather data from an external API, manage the data using CRUD operations, and access it securely with JWT-based authentication.

The API is deployed and accessible at: https://rest-api-demo-project.vercel.app

---

## **Features**
- Integration with [OpenWeatherMap](https://openweathermap.org/api) to fetch weather data.
- CRUD functionality for storing and managing weather data in a PostgreSQL database hosted in the cloud (via Railway).
- Secure authentication using JSON Web Tokens (JWT).
- User registration and authentication.
- API documentation with Swagger UI.

---

## **Local Setup Instructions**

### **Requirements**
- Python 3.11+
- Docker & Docker Compose

### **Clone the Repository**
```bash
git clone <repository_url>
cd <repository_name>
```

### **Setup Environment Variables**
1. Create a `.env` file in the root directory:
   ```env
   API_KEY=<your_openweathermap_api_key>
   BASE_URL=http://api.openweathermap.org/data/2.5/forecast

   SECRET_KEY=<your_secret_key>
   ALGORITHM=HS256

   DATABASE_URL=postgresql://postgres:password@db:5432/fastapi_db
   ```
2. Add `.env` to `.gitignore` to secure sensitive data.

### **Run Locally with Docker Compose**
1. Build and start the application:
   ```bash
   docker-compose up --build
   ```
2. Access the application at:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### **Run Without Docker**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start a PostgreSQL database locally and update the `DATABASE_URL` in the `.env` file accordingly.
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## **Endpoints**

### **Authentication**
- **Login**: `/login`
  - **Method**: `POST`
  - **Description**: Obtain a JWT token for accessing secure endpoints.
  - **Body**:
    ```json
    {
      "username": "user@example.com",
      "password": "yourpassword"
    }
    ```
  - **Response**:
    ```json
    {
      "access_token": "jwt_token",
      "token_type": "bearer"
    }
    ```

### **Users**
- **Create User**: `/users`
  - **Method**: `POST`
  - **Description**: Register a new user.
  - **Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "yourpassword"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "created_at": "2024-12-04T12:00:00"
    }
    ```
  - **Error Response**:
    ```json
    {
      "detail": "User already exists"
    }
    ```
- **Get User**: `/users/{id}`
  - **Method**: `GET`
  - **Description**: Fetch user details by ID. Returns user info or 404 if not found.
  - **Response**:
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "created_at": "2024-12-04T12:00:00"
    }
    ```
  - **Error Response**:
    ```json
    {
      "detail": "User with id: {id} does not exist"
    }
    ```

### **Weather**
- **Get All Weather Data**: `/weather`
  - **Method**: `GET`
  - **Description**: Fetch all weather records from the database for the authenticated user.
  - **Headers**:
    - `Authorization: Bearer <token>`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "city": "Nur-Sultan",
        "temperature": -5.0,
        "created_at": "2024-12-04T12:00:00"
      }
    ]
    ```

- **Create Weather Data**: `/weather`
  - **Method**: `POST`
  - **Description**: Add a new weather record by specifying the city name.
  - **Headers**:
    - `Authorization: Bearer <token>`
  - **Body**:
    ```json
    {
      "city": "Nur-Sultan"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "city": "Nur-Sultan",
      "temperature": -5.0,
      "created_at": "2024-12-04T12:00:00"
    }
    ```

- **Fetch Weather Information for a Specific City**: `/weather-info/{city}`
  - **Method**: `GET`
  - **Description**: Fetch weather information for a specific city. If the city exists in the local database, the data is returned from the database. Otherwise, it fetches data from the external weather API, stores it in the database, and then returns it.
  - **Headers**:
    - `Authorization: Bearer <token>`
  - **Path Parameters**:
    - `city`: The name of the city for which to fetch weather data.
  - **Response**:
    ```json
    {
      "id": 1,
      "city": "Astana",
      "temperature": -5.0,
      "created_at": "2024-12-04T12:00:00"
    }
    ```

- **Update Weather Data**: `/weather/{id}`
  - **Method**: `PUT`
  - **Description**: Update the weather data for a specific record by ID.
  - **Headers**:
    - `Authorization: Bearer <token>`
  - **Body**:
    ```json
    {
      "city": "Almaty"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "city": "Almaty",
      "temperature": -3.0,
      "created_at": "2024-12-04T12:00:00"
    }
    ```

- **Delete Weather Data**: `/weather/{id}`
  - **Method**: `DELETE`
  - **Description**: Delete a weather record by ID.
  - **Headers**:
    - `Authorization: Bearer <token>`
  - **Response**:
    ```json
    {
      "detail": "Weather record deleted successfully."
    }
    ```

---


## **Deployment**

### **Backend (FastAPI)**: Deployed on Vercel
The FastAPI backend is deployed on [Vercel](https://vercel.com). Access the deployed API here:
- **Swagger UI**: [https://rest-api-demo-project.vercel.app/docs](https://rest-api-demo-project.vercel.app/docs)
- **Base URL**: `https://rest-api-demo-project.vercel.app/`

### **Database**: Deployed on Railway
The PostgreSQL database is hosted on [Railway](https://railway.app), and the backend connects to it using the `DATABASE_URL` environment variable.

- Railway provides the connection string in the format:
  ```text
  postgresql://<username>:<password>@<host>:<port>/<database>
  ```
- This connection string is securely stored as an environment variable (`DATABASE_URL`) in Vercel.

---

### **How the Components Work Together**
- **FastAPI**: Handles requests and performs CRUD operations using SQLAlchemy.
- **PostgreSQL (Railway)**: Stores persistent data, such as weather records and user information.
- **Environment Variables**:
  - Vercel provides the `DATABASE_URL` to the FastAPI app during runtime.
  - The FastAPI app uses this to establish a connection with the PostgreSQL database on Railway.

---

## **Technologies Used**
- **FastAPI**: Backend framework.
- **PostgreSQL**: Database.
- **SQLAlchemy**: ORM for database interaction.
- **Docker**: Containerization.
- **OpenWeatherMap API**: External API integration.
- **Railway**: Cloud deployment for PostgreSQL.
- **Vercel**: Cloud deployment for FastAPI app.

---

## Contact

Nursat - [@nursatse](https://t.me/nursatse) - nursat.seitov12@gmail.com

Project Link: [https://github.com/nursats/REST_API-Demo](https://github.com/nursats/REST_API-Demo)