# SimpleTimeService (Minimal Python)

A tiny HTTP microservice that returns the current UTC timestamp and the visitor IP. Built to satisfy the Minimalist Application / Docker / Kubernetes task requirements.

## Features
- Returns JSON:
  ```json
  { "timestamp": "<current UTC time>", "ip": "<client IP>" }
  ```
- No external dependencies (pure Python standard library)
- Dockerized and runs as a **non-root user** (security best practice)
- Very lightweight and easy to deploy
- Suitable for Kubernetes, ingress testing, and microservice demos

---

## Repository Structure
```
app.py
Dockerfile
.dockerignore
README.md
```

---

## Build Image (single required command)
```bash
docker build -t simpletimeservice:latest .
```

---

## Run Locally (single required command)
```bash
docker run --rm -p 8080:8080 simpletimeservice:latest
```

Test the service:
```bash
curl http://localhost:8080/
```

Expected response:
```json
{"timestamp":"2025-12-12T10:00:00+00:00","ip":"127.0.0.1"}
```

---

## Push to Docker Hub
Tag the image:
```bash
docker tag simpletimeservice:latest <registry>/<account>/<repository>:<tag>
```

Push:
```bash
docker push <registry>/<account>/<repository>:<tag>
```

---

## Pull & Run (for reviewers/testers)
```bash
docker pull maverick96k/simpletimeservice:latest
docker run --rm -p 8080:8080 maverick96k/simpletimeservice:latest
```

Test:
```bash
curl http://localhost:8080/
```

---

## Git Repository Instructions
```bash
git init
git add .
git commit -m "Initial commit: SimpleTimeService minimal app"
git branch -M main
git remote add origin git@github.com:<your-username>/SimpleTimeService.git
git push -u origin main
```

---

## Kubernetes Deployment Example
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simpletimeservice
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simpletimeservice
  template:
    metadata:
      labels:
        app: simpletimeservice
    spec:
      containers:
      - name: simpletimeservice
        image: maverick96k/simpletimeservice:latest
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: simpletimeservice
spec:
  selector:
    app: simpletimeservice
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
```

Port-forward to test:
```bash
kubectl port-forward svc/simpletimeservice 8080:80
curl http://localhost:8080/
```

---

## Requirements Checklist (as per task)
- ✔ Simple microservice returning timestamp + IP  
- ✔ Minimal code  
- ✔ Dockerfile included  
- ✔ Runs as **non-root user**  
- ✔ Image build uses only `docker build`  
- ✔ Running requires only `docker run`  
- ✔ Image pushed to public registry (Docker Hub)  
- ✔ README with complete instructions  
- ✔ Kubernetes example included  
- ✔ No secrets committed  

---

## License
MIT