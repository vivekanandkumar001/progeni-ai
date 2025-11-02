# ---- Base Image ----
FROM python:3.10-slim

# ---- Working Directory ----
WORKDIR /app

# ---- Copy Requirements and Install ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy the Entire App ----
COPY . .

# ---- Expose Port ----
EXPOSE 7860

# ---- Environment Variables ----
ENV PORT=7860
ENV PYTHONUNBUFFERED=1

# ---- Run Flask ----
CMD ["python", "app.py"]
