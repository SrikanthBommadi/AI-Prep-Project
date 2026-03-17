# Lab 2: LangChain Fundamentals - Code Files

## 🎯 Learning Objectives
Master LangChain fundamentals by building flexible AI systems that can switch between providers, use templates, parse structured data, and chain operations together for TechCorp's support system.

## 📁 Lab Files

### 1. **verify_environment.py**
- **Purpose**: Validates LangChain and dependencies are properly installed
- **What it does**: Checks Python environment, LangChain installation, and API connectivity
- **Run first**: Essential pre-flight check before starting exercises
- **Creates**: `/root/markers/environment_verified.txt` on success

### 2. **task_1_openai_vs_langchain.py**
- **Learning Goal**: Understand why LangChain simplifies AI development
- **Skills**:
  - Compare raw OpenAI SDK complexity with LangChain simplicity
  - See 70% code reduction with LangChain abstraction
  - Understand provider-agnostic benefits
- **Key Concepts**: OpenAI client vs ChatOpenAI, response handling, abstraction benefits
- **TODO Tasks**: 5 tasks comparing both approaches

### 3. **task_2_multi_model.py**
- **Learning Goal**: Experience provider flexibility without code changes
- **Skills**:
  - Test OpenAI GPT-4.1-mini model
  - Test Google Gemini-2.5-flash model
  - Test X.AI Grok-code-fast-1 model
  - Compare all models side-by-side for A/B testing
- **Key Concepts**: One interface for multiple providers, model switching, comparison
- **TODO Tasks**: 4 tasks to test and compare multiple AI providers

### 4. **task_3_prompt_templates.py**
- **Learning Goal**: Master prompt templates for consistent, reusable prompts
- **Skills**:
  - Create customer support templates with variables
  - Build technical issue troubleshooting templates
  - Design billing inquiry templates
  - Test templates with actual LLM
- **Key Concepts**: PromptTemplate, input_variables, template formatting, variable injection
- **TODO Tasks**: 4 tasks to create dynamic TechCorp support templates

### 5. **task_4_output_parsers.py**
- **Learning Goal**: Extract structured data from unstructured AI responses
- **Skills**:
  - Use StrOutputParser for clean text output
  - Use CommaSeparatedListOutputParser for Python lists
  - Get JSON output via prompt engineering
  - Build chains with parsers using pipe operator
- **Key Concepts**: Output parsers, chain composition, structured data extraction
- **TODO Tasks**: 5 tasks to parse AI outputs into strings, lists, and JSON

### 6. **task_5_complete_chain.py**
- **Learning Goal**: Master chain composition with the pipe operator (|)
- **Skills**:
  - Build support chains for customer assistance
  - Create analysis chains for issue categorization
  - Generate solution chains with list output
  - Detect urgency with simple chains
  - Combine all chains into complete support system
- **Key Concepts**: Chain composition, pipe operator, modular components, data flow
- **TODO Tasks**: 4 tasks to build TechCorp's complete support pipeline

## 🚀 How to Use These Files

1. **Environment Check**: Start with `python verify_environment.py`
2. **Sequential Learning**: Complete tasks 1-5 in order - each builds on previous concepts
3. **Interactive Navigation**:
   - Select files from VS Code explorer
   - Use `Ctrl+G` (Windows/Linux) or `Cmd+G` (Mac) to jump to line numbers
4. **TODO Format**: Look for `___` placeholders to fill in
5. **Validation**: Each task creates a marker file on successful completion

## 💡 Key Learning Points

### Task 1: OpenAI vs LangChain
- Raw OpenAI SDK requires 10+ lines of boilerplate
- LangChain achieves same result in 3 lines
- Provider abstraction prevents vendor lock-in

### Task 2: Multi-Model Support
- Same `ChatOpenAI` class works with ALL providers
- Just change the model name - no other code changes
- Perfect for A/B testing and model comparison

### Task 3: Prompt Templates
- No more hardcoded customer names or issues
- Reusable templates with `{placeholders}`
- Consistent prompts across your team

### Task 4: Output Parsers
- Transform unstructured text into structured data
- String, list, and JSON outputs
- Chain composition with `prompt | llm | parser`

### Task 5: Chain Composition
- Connect components with the pipe operator `|`
- Build complete systems in one line
- Modular, reusable, and maintainable

## 🏗️ Architecture Pattern

```
Input → Prompt Template → LLM → Parser → Output
           ↑                ↓
           └─ One Line Chain with | operator
```

## 🔧 Troubleshooting Tips

- **Import errors**: Ensure virtual environment is activated
- **API failures**: Verify `OPENAI_API_KEY` and `OPENAI_API_BASE` are set
- **Chain errors**: Check that all `___` placeholders are filled correctly
- **No output**: Ensure each component is properly connected with `|`

## 📊 Progress Tracking

Each completed task creates a marker file:
- `/root/markers/environment_verified.txt` - Environment ready
- `/root/markers/task1_complete.txt` - OpenAI vs LangChain comparison done
- `/root/markers/task2_complete.txt` - Multi-model testing complete
- `/root/markers/task3_complete.txt` - Prompt templates mastered
- `/root/markers/task4_complete.txt` - Output parsing learned
- `/root/markers/task5_complete.txt` - Chain composition achieved

## 🎉 What You'll Achieve

By completing this lab, you'll:
- ✅ Understand why LangChain beats raw SDK approaches
- ✅ Switch between AI providers with zero code changes
- ✅ Create reusable prompt templates for any scenario
- ✅ Parse AI responses into usable data structures
- ✅ Build complete AI systems with chain composition

Ready to master LangChain fundamentals! 🚀