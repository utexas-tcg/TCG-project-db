# TCG Outreach Tracker

A centralized tool for tracking company outreach efforts made by TCG project committee members across semesters. Designed to preserve institutional memory, assist future project directors, and streamline communication between TCG and external companies.

---

## 📚 Table of Contents

1. [Overview](#overview)
   - [Problem Statement](#problem-statement)
   - [Solution](#solution)
   - [Benefits](#benefits)
2. [Architecture](#architecture)
3. [Project Structure](#project-structure)
4. [Tech Stack](#tech-stack)
5. [Setup Instructions](#setup-instructions)
6. [Future Enhancements](#future-enhancements)

---

## 🔍 Overview

### Problem Statement

Over the course of multiple semesters, different project committees at TCG reach out to a wide range of companies. However, there is no centralized system to track which companies have already been contacted, by whom, and for what purpose. This leads to duplicated efforts, loss of historical knowledge, and inefficiencies in outreach.

### Solution

This project provides a centralized dashboard and backend database to track all outreach activity. Project directors upload a CSV at the end of each semester to add new data, and committee members can view outreach history, search by company or individual, and avoid redundant communication.

### Benefits

- 🔁 Prevents duplicated outreach by maintaining historical contact logs.
- 🔎 Searchable database for checking prior outreach per company or member.
- 📈 Analytics on who contacted which companies and how often.
- 🔐 Secure access limited to verified TCG members only.
- 🧠 Helps new directors quickly get up to speed with past outreach efforts.

---

## 🏗️ Architecture

- **Frontend**: [Streamlit](https://streamlit.io/) app for file upload, data exploration, and visual analytics.
- **Backend**: Python with SQLAlchemy for database interaction.
- **Database**: PostgreSQL (preferred) or SQLite (for local development).
- **Security**: Basic authentication using environment variables or token-based login (upgradable to OAuth).
- **Deployment**: Streamlit Cloud or Render (optional for future use).

---

## 🗂 Project Structure

tcg-outreach/ ├── app.py # Main Streamlit app ├── /pages/ # Additional app pages (if needed) ├── /db/ # Database connection and models │ ├── connect.py │ └── models.py ├── /data/ # Temporarily uploaded CSVs (ignored in git) ├── .env # Environment variables (DB credentials, etc.) ├── .gitignore # Exclude sensitive and unnecessary files ├── requirements.txt # Python dependencies └── README.md

---

## ⚙️ Tech Stack

- Python 3.10+
- Streamlit
- SQLAlchemy
- Pandas
- PostgreSQL or SQLite
- `dotenv` for environment management

---