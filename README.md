# Movie Recommendation App

## Overview
The **Movie Recommendation App** is a Streamlit-based web application that allows users to ask movie-related questions in natural language and get relevant movie recommendations. The app utilizes Google Gemini AI to convert natural language queries into SQL commands and fetches data from a SQLite database.

## Features
- Accepts natural language questions about movies.
- Uses Google Gemini AI to generate SQL queries.
- Fetches movie data from a SQLite database.
- Displays movie recommendations based on user queries.

## Technologies Used
- **Python**: Backend programming.
- **Streamlit**: Web interface.
- **SQLite**: Database for movie records.
- **Google Gemini AI**: Converts natural language to SQL queries.
- **dotenv**: Loads environment variables.

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/your-username/MovieRecommendationApp.git
cd MovieRecommendationApp
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file and add your **Google API Key**:
```
GOOGLE_API_KEY=your_google_api_key
```

### 5. Run the application
```bash
streamlit run app.py
```

## Database Schema
The SQLite database (`movies.db`) contains a table named `MOVIES` with the following schema:
```
MOVIES (
    TITLE TEXT,
    GENRE TEXT,
    RATING REAL
)
```

## How It Works
1. User enters a question related to movies (e.g., "What are the top-rated action movies?").
2. The app uses Google Gemini AI to convert the question into an SQL query.
3. The generated SQL query is executed on the SQLite database.
4. The retrieved movie data is displayed as recommendations.

## Example Queries
| User Question | Generated SQL Query |
|--------------|----------------------|
| What is the highest rated movie? | `SELECT * FROM MOVIES ORDER BY RATING DESC LIMIT 1;` |
| What movies are in the Comedy genre? | `SELECT * FROM MOVIES WHERE GENRE='Comedy';` |
| List all action movies with a rating above 8 | `SELECT * FROM MOVIES WHERE GENRE='Action' AND RATING > 8;` |

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your fork and submit a pull request.


## Contact
For any questions or issues, reach out via GitHub or email at `shizakhurram7@gmail.com`.

