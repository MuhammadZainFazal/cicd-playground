# ---- Build stage: install dependencies ----
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---- Runtime stage: small final image ----
FROM python:3.12-slim
WORKDIR /srv
COPY --from=builder /install /usr/local
COPY app ./app

# Run as non-root (security best practice)
RUN useradd --create-home appuser
USER appuser

ENV PORT=8000
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.main:app"]
