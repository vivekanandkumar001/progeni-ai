# ---------- BASE IMAGE ----------
FROM python:3.10-slim

# ---------- WORKDIR ----------
WORKDIR /app

# ---------- INSTALL DEPENDENCIES ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- COPY APP FILES ----------
COPY . .

# ---------- ENVIRONMENT ----------
ENV PORT=7860
EXPOSE 7860

# ---------- RUN FLASK ----------
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
