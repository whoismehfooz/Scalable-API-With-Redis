# 🚀 Scalable API with Redis

A FastAPI project that demonstrates how Redis can be used to build faster and more scalable APIs through **Caching**, **TTL**, and **Rate Limiting**.

Instead of hitting the database on every request, the API intelligently stores frequently accessed data inside Redis, reducing database load and improving response times. ⚡

---

## ✨ Features

✅ Product Management API

✅ Redis Integration

✅ Response Caching

✅ Cache Hit / Cache Miss Logic

✅ Automatic Cache Expiration (TTL)

✅ Cache Invalidation

✅ Custom FastAPI Middleware

✅ Redis-Based Rate Limiting

✅ SQLite Database

✅ SQLAlchemy ORM

---

## 🛠️ Tech Stack

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| FastAPI        | API Framework           |
| SQLAlchemy     | ORM                     |
| SQLite         | Database                |
| Redis (Valkey) | Caching & Rate Limiting |
| Pydantic       | Validation              |

---

## 📂 Project Structure

```text
src/
├── cache/
│   ├── redis_client.py
│
├── middleware/
│   ├── rate_limit.py
│
├── products/
│   ├── controllers.py
│   ├── models.py
│   ├── routers.py
│   └── schemas.py
│
└── utils/
    ├── db.py
    └── settings.py
```

---

## ⚡ Redis Caching Flow

### First Request

```text
Client
   ↓
Redis ❌ (Cache Miss)
   ↓
Database
   ↓
Redis Store
   ↓
Response
```

### Second Request

```text
Client
   ↓
Redis ✅ (Cache Hit)
   ↓
Response
```

No database query needed. 🎯

---

## 🔥 Cache Invalidation

Whenever a new product is created:

```text
POST /products
      ↓
Database Updated
      ↓
Redis Cache Deleted
      ↓
Fresh Data Generated
```

This ensures users never receive stale data.

---

## 🛡️ Rate Limiting

The API tracks requests using Redis counters.

### Example

```text
Request #1  ✅
Request #2  ✅
Request #3  ✅
Request #4  ✅
Request #5  ✅
Request #6  ❌ 429 Too Many Requests
```

If the limit is exceeded:

```json
{
    "message": "Too many requests. Please try again later."
}
```

---

## 🌐 Available Endpoints

### Create Product

```http
POST /products
```

Example:

```json
{
  "name": "Keyboard",
  "price": 1200
}
```

---

### Get All Products

```http
GET /products
```

---

### Get Product By ID

```http
GET /products/{product_id}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd Scalable-API-With-Redis
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Redis / Valkey

```bash
sudo systemctl start valkey
```

### Run Application

```bash
fastapi dev main.py
```

---

## 🧠 Key Concepts Learned

* Redis Fundamentals
* Key-Value Storage
* TTL (Time To Live)
* Response Caching
* Cache Hit & Cache Miss
* Cache Invalidation
* Middleware Architecture
* Request Interception
* Redis Counters
* Rate Limiting
* FastAPI Project Structuring

---

## 🚀 Future Improvements

* Product Update Endpoint
* Product Delete Endpoint
* Cache Invalidation for Update/Delete Operations
* Authentication & Authorization
* PostgreSQL Integration
* Docker Support
* Background Tasks
* Distributed Rate Limiting

---

## 🎯 Project Goal

This project was built to understand how modern backend systems use Redis to:

⚡ Improve performance

🛡️ Prevent abuse

📈 Scale efficiently

while following clean FastAPI project architecture.

---

### ⭐ If you found this project useful, consider giving it a star.
