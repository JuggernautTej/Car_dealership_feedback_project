
# Audi Customer Feedback Application

## 📌 About the Project

This is a simple **Flask** web application that allows customers to submit feedback about their experiences with Audi dealerships. The application collects customer feedback, stores it in a **PostgreSQL database**, and sends email notifications upon submission. The project is designed to be deployed on **Render** with a **Render-hosted PostgreSQL database**.

## 🚀 Features

-   Collect customer feedback including **customer name, dealer name, rating, and comments**.
-   Store feedback in a **PostgreSQL database**.
-   Prevent duplicate feedback submissions based on the customer's name.
-   Send email notifications upon successful feedback submission.

## 🛠️ Technologies Used

-   **Python** (Flask Framework)
-   **PostgreSQL** (Database)
-   **SQLAlchemy** (ORM for database interactions)
-   **Flask-Mail** (For email notifications)
-   **Render** (Database hosting and application deployment)
-    **HTML/CSS** (Front end implementation) 

----------

## 🏗️ Setup and Installation

### 1️⃣ Clone the Repository

```sh
 git clone https://github.com/JuggernautTej/audi-feedback-app.git
 cd audi-feedback-app

```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt

```

### 4️⃣ Set Up Environment Variables

Create a **.env** file in the project root and add:

```
FLASK_APP=app.py
ENV=dev
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
DB_NAME=your_db_name
MAIL_LOGIN=your_mailtrap_login
MAIL_PASSWORD=your_mailtrap_password
MAIL_SERVER=smtp.mailtrap.io
MAIL_PORT=2525
RENDER_DB_URI=your_render_database_uri

```

### 5️⃣ Initialize the Database

Run the following commands to set up the database:

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

```

Or manually create the table in PostgreSQL:

```sql
CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    customer VARCHAR(200) UNIQUE,
    dealer VARCHAR(200),
    rating INTEGER,
    comments TEXT
);

```

### 6️⃣ Run the Application Locally

```sh
flask run

```

The application will be available at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

----------

## 🚀 Deployment Instructions



The application and database are deployed on **Render**:

-   PostgreSQL is hosted on Render with the provided database URL.
    
-   The Flask application is also deployed on Render and connected to the database.
    

Make sure to configure **environment variables** in the dashboard.

----------

## 🔥 Future Enhancements

### 🌟 Next Steps for Upgrading the Application

-   ✅ **Add Authentication** - Secure access to feedback submissions.
-   ✅ **Admin Dashboard** - View and manage feedback entries.
-   ✅ **Improved Email Features** - Send confirmation emails to users.
-   ✅ **API Endpoints** - Convert the app into an API for mobile integration.
-   ✅ **Unit Testing** - Improve code quality with Flask testing.

----------

## 🤝 Call for Collaboration

Contributions are welcome! 🚀 If you're interested in improving this project, feel free to **fork** the repo and submit a **pull request**.

### 📧 Contact

For suggestions or inquiries, reach out via email: **[tiwatej@gmail.com](mailto:your-email@example.com)**

----------

## ⚖️ License

This project is licensed under the **MIT License**.