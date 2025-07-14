# 🚀 Portfolio Website Generator

This project is a FastAPI backend that generates a **fully responsive and colorful portfolio website** using a large language model (LLM) hosted on **Groq**. The website is styled with **TailwindCSS** and returned as a **single HTML file**.

---

## 🧠 Key Features

* Uses **Groq-hosted DeepSeek LLaMA 70B** model to generate code
* Accepts user prompts to guide the portfolio website's theme or content
* Outputs a **visually rich, mobile-responsive HTML portfolio**
* Stores the result locally as `portfolio.html`
* Supports CORS (Cross-Origin Resource Sharing)
* Simple REST API endpoints

---

## 📁 Project Structure

```
.
├── main.py              # FastAPI app
├── .env                 # Environment file (store your GROQ_API_KEY here)
├── portfolio.html       # Generated HTML file (auto-created)
└── README.md            # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/portfolio-generator.git
cd portfolio-generator
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn groq pydantic python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Run the App

```bash
uvicorn main:app --reload
```

The API will be available at:
`http://127.0.0.1:8000`

---

## 🔌 API Endpoints

### 1. **POST** `/generate_portfolio`

Generates the portfolio HTML based on the prompt.

**Request Body:**

```json
{
  "prompt": "I want a portfolio for a frontend developer with sections for projects, skills, and contact."
}
```

**Response:**

```json
{
  "message": "Generation completed."
}
```

---

### 2. **GET** `/get_html`

Fetches the generated portfolio HTML content.

**Response:**

```json
{
  "html_content": "<!DOCTYPE html>..."
}
```

---

## 💡 Prompt Tips

When sending a prompt, describe the desired features or theme of the portfolio site. Examples:

* "A colorful portfolio for a UI/UX designer"
* "A minimalist developer portfolio with dark theme"
* "A personal site for a data scientist showing projects, blog, and contact form"

---

## 🚰 Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) — API Framework
* [Groq](https://groq.com/) — LLM API Provider
* [TailwindCSS](https://tailwindcss.com/) — CSS Utility Framework
* [Pydantic](https://docs.pydantic.dev/) — Data validation
* [Uvicorn](https://www.uvicorn.org/) — ASGI Server

---

## 📄 License

MIT License

---
