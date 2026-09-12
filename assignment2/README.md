# Assignment 2

This assignment contains a mini Flask application with a frontend and a backend connected to MongoDB.

## Project Structure

```text
assignment2/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env   (optional if you store MongoDB connection details here)
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── README.md
```

## Backend

The backend is responsible for connecting to MongoDB and handling the database operations.

### Features

- Connects to MongoDB using `pymongo`
- Saves submitted form data to a collection named `test_collection`
- Provides:
  - `POST /submit` to insert a document
  - `GET /view` to fetch stored records

### Run backend

From the `assignment2/backend` folder:

```bash
pip install -r requirements.txt
python app.py
```

The backend listens on:

```text
http://127.0.0.1:9000
```

### Environment variable

The backend expects a MongoDB connection string in an environment variable named `mongo_url`.

Example:

```bash
set mongo_url=mongodb+srv://<username>:<password>@<cluster-url>/test
```

On Linux/macOS:

```bash
export mongo_url="mongodb+srv://<username>:<password>@<cluster-url>/test"
```

## Frontend

The frontend provides a simple HTML form for submitting name, email, and password data to the backend.

### Features

- Displays a signup page
- Sends form data to the backend using `requests`
- Shows stored data from the backend when the user clicks the View Data button

### Run frontend

From the `assignment2/frontend` folder:

```bash
pip install -r requirements.txt
python app.py
```

The frontend runs on:

```text
http://127.0.0.1:8000
```

## Flow

1. Start the backend server.
2. Start the frontend server.
3. Open the frontend page in the browser.
4. Submit the form.
5. View data from the backend using the data viewing option.

## Notes

- Make sure MongoDB is available and the `mongo_url` is configured correctly.
- The backend and frontend must both be running at the same time for the app to work as intended.
