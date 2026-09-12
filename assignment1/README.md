# Assignment 1

This project is a simple Flask application that exposes a JSON API and reads data from a local file.

## Project Overview

- `app.py` creates a Flask app.
- `/api` reads the content of `sample.txt`.
- `sample.txt` contains a list of student records in JSON format.

## Files

- `app.py` — Flask server and API endpoint
- `sample.txt` — JSON data used by the API

## Run the Project

From the `assignment1` folder:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/api
```

## API Response

The endpoint returns the JSON array from `sample.txt`.

Example output:

```json
[
  {
    "id": 1,
    "name": "Surya",
    "age": 20,
    "course": "Computer Science"
  }
]
```
