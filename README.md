# ✈ Smart Travel Assistant & Planner

Smart Travel Assistant & Planner is a desktop application built with Python that helps users plan trips more intelligently by combining weather information, route estimation, fare prediction, and trip history management into one system.

The application allows a user to select a departure location, destination, travel date and transport type, then automatically estimates travel cost, retrieves weather information, and stores the trip locally for future access.

---

# Problem

Planning local travel often involves switching between multiple tools:

* Checking weather separately
* Estimating transport costs manually
* Calculating routes mentally
* Forgetting previously planned trips

This makes travel preparation slower and less organized.

---

# Solution

Smart Travel Assistant & Planner combines trip planning features into one desktop application.

The system:

✔ Plans trips between locations
✔ Retrieves live weather information
✔ Estimates transport fare dynamically
✔ Stores trip history locally
✔ Allows trip management

---

# Features

## Trip Planning

Create a travel plan using:

* Departure place
* Destination
* Travel date
* Travel time
* Vehicle type
* Notes

---

## Weather Integration

The system connects to OpenWeather API to retrieve:

* Temperature
* Weather condition
* Humidity

Weather is fetched only for the destination.

---

## Dynamic Fare Estimation

Fare is estimated using an algorithm:

Estimated Fare =
(Base Fare + Distance × Per KM Rate)

Vehicle supported:

* Bus
* Van
* Taxi

---

## Distance Calculation

The application:

1. Converts place names into coordinates
2. Calculates route distance
3. Uses distance for fare prediction

---

## Trip History

Users can:

* View previous trips
* Delete one trip
* Clear all trip history

---

# Preview

Travel Assistant Desktop Application

Modern desktop interface with:

* Two-column layout
* Trip controls
* Result display panel
* Dark mode

---

# Technologies Used

| Technology      | Purpose              |
| --------------- | -------------------- |
| Python          | Core language        |
| CustomTkinter   | Modern desktop UI    |
| SQLite          | Local database       |
| OpenWeather API | Weather retrieval    |
| OpenStreetMap   | Geocoding            |
| OSRM API        | Distance calculation |
| Git             | Version control      |

---

# Project Structure

```plaintext
Smart-Travel-Assistant-Planner/

│
├── main.py
├── planner.py
├── requirements.txt
├── .env
│
├── database/
│   └── database.py
│
├── models/
│   └── trip.py
│
├── services/
│   ├── weather_api.py
│   ├── fare_service.py
│   ├── distance_service.py
│   └── geocode_service.py
│
└── ui/
    └── ui.py
```

---

# Installation

## 1 Clone Repository

```bash
git clone https://github.com/amin10003/Smart-Travel-Assistant-Planner.git
```

---

## 2 Move Into Project

```bash
cd Smart-Travel-Assistant-Planner
```

---

## 3 Create Virtual Environment

Linux:

```bash
python -m venv venv
```

Windows:

```bash
python -m venv venv
```

---

## 4 Activate Environment

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 5 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a file:

```plaintext
.env
```

Add:

```env
API_KEY=your_openweather_api_key
```

Get API key from OpenWeather.

---

# Run Application

Start the application:

```bash
python main.py
```

Expected:

```plaintext
Application window opens
↓
Create trip
↓
Weather + Fare calculated
↓
Trip stored locally
```

---

# Example Usage

Input:

```plaintext
Departure:
Nairobi

Destination:
Mombasa

Date:
2026-06-30

Vehicle:
Van
```

Output:

```plaintext
Weather:
29°C Clear

Estimated Fare:
KES XXXX

Trip Saved
```

---

# Future Improvements

* Live Maps Integration
* Traffic Awareness
* Route Visualization
* Smarter Fare Prediction
* AI Travel Recommendations
* Multi-user Support

---

# Author

Mohamed Ibrahim Yusuf

Software Development Student

GitHub:
https://github.com/amin10003

---

# License

Licensed under MIT License.
