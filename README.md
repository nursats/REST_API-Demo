# **FastAPI Weather API**

A RESTful API built with FastAPI for weather data integration. This API allows users to fetch weather data from an external API, manage the data using CRUD operations, and access it securely with JWT-based authentication.

---

## **Features**
- Integration with [OpenWeatherMap](https://openweathermap.org/api) to fetch weather data.
- CRUD functionality for storing and managing weather data locally in PostgreSQL.
- Secure authentication using JSON Web Tokens (JWT).
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

---

## **Endpoints**

### **Authentication**
- **Login**: `/login`
  - **Method**: `POST`
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

### **Weather**
- **Get All Weather Data**: `/weather`
  - **Method**: `GET`
  - **Headers**: `Authorization: Bearer <token>`
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
  - **Headers**: `Authorization: Bearer <token>`
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

- **Update Weather Data**: `/weather/{id}`
  - **Method**: `PUT`
  - **Headers**: `Authorization: Bearer <token>`
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
  - **Headers**: `Authorization: Bearer <token>`
  - **Response**:
    ```json
    {
      "detail": "Weather record deleted successfully."
    }
    ```

- **Fetch Weather Information**:`/weather-info/{city}`

- **Method**: `GET`
- **Description**: Fetch weather information for a specific city. If the city exists in the local database, the data is returned from the database. Otherwise, it fetches data from the external weather API, stores it in the database, and then returns it.
- **Headers**:
  - `Authorization: Bearer <token>`
- **Path Parameters**:
  - `city`: The name of the city for which to fetch weather data.

#### **Example Request (Postman or cURL)**

- **Request**:
  ```bash
  curl -X GET "http://localhost:8000/weather-info/Astana" \
  -H "Authorization: Bearer <your_jwt_token>"
  ```

- **Response** (when data exists in the database):
  ```json
  {
    "id": 1,
    "city": "Astana",
    "temperature": -5.0,
    "created_at": "2024-12-04T12:00:00"
  }
  ```

- **Response** (when fetching from the external API):
  ```json
  {
    "id": 2,
    "city": "Astana",
    "temperature": -6.5,
    "created_at": "2024-12-04T13:00:00"
  }
  ```

- **Error Response** (invalid city or failed external API call):
  ```json
  {
    "detail": "Failed to fetch weather data for city 'InvalidCity'. Error: <API Error Details>"
  }
  ```

---

## **Deployment**

### **Railway**
The backend and database are deployed on [Railway](https://railway.app). Access the deployed API:
- Swagger UI: [<Railway Deployment URL>/docs](#)

### **Vercel**
The API is also deployed on Vercel. Access it here:
- Swagger UI: [<Vercel Deployment URL>/docs](#)

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

## **Future Improvements**
- Add unit and integration tests.
- Implement user roles and permissions.
- Introduce rate limiting for API requests.

---

## **License**
This project is licensed under the MIT License.
