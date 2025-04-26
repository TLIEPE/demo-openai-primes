# Prime Numbers Calculation Script by TLIEPE
# Updated to use Instructor library with OpenAI API (strict structured output) https://python.useinstructor.com/integrations/openai/
# Designed for macOS environment

import os
import openai
import instructor
from pydantic import BaseModel
from openai import OpenAIError

# Set the OpenAI API Key from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Initialize the OpenAI client with Instructor, strict validation enabled
client = instructor.from_openai(openai.OpenAI(), mode=instructor.Mode.TOOLS_STRICT)

# Pydantic model for validating the structured response
class PrimeNumberResponse(BaseModel):
    primes: list[int]

def get_prime_numbers(limit):
    """Get prime numbers up to a limit using OpenAI with strict schema validation."""
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You generate prime numbers."},
            {"role": "user", "content": f"List all prime numbers less than or equal to {limit}."}
        ],
        response_model=PrimeNumberResponse
    )
    return completion.primes

def main():
    try:
        limit = int(input("Enter the upper limit for prime numbers: "))
        primes = get_prime_numbers(limit)
        print(f"\nPrime numbers up to {limit}:\n{primes}")

    except OpenAIError as e:
        if hasattr(e, 'status_code') and e.status_code == 400:
            print("\nThe model failed to return correctly structured data (HTTP 400 Error).\n"
                  "This usually happens if the model could not strictly follow the expected format.")
        else:
            print(f"\nAn OpenAI API error occurred: {e}")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()