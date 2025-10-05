# 🐾 Veterinary Practice Data Status API

A lightweight **Flask-based REST API** designed to simulate veterinary data reporting and integration workflows for pet-insurance analytics.  
The system accepts JSON requests, validates input, returns structured responses, and includes health-check and data-retrieval endpoints.  
Deployed on **Google Cloud Platform (App Engine)** for scalability and testing.

---

## 🚀 Features
- **Flask REST API** with clean routing and modular structure  
- **Input validation** and descriptive error handling  
- **Mock database** to simulate daily pet-record loads  
- **Endpoints** for health checks and data queries  
- **JSON responses** for reliable client integration  
- **Cloud deployment** with environment-variable port configuration  

---

## 🧩 Tech Stack
- **Language:** Python 3  
- **Framework:** Flask  
- **Data Handling:** pandas (for ETL-style extensions)  
- **Cloud Hosting:** Google Cloud Platform (App Engine)  
- **Tools:** cURL / Postman for API testing  

---

## 📡 API Endpoints

| Method | Route | Description |
|:--|:--|:--|
| `GET` | `/` | Root test route |
| `GET` | `/healthcheck` | Returns API operational status |
| `POST` | `/status` | Accepts JSON payload with `command` and `practice_id`; returns pets loaded today |
| `GET` | `/practices/<practice_id>` | Retrieves pet load data for a specific practice |

### Example Request
```bash
curl -X POST https://<your-app>.appspot.com/status \
  -H "Content-Type: application/json" \
  -d '{"command":"status","practice_id":"kitcat"}'
```
### Example Response
```bash
{
  "pets_loaded_today": 198
}

```
##⚙️ Running Locally

### Clone the repo
```bash
git clone https://github.com/<yourusername>/veterinary-status-api.git
cd veterinary-status-api
```

### Install dependencies
```bash
pip install flask
```

### Run the server

python app.py


The app will start on http://0.0.0.0:8080.

## 🧠 Key Learnings

Implemented structured REST API endpoints and HTTP error handling

Strengthened understanding of JSON validation and response formatting

Gained experience deploying Python web apps on Google Cloud Platform

Practised clean-code principles for maintainability and testing

## 🧾 License

This project is released under the MIT License.
