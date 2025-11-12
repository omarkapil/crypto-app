# Crypto App

A web-based cryptographic application built with Flask that implements various encryption algorithms and cryptographic techniques.

## Features

This application supports the following cryptographic methods:

1. **Monoalphabetic Cipher** - Simple substitution cipher
2. **Hill Cipher** - Polygraphic substitution cipher based on linear algebra
3. **Columnar Transposition** - Transposition cipher using keyword-based column rearrangement
4. **RC4** - Rivest Cipher 4 stream cipher
5. **MAC** - Message Authentication Code using HMAC-SHA256
6. **CBC** - Cipher Block Chaining mode (AES-CBC)
7. **OFB** - Output Feedback mode (AES-OFB)
8. **CTR** - Counter mode (AES-CTR)

## Requirements

- Python 3.13+
- Flask >= 3.0.0
- pycryptodome >= 3.19.0
- numpy >= 1.26.0

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/omarkapil/crypto-app.git>
cd crypto-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select a cryptographic method from the available options
4. Enter your text in the input field
5. Click "lets go" to encrypt/process your text
6. View the result with the encrypted output and relevant keys/parameters

## Project Structure

```
crypto-app/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── crypto_modules/             # Cryptographic algorithm modules
│   ├── __init__.py
│   ├── monoalphabetic_cipher.py
│   ├── hill_cipher.py
│   ├── columnar_transposition.py
│   ├── rc4.py
│   ├── mac.py
│   ├── cbc.py
│   ├── aes_ofb.py
│   └── ctr.py
├── static/                     # Static files
│   ├── script.js              # Frontend JavaScript
│   └── style.css              # Styling
└── templates/                  # HTML templates
    └── index.html             # Main page
```

## Notes

- Some algorithms (CBC, OFB, CTR) require the `pycryptodome` library
- Hill Cipher requires `numpy` for matrix operations
- Each algorithm generates its own keys/parameters automatically
- Keys and initialization vectors (IVs) are displayed in base64 format for easy sharing


