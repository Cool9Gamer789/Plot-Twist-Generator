import sys
from openai import OpenAI

# Create the OpenRouter hub so we can use Deepseek
client = OpenAI(
    # GENERATE YOUR OWN API KEY
    api_key="",
    base_url="https://openrouter.ai/api/v1",
)

def main():
    user_summary = input("Enter a story summary: ").rstrip()
    if not user_summary.strip():
        sys.exit("No summary given.")

    # Contains the reply from Deepseek
    reply = generate_twist(user_summary)

    with open("twist.txt", "w") as file:
        lines = reply.splitlines()
        for line in lines:
            file.write(line + "\n")

def generate_twist(summary):
    # Create the response from Deepseek
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role":"system",
                "content": (
                    "You are a Professor of English at a prestigious university "
                    "that analyzes the user's summary and writes a plot twist "
                    "that would surprise the reader."
                )
            },
            {
                "role":"user",
                "content": summary
            }
        ]
    )
    # Returns the response from Deepseek
    return response.choices[0].message.content

if __name__ == "__main__":
    main()