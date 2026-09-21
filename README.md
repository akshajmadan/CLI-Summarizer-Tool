# CLI Summarizer Tool

A small Python tool that reads a text file and prints a short summary of it using the Groq API.

## How it works

1. You give it a text file
2. It reads the file
3. It sends the text to an AI model and asks for a summary
4. It prints the summary in the terminal

## Setup

```bash
pip install groq python-dotenv
```

Create a `.env` file with your Groq API key:

```
GROQ_API_KEY=your_key_here
```

## Usage

```bash
python main.py myfile.txt
```

## Built with

- Python
- Groq API (`openai/gpt-oss-120b`)
- python-dotenv
