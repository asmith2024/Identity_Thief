# Identity_Thief

Small Flask app that collects JSON payloads and stores them with TinyDB.

**Prerequisites**

- Docker and Docker Compose installed

**Run locally (dev)**

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python app.py
```

The app listens on port `5000` by default.

**Docker Compose (recommended)**

This repository includes a `docker-compose.yml` that maps host port `5002` to the container's HTTP port `5000`.

The app uses Werkzeug's `ProxyFix` middleware so it correctly handles `X-Forwarded-For`, `X-Forwarded-Proto`, `X-Forwarded-Host`, and `X-Forwarded-Prefix` headers from a reverse proxy.

Bring the service up:

```bash
docker compose up --build
```

Then open http://localhost:5002 in your browser.

To run in detached mode:

```bash
docker compose up --build -d
```

To stop and remove containers:

```bash
docker compose down
```

Files added:

- `docker-compose.yml` — Docker Compose service mapping host port `5002` to container port `5000`.
- `Dockerfile` — image used by the Compose service.
