# Bus Ticket Booking API

This Django application provides API endpoints for user registration, obtaining JWT tokens, searching buses, blocking seats, and booking tickets. It uses Django REST framework for the API implementation and JWT authentication for secure access.

## API Endpoints

### 1. User Registration

**URL**: `/api/register/`  
**Method**: `POST`  
**Auth**: No authentication required

**Description**: Registers a new user.

**Request Body**:
```json
{
  "username": "user1",
  "password": "password",
  "email": "user1@example.com"
}
