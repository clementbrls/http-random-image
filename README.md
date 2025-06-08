# 🖼️ Image Switcher with Probability

This is a simple web server that returns either `a.webp` or `b.webp` when accessed via HTTP, based on a configurable probability.

It is built with Flask and served using Gunicorn, packaged in a lightweight Docker container.

---

## 📦 Features

- Serves one of two images (`a.webp` or `b.webp`) at `/`
- Configurable probability for image `b.webp`
- Minimal and production-ready setup
- Dockerized, with support for external volume mapping

---

## 🧠 How It Works

When a request is made to `/`, the app:

1. Reads `config.json` to determine the probability (`proba_image_b`) of serving `b.webp`
2. Returns `b.webp` with that probability, otherwise returns `a.webp`
3. Images must be placed in a mounted volume along with the config file

---

## 🗂️ Expected Directory Structure (Mounted Volume)

```bash
/data/
├── a.webp              # Default image
├── b.webp              # Alternate image
└── config.json         # Probability config
````

Example `config.json`:

```json
{
  "proba_image_b": 0.4
}
```

This means there's a 40% chance `b.webp` will be returned, otherwise `a.webp`.

---

## 🚀 Usage

### 1. Build the Docker image

```bash
docker build -t image-switcher .
```

### 2. Run it

```bash
docker run -p 8080:8080 -v /your/local/data:/data image-switcher
```

Or with Docker Compose (see below).


## 🐳 docker-compose.yml

```yaml
services:
  image-switcher:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data:/data
    restart: unless-stopped
```

Place your images and `config.json` in a local `./data/` folder.

### Then launch:

```bash
docker compose up --build
```


## 📝 Notes

* `proba_image_b` must be a float between `0.0` and `1.0`
* Both `a.webp` and `b.webp` must exist in the data directory
* Default probability is `0.25` if `config.json` is missing or invalid


## 📍 Endpoint

```
GET /
→ returns either a.webp or b.webp (with `image/webp` MIME type)
```

