import random

EXIT_WORDS = ["exit", "quit", "bye", "goodbye","close"]

FALLBACK = ["Sorry, I do not understand. Type 'help' to see what I can do."
           "Hmm, I don't know that one yet. Try 'help'.",
           "I'm not sure what you mean. Type 'help' for ideas.",
           ]

responses = {
    # Greetings
    "hello": ["Hi there!", "Hello!", "Hey, nice to see you!"],
    "hi": ["Hello! How can I help you?", "Hi! What's up?"],
    "hey": ["Hey! Nice to see you."],
    "good morning": ["Good morning! Hope your day goes well."],
    "good evening": ["Good evening! How was your day?"],

    # About the bot
    "how are you": ["I'm just a program, but I'm running great!", "All systems working perfectly!"],
    "what is your name": ["I'm DecodeBot, your first rule-based chatbot."],
    "who made you": ["I was built by Kazim as part of the DecodeLabs internship."],
    "what can you do": ["I can chat, answer a few questions, and soon tell you the time."],
    "are you a robot": ["Yes, I'm a rule-based bot. Every answer I give is hard-coded."],

    # Learning and tech
    "what is ai": ["AI means making machines do tasks that normally need human intelligence."],
    "what is python": ["Python is a beginner-friendly programming language, popular in AI."],
    "what is a chatbot": ["A chatbot is a program that talks with users through text or voice."],
    "what is machine learning": ["Machine learning is when a system learns patterns from data instead of fixed rules."],

    # Small talk
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? He used up all his cache.",
    ],
    "thanks": ["You're welcome!", "Anytime!"],
    "ok": ["Great!"],

    # Help
    "help": ["Try: hello, what is your name, what is ai, tell me a joke, or type exit to leave."],
}

print("Hi! I'm DecodeBot. Type 'help' to start, or 'exit' to leave.")

while True:
    raw_input = input(" You : ask some spical question : ")
    clean_input = raw_input.lower().strip().strip("!?.,")
    
    if clean_input == "":
        print("Bot: Please type something.")
        continue
    
    if clean_input in EXIT_WORDS:
        print("Bot: Goodbye!")
        break
    
    options = responses.get(clean_input, FALLBACK)
    print("Bot:",random.choice(options))