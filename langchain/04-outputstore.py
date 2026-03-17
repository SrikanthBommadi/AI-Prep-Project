#!/usr/bin/env python3
"""
Task 4: Output Parsers - From Text to Structured Data
Transform AI responses into structured formats your application can use.

Learning Goal: Extract structured data from unstructured AI responses.
"""

import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

def main():
    print("🎯 Task 4: Output Parsers - Text to Data")
    print("=" * 50)

    # Initialize LLM once for all examples
    llm = ChatOpenAI(
        model="openai/gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),
        temperature=0
    )

    # Example 1: List Parser - Simple structured data
    print("\n📋 List Output Parser")
    print("=" * 50)

    # TODO 1: Create list parser
    list_parser = CommaSeparatedListOutputParser()  # Replace ___ with: CommaSeparatedListOutputParser

    # Create prompt for list output
    list_prompt = PromptTemplate(
        template="List 3 benefits of {technology} (comma-separated):",
        input_variables=["technology"]
    )

    # TODO 2: Build chain with list parser
    list_chain =  list_prompt | llm | list_parser  # Replace ___ with: list_prompt, llm, list_parser

    # Test the list chain
    if list_chain:
        result = list_chain.invoke({
            "technology": "cloud computing"
        })
        print(f"✅ Input: 'List 3 benefits of cloud computing'")
        print(f"✅ Parsed Output: {result}")
        print(f"✅ Type: {type(result)} - It's a Python list!")
        print(f"✅ Access items: result[0] = '{result[0] if result else ''}'")

    # Example 2: JSON Output - Complex structured data
    print("\n📦 JSON Output Parser")
    print("=" * 50)

    # Create JSON parser (automatically adds format instructions)
    json_parser = JsonOutputParser()

    # Prompt that requests JSON format with auto-generated instructions
    json_prompt = PromptTemplate(
        template="""Analyze {technology} and respond with JSON containing:
        - benefits: array of 2 benefits
        - complexity: low/medium/high
        - use_case: one main use case

        Technology: {technology}

        {format_instructions}""",
        input_variables=["technology"],
        partial_variables={"format_instructions": json_parser.get_format_instructions()}
    )

    # TODO 3: Build chain for JSON output
    json_chain = json_prompt | llm | json_parser  # Replace ___ with: json_prompt, llm, json_parser

    # Test the JSON chain
    if json_chain:
        result = json_chain.invoke({
            "technology": "machine learning"
        })

        print(f"✅ Input: 'Analyze machine learning'")

        try:
            # TODO 4: JsonOutputParser returns dict directly - no parsing needed!
            parsed = result  # Replace ___ with: result (already a dict from json_parser!)

            print("✅ Parsed JSON Output:")
            print(f"   Benefits: {parsed.get('benefits', [])}")
            print(f"   Complexity: {parsed.get('complexity', 'N/A')}")
            print(f"   Use Case: {parsed.get('use_case', 'N/A')}")
            print(f"✅ Type: {type(parsed)} - It's a Python dict!")
        except (json.JSONDecodeError, TypeError, AttributeError):
            print(f"⚠️ Parsing failed (rare with JsonOutputParser): {result}")

    # Show the transformation
    print("\n💡 Parser Magic:")
    print("  ✓ List parser: Text → Python list")
    print("  ✓ JSON parser: Text → Python dict")
    print("  ✓ Direct data access: result[0], parsed['benefits']")
    print("  ✓ Ready for your application!")

    # Create marker for completion
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task4_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 4 completed! You can now parse AI outputs into data structures!")

if __name__ == "__main__":
    main()