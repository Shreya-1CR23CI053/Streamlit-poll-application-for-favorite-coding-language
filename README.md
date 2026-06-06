# Favorite Coding Language Poll

A simple and interactive Streamlit web application to poll users about their favorite coding language.

## Features

- 🗳️ Vote for your favorite coding language (Python, JavaScript, Java, Go)
- 📊 Real-time poll results visualization
- 📈 Bar chart showing vote distribution
- 💾 Persistent vote storage in JSON format
- ✨ Interactive and user-friendly interface

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### 1. Clone or Download the Project

```bash
cd Streamlit
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. Select your favorite coding language from the radio buttons
2. Click the **Vote** button to cast your vote
3. View the poll results in real-time with:
   - Vote counts per language
   - Bar chart visualization
   - Statistics (Total votes, Leading language, Top vote count)

## Project Structure

```
Streamlit/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
└── votes.json          # Stored votes (created after first vote)
```

## Dependencies

- **streamlit**: Web app framework for data scientists and ML engineers

See `requirements.txt` for version details.

## Vote Storage

Votes are automatically saved to a `votes.json` file in the project directory. This allows votes to persist between sessions.

Example `votes.json`:
```json
{
  "Python": 5,
  "JavaScript": 3,
  "Java": 2,
  "Go": 1
}
```

## Deactivating Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

### Port Already in Use
If port 8501 is already in use, run:
```bash
streamlit run main.py --server.port 8502
```

### ModuleNotFoundError
Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- Add user authentication to prevent duplicate votes
- Store votes in a database (SQLite, PostgreSQL)
- Add email notifications for results
- Create an admin dashboard to view detailed statistics

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions, please refer to the [Streamlit documentation](https://docs.streamlit.io/).
