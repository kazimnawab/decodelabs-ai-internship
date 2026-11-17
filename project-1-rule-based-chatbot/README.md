# Project 1: Rule-Based AI Chatbot

A console chatbot (**DecodeBot**) that answers using explicit, hard-coded rules instead of machine learning. Built as part of the DecodeLabs AI Internship (Batch 2026).

## Why a rule-based bot?
Rule-based systems are "white boxes": every answer can be traced from input to logic to output. There is no hallucination, which is why this approach is still used as a control layer (guardrails) around modern LLMs.

## Features
- Continuous conversation loop (`while True`)
- Input sanitization: handles upper/lower case, extra spaces, and edge punctuation
- Knowledge base: a dictionary with 15+ intents (greetings, tech questions, small talk, help)
- Random replies per intent using `random.choice()`
- Fallback replies for unknown input
- Clean exit with multiple commands: `exit`, `quit`, `bye`, `goodbye`, `close`
- Empty-input handling

## How it works (IPO model)
```
Input    -> raw text from the user, cleaned with .lower().strip()
Process  -> exit check, then dictionary lookup with .get()
Output   -> random reply from the matched intent, or a fallback
```

## Concepts practiced
`while` loops, `if` conditions, `break` / `continue`, dictionaries, lists, `.get()`, string methods, the `random` module.

## Run it
```bash
python chatbot.py
```
Requires Python 3.8 or newer. No extra libraries needed.

## Example
```
You: Hello!
Bot: Hey, nice to see you!
You: What is AI?
Bot: AI means making machines do tasks that normally need human intelligence.
You: bye
Bot: Goodbye!
```

## Limitations and next steps
Matching is exact, so the bot only understands phrases it has a rule for. Project 2 moves toward meaning-based matching.

## Author
Kazim nawab, AI Intern at DecodeLabs