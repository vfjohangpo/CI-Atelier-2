# ---------- build ----------
FROM python:3.12-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- runtime ----------
FROM python:3.12-slim

LABEL maintainer="stephane-robert" \
      description="Pipeline Craft — API FastAPI fil rouge"

RUN groupadd --gid 1000 app && \
    useradd  --uid 1000 --gid app --shell /bin/false app

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app/ ./app/

USER app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
