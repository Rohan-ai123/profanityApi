# Profanity Censor API

This project is a simple API built with **FastAPI** that censors profane words from the provided input text using the `better-profanity` library. It includes endpoints for checking profanity in text and returning a censored version of the input.

## Features

- **Sanitization**: Removes non-printable control characters from the input.
- **Profanity Detection**: Identifies and censors offensive or inappropriate words.
- **Extensible**: Easily extendable for additional text processing tasks.

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Steps

1. Clone the repository or download the project files:
   ```bash
   git clone <repository_url>
   cd profanity_api
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

---

## API Endpoints

### 1. Root Endpoint

**URL**: `/`

**Method**: `GET`

**Description**: Returns a welcome message to confirm the API is running.

**Response**:
```json
{
  "message": "Welcome to the Profanity Censor API!"
}
```

### 2. Censor Text Endpoint

**URL**: `/censor/`

**Method**: `POST`

**Description**: Takes an input string and returns a censored version with profane words replaced.

**Request Body**:
```json
{
  "input_text": "Your input text here"
}
```

**Response**:
```json
{
  "censored_text": "Your **** text here"
}
```

---

## Project Structure

```
profanity_api/
├── main.py           # Main FastAPI application
├── requirements.txt  # Dependencies
├── words.txt         # Custom profanity word list (if any)
└── README.md         # Project documentation
```

---

## How It Works

1. Input text is sanitized to remove control characters.
2. The text is passed through the `better-profanity` library for profanity detection and censorship.
3. The censored text is returned as a JSON response.

---

## Dependencies

- **FastAPI**: Framework for building APIs.
- **Uvicorn**: ASGI server for running FastAPI.
- **better-profanity**: Library for detecting and censoring profanity.
- **pydantic**: For request body validation.

Install these dependencies via `requirements.txt`.
