#!/usr/bin/env python3
"""
Task 1: OpenAI SDK vs LangChain - See the Difference!
Compare the complexity of raw OpenAI SDK with LangChain's clean abstraction.

Learning Goal: Understand why LangChain simplifies AI development.
"""

import os

def raw_openai_approach():
    """Raw OpenAI SDK - complex and verbose"""
    print("\n🔴 RAW OPENAI SDK APPROACH")

    import openai

    # TODO 1: Create OpenAI client
    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),   # Replace ___ with: "OPENAI_API_KEY"
        base_url=os.getenv("OPENAI_API_BASE")   # Replace ___ with: "OPENAI_API_BASE"
    )

    # TODO 2: Make API call (notice the complexity!)
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",  # Replace ___ with: "openai/gpt-4.1-mini"
        messages=[
            {"role": "user", "content": "Explain machine learning in one sentence"}  # Replace ___ with: "user", "Explain machine learning in one sentence"
        ]
    )

    # TODO 3: Extract text (notice nested structure)
    if response:
        text = response.choices[0].message.content  # Replace ___ with: 0, content
        print(f"Response: {text[:100]}...")
        return text

    return None

def langchain_approach():
    """LangChain - clean and simple"""
    print("\n🟢 LANGCHAIN APPROACH")

    from langchain_openai import ChatOpenAI

    # TODO 4: Initialize model (so simple!)
    llm = ChatOpenAI(
        model="openai/gpt-4.1-mini",                    # Replace ___ with: "openai/gpt-4.1-mini"
        api_key=os.getenv("OPENAI_API_KEY"),      # Replace ___ with: "OPENAI_API_KEY"
        base_url=os.getenv("OPENAI_API_BASE")      # Replace ___ with: "OPENAI_API_BASE"
    )

    # TODO 5: Make the call (one line!)
    response = llm.invoke("Explain machine learning in one sentence")

    if response:
        print(f"Response: {response.content[:100]}...")
        return response.content

    return None

def main():
    print("🎯 Task 1: OpenAI SDK vs LangChain Comparison")
    print("=" * 50)

    # Run both approaches
    raw_result = raw_openai_approach()
    langchain_result = langchain_approach()

    # Show the difference
    if raw_result and langchain_result:
        print("\n📊 COMPARISON:")
        print("✅ Both approaches work, but LangChain is:")
        print("  - 70% less code")
        print("  - Cleaner response handling")
        print("  - Provider agnostic")

        # Create marker
        os.makedirs("/root/markers", exist_ok=True)
        with open("/root/markers/task1_complete.txt", "w") as f:
            f.write("COMPLETED")
        print("\n✅ Task 1 completed!")

if __name__ == "__main__":
    main()