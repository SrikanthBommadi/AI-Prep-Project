#!/usr/bin/env python3
"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
"""

import openai
import os

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# Make a simple API call to get a response
response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[{"role": "user", "content": "What is Python in one sentence?"}]
)

# ==========================================
# THE MAGIC PATH TO THE AI'S ANSWER
# ==========================================
#
# After making an API call, the AI's text is ALWAYS at:
# response.choices[0].message.content
#
# Let's understand each part:
# ┌─────────┐     response: The complete response object from OpenAI
# │response │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .choices: List of possible responses (usually just one)
# │.choices │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     [0]: Get the first (and typically only) choice
# │  [0]    │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .message: The message object containing the response
# │.message │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The actual text string from the AI!
# │.content │
# └─────────┘
# ==========================================

# TODO: Extract the AI's text response using the exact path
# Fill in each part of the path:
ai_text = response.choices[0].message.content  # TODO: choices[0].message.content

# Display what we extracted
print("🎯 Successfully extracted the AI's response!")
print("\n" + "="*60)
print("Question: What is Python in one sentence?")
print("\nAI's Answer:")
print(ai_text)
print("="*60)

# Show the magic path one more time
print("\n🔑 THE GOLDEN PATH - Memorize this:")
print("   response.choices[0].message.content")
print("\n   This path works for EVERY chat completion response!")

# Create marker for completion tracking
os.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task4_extract_complete.txt", "w") as f:
    f.write("SUCCESS")

print("\n✅ Task 4 completed! You now know how to extract AI responses!")