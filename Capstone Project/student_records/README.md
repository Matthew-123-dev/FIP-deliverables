# Student Records Management API

Async FastAPI app with PostgreSQL (asyncpg) and SQLAlchemy 2.x.

Setup
1. Copy `.env.example` to `.env` and set `DATABASE_URL` and `OPENAI_API_KEY` if using AI.
2. Install dependencies: pip install -r requirements.txt
3. Ensure PostgreSQL has the uuid-ossp extension: `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`
4. Initialize alembic and run migrations:

   alembic upgrade head

Run locally

Use uvicorn:

    uvicorn app.main:app --reload

Endpoints

GET /health — status

Students (/api/v1/students)
- POST / — create student
- GET / — list students (params: page, limit, course, grade, is_active, min_gpa, max_gpa)
- GET /{student_id} — get student
- PATCH /{student_id} — partial update
- DELETE /{student_id} — soft delete (is_active=false)

Search (/api/v1/search)
- GET /?q=&page=1&limit=20&course=&grade=&is_active=

AI summary (/api/v1/students/{student_id}/summary)
- GET — returns one-paragraph summary using OpenAI (requires OPENAI_API_KEY)

Example curl

Create:

```
curl -X POST http://localhost:8000/api/v1/students/ -H "Content-Type: application/json" -d '{"first_name":"John","last_name":"Doe","email":"john@example.com","course":"Math","enrolled_at":"2024-09-01"}'
```

List with filters:

```
curl "http://localhost:8000/api/v1/students/?page=1&limit=10&course=Math&min_gpa=3.0"
```

Search:

```
curl "http://localhost:8000/api/v1/search/?q=john&page=1&limit=10"
```

AI summary:

```
curl "http://localhost:8000/api/v1/students/{student_id}/summary"
```
