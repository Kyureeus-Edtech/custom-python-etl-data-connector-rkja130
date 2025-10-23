🧠 PublicWWW (Free Endpoint) – ETL Data Integration Project
📋 Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline that collects data from multiple public APIs, processes it, and stores it into MongoDB.

The system automatically:

Extracts data from 3 APIs (CoinGecko and Open-Meteo)

Transforms the data into a clean format

Loads the data into MongoDB

Prints sample outputs in the terminal

⚙️ Features

Modular ETL Design (extract, transform, load separated)

Retry and Logging Mechanism

MongoDB Integration

Supports Multiple APIs

🌐 APIs Used
API	Endpoint	Purpose
CoinGecko	/coins/markets?vs_currency=usd	Cryptocurrency market data
CoinGecko	/exchange_rates	Exchange rate information
Open-Meteo	/forecast?latitude=10&longitude=76&hourly=temperature_2m	Weather forecast (temperature)
🧩 Project Structure
publicwww_project/
│
├── extract.py         # Fetch data from APIs
├── transform.py       # Process and limit data
├── load.py            # Load data into MongoDB
├── etl_connector.py   # Main ETL workflow
├── .env               # Environment variables (API base + Mongo URI)
├── requirements.txt   # Dependencies
└── README.md          # Project documentation

⚙️ Environment Setup
Step 1: Install dependencies
pip install -r requirements.txt

Step 2: Set up .env file

Create a .env file in the project folder with the following content:

API_BASE=https://api.coingecko.com/api/v3/
MONGO_URI=mongodb://localhost:27017/publicwww


Make sure MongoDB is running locally.

Step 3: Run the ETL pipeline
python etl_connector.py


You’ll see log messages and sample data printed in the terminal.

🗄️ MongoDB Output

The data will be stored in a database named publicwww with collections:

coins_markets_vs_currency_usd

exchange_rates

weather

You can verify using:

use publicwww
show collections
db.weather.findOne()

🧾 Example Output
[INFO] Fetching coins/markets?vs_currency=usd
Inserted 100 records...
---- Sample output from coins/markets?vs_currency=usd ----
{'id': 'bitcoin', 'symbol': 'btc', ...}
----------------------------------

[INFO] Fetching weather
---- Sample output from weather ----
{'latitude': 10, 'longitude': 76, 'hourly': {...}}
----------------------------------

[INFO] ETL process completed successfully

👨‍💻 Technologies Used

Python 3

Requests (API calls)

PyMongo (MongoDB operations)

Dotenv (environment management)

Logging module (ETL logs)

📚 Author

Jothir Aditya R K.
Final Year CSE Student
Software Architecture Project – Assignment 2

