
# Url Analyzer Tool

Check the security status of any website with this URL Analyzer Tool, built using React and Flask.

## Features

- **HTTPS Status**: Verify if a website is served securely over HTTPS.
- **SSL Certificate Validity**: Check the validity of the SSL certificate.
- **Security Headers**: Ensure essential security headers are properly configured.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/URL-Analyzer.git
   cd URL-Analyzer
   ```

2. **Install dependencies**:

   - Backend (Flask):
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   
   - Frontend (React):
     ```bash
     cd frontend
     npm install
     ```

3. **Start the backend server**:

   ```bash
   cd backend
   python app.py
   ```

4. **Start the frontend development server**:

   ```bash
   cd frontend
   npm start
   ```

5. **Open your browser**:

   Visit `http://localhost:3000` to use the Website Security Checker.

## Usage

1. Enter the URL of the website you want to check in the input field.
2. Click on the "Check Security" button.
3. View the results including HTTPS status, SSL certificate validity, security headers, and a security rating on a scale of 1-10.

## Technologies Used

- **Frontend**: React, JavaScript, HTML, CSS
- **Backend**: Flask (Python)
- **Additional Tools**: Axios, Bootstrap (for styling)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Acknowledgments

- This project was inspired by the need to easily assess website security for personal and small business websites.
