# Crypto App - User Guide

## Overview
Crypto App is a web application that provides encryption, decryption, and hashing services using various cryptographic algorithms. The application features a simple, clean interface that makes cryptographic operations easy to use.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`

## Features

### 1. Encryption
Encrypt your text using various encryption methods:
- **Monoalphabetic Cipher**: Simple substitution cipher
- **Hill Cipher**: Matrix-based encryption
- **Columnar Transposition**: Rearranges columns based on a keyword
- **RC4**: Stream cipher encryption
- **CBC**: Cipher Block Chaining mode
- **OFB**: Output Feedback mode
- **CTR**: Counter mode

### 2. Decryption
Decrypt encrypted text using:
- **Monoalphabetic Cipher**
- **RC4**
- **CBC**
- **OFB**
- **CTR**

### 3. Hashing
Generate hash values using:
- **MAC**: Message Authentication Code (HMAC-SHA256)
- **SHA-1**: Secure Hash Algorithm 1

## How to Use

### Encryption Process

1. **Start the Application**
   - Run `python app.py` in your terminal
   - Open `http://localhost:5000` in your browser

2. **Choose Operation Type**
   - Click on the **"Encryption"** button on the home page

3. **Select Encryption Method**
   - Choose from the available encryption methods
   - Click on your preferred method (e.g., "RC4", "CBC", etc.)

4. **Enter Text**
   - A popup window will appear
   - Enter the text you want to encrypt in the text area
   - Click **"Start Encryption"**

5. **View Results**
   - The encrypted text will appear in the output area
   - Copy the result for your use

### Decryption Process

1. **Navigate to Decryption**
   - Click on the **"Decryption"** button from the home page

2. **Select Decryption Method**
   - Choose the same method used for encryption
   - Click on the method (e.g., "RC4", "CBC", etc.)

3. **Enter Encrypted Text**
   - Enter the encrypted text in the popup window
   - Click **"Start Decryption"**

4. **View Results**
   - The decrypted (original) text will be displayed

### Hashing Process

1. **Navigate to Hashing**
   - Click on the **"Hashing"** button from the home page

2. **Select Hashing Method**
   - Choose either "MAC" or "SHA-1"

3. **Enter Text**
   - Enter the text you want to hash
   - Click **"Start Hashing"**

4. **View Results**
   - The hash value will be displayed
   - Note: For MAC, a key will also be generated

## Important Notes

### Encryption/Decryption Keys

- **Monoalphabetic**: Uses a seed value (default: 12345) to generate keys
- **RC4**: Uses a default key "defaultkey"
- **CBC/OFB/CTR**: These methods generate keys automatically. **Save the keys and IVs** shown in the output for decryption
- **Hill Cipher**: Generates a random key matrix (displayed in output)

### Security Considerations

- **Never share your encryption keys** with unauthorized parties
- **Save all keys and IVs** when encrypting data - you'll need them for decryption
- **Use strong, unique keys** for production environments
- **MAC keys** are randomly generated - save them if you need to verify later

### Limitations

- Some decryption methods require additional parameters (like IV for CBC/OFB)
- The current implementation uses default keys for some methods
- For production use, implement proper key management

## Troubleshooting

### Application Won't Start
- **Check Python version**: Ensure Python 3.7+ is installed
- **Install dependencies**: Run `pip install -r requirements.txt`
- **Check port**: Make sure port 5000 is not in use

### Encryption/Decryption Errors
- **Verify method match**: Use the same method for encryption and decryption
- **Check input format**: Ensure encrypted text is in the correct format (Base64, hex, etc.)
- **Verify keys**: Make sure you're using the correct keys/IVs for decryption

### Import Errors
- **Install missing packages**: Run `pip install -r requirements.txt`
- **Check Python path**: Ensure all modules are in the correct directories

## Keyboard Shortcuts

- **Ctrl + Enter**: Submit form (when typing in text area)
- **Escape**: Close modal/popup window

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Check the application logs in the terminal

## File Structure

```
crypto-app-main/
├── app.py                 # Main Flask application
├── crypto_modules/       # Cryptographic algorithms
├── templates/             # HTML templates
├── static/                # CSS and JavaScript files
├── requirements.txt       # Python dependencies
└── USER_GUIDE.md         # This file
```

## Examples

### Example 1: Encrypting Text with RC4
1. Go to Encryption → RC4
2. Enter: "Hello World"
3. Click "Start Encryption"
4. Result: Base64 encoded ciphertext

### Example 2: Hashing with SHA-1
1. Go to Hashing → SHA-1
2. Enter: "Hello World"
3. Click "Start Hashing"
4. Result: SHA-1 hash value

---

**Version**: 1.0  
**Last Updated**: 2024

