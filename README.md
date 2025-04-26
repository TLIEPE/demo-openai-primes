# Prime Numbers Calculation Script by TLIEPE


![GitHub Release (latest by date)](https://img.shields.io/github/v/release/TLIEPE/demo-openai-primes)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


## Current Version: v3

This project now uses OpenAI's strict structured output mode. 
This ensures that responses must fully comply with the expected data format. 
If the model fails to deliver correct structured data, a clear error message (HTTP 400) is shown.


## Versioning

This project maintains multiple versions:

- [v1 - Beta Structured Output Version](https://github.com/TLIEPE/demo-openai-primes/releases/tag/v1)
- [v2 - Stable Structured Output Version](https://github.com/TLIEPE/demo-openai-primes/releases/tag/v2)
- [v3 - Strict Structured Output Version](https://github.com/TLIEPE/demo-openai-primes/releases/tag/v3)

Latest release: [v3 - Strict Structured Output Version](https://github.com/TLIEPE/demo-openai-primes/releases/latest)


## Overview
This script showcases a new approach to generating **structured output** using OpenAI's stable structured outputs API (TOOLS_STRICT mode). It requests prime numbers up to a user-specified limit and validates the response format using a Pydantic model.

## How It Works
The script works as follows:

1. **API Key Setup:** The OpenAI API key is set using an environment variable named `OPENAI_API_KEY`.
2. **User Input:** The user is prompted to provide an upper limit for calculating prime numbers.
3. **OpenAI API Request:** The script sends a structured request to OpenAI, asking it to generate the prime numbers up to the user-provided limit using strict schema validation.
4. **Display:** The received list of prime numbers is displayed to the user.

## Code Flow
1. **API Key Setup** 
2. **User Input** 
3. **OpenAI API Request** 
4. **Prime Numbers Display**

## Prerequisites
Before running the script, you'll need to set up a virtual environment and install the required libraries.

### Setting up a Virtual Environment on macOS
To set up a virtual environment, follow these steps:

1. **Open Terminal**
2. Navigate to your desired directory:
   ```sh
   cd /path/to/your/project
   ```
3. Create a virtual environment named `macenv`:
   ```sh
   python3 -m venv macenv
   ```
4. Activate the virtual environment:
   ```sh
   source macenv/bin/activate
   ```
5. Install the required libraries using the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```
6. Or install the required libraries manuel:
   ```sh
   pip install openai instructor pydantic
   ```

After setting up the virtual environment and installing the libraries, you're ready to run the script.

## Running the Script
1. Make sure the virtual environment is activated (`source macenv/bin/activate`).
2. Set the OpenAI API key as an environment variable:
   ```sh
   export OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the script:
   ```sh
   python3 main.py
   ```

## Notes
- **MIT License**: This project is licensed under the MIT License, meaning you are free to use, modify, and distribute it as long as proper credit is given.

- **Strict Mode Option**: OpenAI now supports a strict mode in structured output, ensuring perfect schema compliance. This project currently uses a relaxed mode for flexibility in examples. For critical applications, enabling `strict: true` is recommended to guarantee response schema adherence.

- **Strict Mode Handling**: Version 3 introduces strict mode for structured outputs. This enforces exact schema validation. If the OpenAI model fails to generate a correct response, the script informs the user with a detailed error message instead of trying to recover or continuing silently.

## License
MIT License. See `LICENSE` for more details.

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute or have ideas for improving this project.
