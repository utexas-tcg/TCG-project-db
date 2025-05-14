# TCG Outreach Tracker

A centralized tool for tracking company outreach efforts made by TCG project committee members across semesters. Designed to preserve institutional memory, assist future project directors, and streamline communication between TCG and external companies.

---

## 📚 Table of Contents

1. [Overview](#overview)
   - [Problem Statement](#problem-statement)
   - [Solution](#solution)
   - [Benefits](#benefits)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Project Structure](#project-structure)
5. [Tech Stack](#tech-stack)
6. [Setup Instructions](#setup-instructions)
7. [Usage Guide](#usage-guide)
8. [Future Enhancements](#future-enhancements)

---

## 🔍 Overview

### Problem Statement

Over the course of multiple semesters, different project committees at TCG reach out to a wide range of companies. However, there is no centralized system to track which companies have already been contacted, by whom, and for what purpose. This leads to duplicated efforts, loss of historical knowledge, and inefficiencies in outreach.

### Solution

This project provides a centralized dashboard and backend database to track all outreach activity. Project directors upload a CSV at the end of each semester to add new data, and committee members can view outreach history, search by company or individual, and avoid redundant communication.

### Benefits

- 🔁 Prevents duplicated outreach by maintaining historical contact logs
- 🔎 Searchable database for checking prior outreach per company or member
- 📈 Analytics on who contacted which companies and how often
- 🔐 Secure access limited to verified TCG members only
- 🧠 Helps new directors quickly get up to speed with past outreach efforts

---

## ✨ Features

- **Home Dashboard**: View confirmed projects and search all outreach records
- **Edit Records**: Search, modify, and delete existing outreach entries
- **Upload CSV**: Add new outreach data via CSV upload with intelligent validation
- **Smart Data Cleaning**: Automatic data validation and cleaning using Gemini AI
- **Duplicate Prevention**: System automatically detects and prevents duplicate entries

---

## 🏗️ Architecture

- **Frontend**: [Streamlit](https://streamlit.io/) app for file upload, data exploration, and visual analytics
- **Backend**: Python with SQLAlchemy for database interaction
- **Database**: PostgreSQL (preferred) or SQLite (for local development)
- **AI Integration**: Google Gemini API for CSV validation and data cleaning
- **Deployment**: Streamlit Cloud or containerized deployment via Docker

---

## 🗂 Project Structure

```
/tcg-outreach/
├── app.py                  # Main Streamlit app with navigation
├── /pages/                 # Page modules for the application
│   ├── Home.py             # Home page with search functionality
│   ├── Edit.py             # Edit page for modifying records
│   └── Upload.py           # Upload page for adding new data
├── /db/                    # Database components
│   ├── models.py           # SQLAlchemy models
│   └── connect.py          # Database connection setup
├── /utils/                 # Utility functions
│   └── utils.py            # Common utilities like footer rendering
├── csv_validator.py        # CSV validation with Gemini AI
├── .streamlit/             # Streamlit configuration
│   └── config.toml         # Theme and appearance settings
├── .env                    # Environment variables (not in repo)
├── .gitignore              # Git ignore patterns
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Tech Stack

- **Python 3.10+**: Core programming language
- **Streamlit**: Web application framework
- **SQLAlchemy**: ORM for database operations
- **Pandas**: Data manipulation and analysis
- **PostgreSQL/SQLite**: Database options
- **Google Gemini API**: AI-powered data validation
- **Python-dotenv**: Environment variable management
- **Streamlit-option-menu**: Navigation component

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/tcg-outreach.git
   cd tcg-outreach
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file with the following variables**
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/tcg_outreach
   # For SQLite: DATABASE_URL=sqlite:///data/tcg_outreach.db
   GEMINI_API=your_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the application**
   Open your browser and navigate to http://localhost:8501

---

## 📖 Usage Guide

### Home Page
- View confirmed projects at the top
- Use the search bar to find specific companies or contacts
- Expand cards to view detailed information about each outreach record

### Edit Page
- Search for records to edit
- Expand a record to modify its details
- Save changes or delete records as needed

### Upload Page
- Upload a CSV file with outreach data
- The system will validate and clean the data using AI
- Review the processed data before submitting to the database
- Only companies that have been reached out to will be added

### CSV Format
Your CSV should include the following columns:
- Committee Member
- Client Name
- Season
- Company
- Contact Info
- Industry
- Website
- Reached Out?(Yes/No)
- Response(Yes/No/Talking)
- Project Confirmed(Yes/No)
- Notes

---

## 🔮 Future Enhancements

- **Authentication**: Implement user login and role-based access
- **Analytics Dashboard**: Add visualizations for outreach statistics
- **Export Functionality**: Allow exporting filtered data to CSV
- **Email Integration**: Send outreach emails directly from the platform
- **Mobile Optimization**: Improve responsive design for mobile devices
- **Bulk Edit**: Enable editing multiple records simultaneously
- **Advanced Filtering**: Add more sophisticated search and filter options

---

## 👨‍💻 Contributors

- **Pranav Belligundu** - Initial development and maintenance
  - [GitHub](https://github.com/pranav-B21)
  - [LinkedIn](https://linkedin.com/in/pranav-belligundu/)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.



