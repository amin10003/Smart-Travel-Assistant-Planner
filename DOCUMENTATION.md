# Smart Travel Assistant & Planner
Version 1.0

Author:
Mohamed Ibrahim Yusuf

---

# 1. Project Description

Smart Travel Assistant & Planner is a desktop application developed using Python.

The application helps users plan trips by:

- Checking weather information using API
- Estimating transportation fare
- Saving travel history
- Viewing previous plans
- Deleting trips

The project demonstrates integration of:
- Object Oriented Programming (OOP)
- API Consumption
- SQLite Database
- CustomTkinter GUI

---

# 2. Problem Statement

Travelers visiting unfamiliar places may experience:

- Unexpected weather conditions
- Unfair transportation pricing
- Difficulty organizing travel information

This system provides simple trip planning assistance.

---

# 3. Objectives

Main objectives:

1. Apply Object Oriented Programming
2. Integrate external APIs
3. Work with SQLite database
4. Develop desktop interfaces
5. Manage data persistence

---

# 4. Scope

Included:

✓ Weather retrieval

✓ Fare estimation

✓ Trip creation

✓ Trip history

✓ Delete trips

Not Included:

✗ User accounts

✗ Online booking

✗ Payment systems

✗ Real transport prices

---

# 5. Technologies Used

Programming Language:
- Python

GUI:
- CustomTkinter

Database:
- SQLite

API:
- OpenWeather API

Version Control:
- Git & GitHub

Environment:
- Virtual Environment

---

# 6. System Architecture

User
↓

CustomTkinter UI
↓

Travel Planner
↓

Weather Service
+
Fare Service
↓

SQLite Database

---

# 7. Project Structure

Smart-Travel-Assistant-Planner/

main.py

planner.py

README.md

DOCUMENTATION.md

requirements.txt

.env

database/
database.py
travel.db

models/
trip.py

services/
weather_api.py
fare_service.py

ui/
ui.py

assets/

---

# 8. Functional Requirements

The system shall:

- Create trip plans
- Retrieve weather
- Estimate fares
- Save plans
- Display history
- Delete trips

---

# 9. Non Functional Requirements

- Easy to use
- Fast execution
- Lightweight
- Local storage

---

# 10. Testing

Test Cases:

Create Trip → Success

Save Database → Success

Show History → Success

Delete One → Success

Clear All → Success

---

# 11. Challenges

- API integration
- Environment variables
- Multi-file structure
- Connecting UI and database

---

# 12. Lessons Learned

- OOP organization
- Database interaction
- API handling
- GUI development

---

# 13. Future Improvements

- Political safety alerts

- Real transport pricing

- Maps integration

- Trip reminders

- User authentication

---

END