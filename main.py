# Prime Numbers Calculation Script by TLIEPE
# Showcase STRUCTURED OUTPUT LLM using Instructor library (stable version) https://python.useinstructor.com/integrations/openai/
# Designed for macOS environment

import os
import openai
import instructor
from pydantic import BaseModel
import sympy

# Set the OpenAI API Key from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Define a Pydantic model to validate the response from the OpenAI API
class PrimeNumberResponse(BaseModel):
    primes: list[int]

def ask_user_limit():
    try:
        limit = int(input("Please enter the upper limit for prime numbers: "))
        if limit <= 1:
            print("The limit should be at least 2 to find prime numbers.")
            return None
        return limit
    except ValueError:
        print("Please enter a valid integer.")
        return None

def get_prime_numbers_using_openai(limit):
    try:
        client = instructor.from_openai(openai.OpenAI())
        completion = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates prime numbers."},
                {"role": "user", "content": f"Provide all prime numbers less than or equal to {limit} as a comma-separated list of integers."}
            ],
            response_model=PrimeNumberResponse,
        )
        primes = completion.primes
        # With GenAI, it can happen that a number exceeding the limit is returned (e.g., 5 for limit=3),
        # so we filter out any numbers greater than the limit here.
        return [p for p in primes if p <= limit]
    except Exception as e:
        print(f"Error using OpenAI API: {e}")
        return None

def get_prime_numbers_locally(limit):
    return list(sympy.primerange(2, limit + 1))

def format_primes_for_side_by_side_display(primes_openai, primes_local):
    max_length = max(len(primes_openai), len(primes_local))
    formatted_output = []
    for i in range(max_length):
        openai_prime = str(primes_openai[i]) if i < len(primes_openai) else ""
        local_prime = str(primes_local[i]) if i < len(primes_local) else ""
        formatted_output.append(f"OpenAI: {openai_prime:<5} | Local: {local_prime}")
    return '\n'.join(formatted_output)

def main():
    user_limit = ask_user_limit()
    if user_limit is None:
        return

    primes_openai = get_prime_numbers_using_openai(user_limit)
    if primes_openai is None:
        return

    primes_local = get_prime_numbers_locally(user_limit)

    print("\nPrime Numbers Comparison:\n")
    print(format_primes_for_side_by_side_display(primes_openai, primes_local))

    if primes_openai == primes_local:
        print("\nBoth results match!")
    else:
        print("\nThe results differ. Please verify the calculations.")

if __name__ == "__main__":
    main()
