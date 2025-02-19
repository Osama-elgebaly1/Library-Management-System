# **Library Management System**

## **Description**  
The **Library Management System** is a web-based application designed for librarians to efficiently manage their library's books and income. Unlike traditional systems, all operations are handled through a user-friendly interface—**no need for the Django admin panel**. The system provides a powerful dashboard that displays real-time financial data and book status insights.

---

## **Features**  

- **Book Management** – Add, edit, and remove books.  
- **Category Management** – Manage different book categories.  
- **Search & Filter** – Search for books by title and filter them by status (sold, rented, available).  
- **Dashboard Overview** – A visual dashboard displaying:  
  - 📊 **Total Income**  
  - 📚 **Total Number of Books**  
  - 📖 **Breakdown of Books** (Sold, Rented, Available)  
  - 💰 **Income Breakdown** (Revenue from Renting vs. Selling)  
- **All actions are performed via the main interface**, eliminating the need for admin panel access.  

---

## **Tech Stack**  

- **Backend:** Django (Python)  
- **Database:** SQLite3  
- **Frontend:** Not developed by me  

---

## **Installation & Setup**  

Follow these steps to set up and run the project locally:  

### **1. Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **2. Clone the Repository**  
```bash
git clone https://github.com/Osama-elgebaly1/Library-Management-System.git
cd Library-Management-System/project
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**  
```bash
python manage.py migrate
```

### **5. Run the Development Server**  
```bash
python manage.py runserver
```

Now, the project should be running at **http://127.0.0.1:8000/**.  

---

## **Usage**  

Once the project is up and running, the librarian can:  

- **Add, Edit, and Delete Books** – Manage the library's collection.  
- **Categorize Books** – Organize books by categories.  
- **Search & Filter Books** – Quickly find books by title or status.  
- **View Financial Data** – Use the dashboard to track income and book status.  

---

-

## **Demo Video**  
*Upload your demo video and add a link here:*  
```markdown
[Click here to watch the demo]()
```

---

## **Contributing**  
Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.  

---



