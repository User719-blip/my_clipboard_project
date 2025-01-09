# Clipboard Sharing Web Application

This project is a web application that allows users to share clipboard data (e.g., text snippets) between devices. The application is built using HTML, CSS, JavaScript for the frontend, and FastAPI for the backend. MongoDB is used as the database to store clipboard content.

## Features

- User-friendly interface for adding and displaying clipboard content
- Responsive design for mobile and desktop use
- Real-time updates for clipboard content
- Clear all clipboard items with a single click
- Cross-device sharing of clipboard data

## Technology Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- FastAPI
- MongoDB
- Python

## Installation

### Prerequisites

- Python 3.7+
- MongoDB (local or MongoDB Atlas)
- Node.js and npm (if you choose to install frontend dependencies via npm)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/User719-blip/my_clipboard_project.git
   cd my_clipboard_project

2. Create a virtual enviroment
    ```sh
    python -m venv venv
    source venv/Scripts/activate

3. Install backend dependencies
   ```sh
   pip install -r requirements.txt

##Usage

 1.enter text into textaera and click "add" button to add clipbord content 

 2.click "refresh" button to get latest clipboard item

 3.click the "clear all" button to delete all clipboard item

##Project structure
```sh
my_clipboard_project/
├── backend/
│   ├── __init__.py
│   ├── main.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
├── .env
├── requirements.txt
├── README.md
