📝 To-Do App

A full-stack To-Do application built with Flask and MongoDB, featuring separate frontend and backend services.  
Live Demo: https://todo-frontend-f962.onrender.com/

------------------------------------------------------------
✨ Features
------------------------------------------------------------
- Add To-Do items with:
  • Item Name
  • Item Description
  • Item ID
  • Item UUID
  • Item Hash
- Store To-Do items in MongoDB Atlas
- View submitted To-Do items
- Separate Flask frontend and backend

------------------------------------------------------------
🛠 Tech Stack
------------------------------------------------------------
- Backend: Python, Flask, PyMongo
- Frontend: Flask (templates, routes)
- Database: MongoDB Atlas
- Other Tools: Requests, Git & GitHub, Render (deployment)

------------------------------------------------------------
📂 Project Structure
------------------------------------------------------------
todo-app/
├── backend/
│   ├── app.py
│   └── requirements.txt
└── frontend/
    ├── app.py
    ├── requirements.txt
    └── templates/
        └── index.html

------------------------------------------------------------
🚀 Deployment
------------------------------------------------------------
The application is deployed using Render:

- Frontend → Render Web Service
- Backend → Render Web Service
- Database → MongoDB Atlas

Database credentials are stored securely as environment variables and are not committed to GitHub.

------------------------------------------------------------
🔮 Future Improvements
------------------------------------------------------------
- Enhance submission and view-data pages with better UI/UX
- Add authentication for users
- Implement update & delete functionality for To-Do items
- Improve error handling and logging

------------------------------------------------------------
📌 Getting Started
------------------------------------------------------------
1. Clone the repository
   git clone https://github.com/your-username/todo-app.git
   cd todo-app

2. Backend setup
   cd backend
   pip install -r requirements.txt
   python app.py

3. Frontend setup
   cd frontend
   pip install -r requirements.txt
   python app.py

4. Environment variables
   Create a .env file in both frontend/ and backend/ with:
   MONGO_URI=<your-mongodb-atlas-uri>
   BACKEND_URL=<your-backend-service-url>

------------------------------------------------------------
📸 Screenshots
------------------------------------------------------------
- Home Page – Add new To-Do items
- View Page – Display stored To-Do items

------------------------------------------------------------
🤝 Contributing
------------------------------------------------------------
Contributions are welcome! Feel free to fork this repo and submit a pull request.
