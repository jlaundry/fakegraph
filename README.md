# fakegraph

Creates a fake Microsoft Graph-like API for testing applications.

This is a high-performance local development environment, primarily for testing scale. This is not designed to be a complete replica of the Graph API, nor be accurate in the data, nor precise in the request validation.

## Usage

1. Do the usual `python -m venv .env && pip install --upgrade pip && pip install -r requirements.txt` dance.
2. (if required) create a new fake dataset using `python scripts/generate-users.py` (or use the existing)
3. Run the Flask server using `flask run`
