# Flask SMTP Testing App

This is a simple web application built with Flask that allows you to test SMTP credentials by sending a test email.

## Features

- Web UI to input SMTP server details.
- Sends a test email to verify the provided SMTP credentials.
- Displays success or error messages based on the result of the email sending attempt.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-smtp-testing-app.git
    cd flask-smtp-testing-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Enter the SMTP server details and email addresses, then click "Test" to send a test email.**

## File Structure

flask-smtp-testing-app/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML template for the web UI
└── README.md # This README file




## Example

1. Fill in the form with the SMTP server details:

    ```
    SMTP Server: smtp.example.com
    SMTP Port: 587
    SMTP Username: your_smtp_username
    SMTP Password: your_smtp_password
    From Email: your_email@example.com
    To Email: recipient_email@example.com
    ```

2. Click the "Test" button to send the test email.

3. The application will display a success or error message based on the result.

## Notes

- Ensure that the SMTP server and credentials provided have the necessary permissions to send emails.
- Adjust the `smtp_port` and `server.starttls()` settings in the code if your SMTP server uses different security configurations.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License.
