# Currency Converter Project

## Introduction
This Currency Converter is a simple Python application that allows users to convert amounts between different currencies using real-time exchange rates obtained from an external API.

## Features
- Real-time currency exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/).
- Support for multiple currencies (as provided by the API).
- User-friendly command-line interface.
- Option to include/exclude uppercase letters, numbers, and symbols in generated passwords.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- `requests` library for Python
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/)

### Installation
1. Clone the repository to your local machine:
git clone https://github.com/mobenet/currency-converter.git

2. Navigate to the cloned repository:
cd currency-converter

3. Install the required packages:
pip install -r requirements.txt


### Configuration
Before using the Currency Converter, you must obtain an API key from [ExchangeRate-API](https://www.exchangerate-api.com/). Once you have it, you can set it as an environment variable or modify the `API_URL` in the code to include your API key.

### Usage
To use the Currency Converter, run the `currency_converter.py` script and follow the on-screen instructions:
python currency_converter.py


## Contributing
Contributions to the Currency Converter project are welcome. Please ensure any pull requests or contributions adhere to the following guidelines:
- Write clean, readable code and ensure it adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.
- Include comments in your code where necessary.
- Add or update tests as appropriate.
- Update the documentation as necessary.

## License
This Currency Converter is released under the [MIT License](LICENSE).

## Contact
For any questions or comments about the Currency Converter, please open an issue on the GitHub repository

