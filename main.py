from collections import Counter
import string

STOP_WORDS = {
    'the', 'is', 'and', 'a', 'an', 'of', 'to', 'in', 'for', 'on', 'that',
    'with', 'as', 'this', 'it', 'are', 'was', 'at', 'by', 'be', 'from',
    'or', 'has', 'have', 'but', 'not', 'you', 'i', 'we', 'they', 'he',
    'she', 'them', 'his', 'her', 'its', 'my', 'our', 'your'
}

#reads the chat log file and returns its lines as a list of strings
def read_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

#parses the chat lines into separate lists for user and AI messages
def parse_chat(lines):
    user_messages = []
    ai_messages = []
    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_messages.append(line[5:].strip())
        elif line.startswith("AI:"):
            ai_messages.append(line[3:].strip())
    return user_messages, ai_messages

#tokenizes a given text by converting it to lowercase, removing punctuation and filtering out stop words
def tokenize(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return [word for word in text.split() if word not in STOP_WORDS]

#analyzes the frequency of keywords in a list of messages and returns the top N keywords
def keyword_analysis(messages, top_n=5):
    all_words = []
    for msg in messages:
        all_words.extend(tokenize(msg))
    return Counter(all_words).most_common(top_n)


def print_summary(user_msgs, ai_msgs):
    total = len(user_msgs) + len(ai_msgs)
    user_keywords = keyword_analysis(user_msgs)
    ai_keywords = keyword_analysis(ai_msgs)
    combined_keywords = keyword_analysis(user_msgs + ai_msgs)

    print("Summary:")
    print(f"- Total exchanges: {total}")
    print(f"- User messages: {len(user_msgs)}")
    print(f"- AI messages: {len(ai_msgs)}")
    print(f"- Most common keywords: {[word for word, _ in combined_keywords]}")

    if user_keywords:
        top_user_topics = ', '.join(word for word, _ in user_keywords[:3])
        print(f"- The user asked mainly about {top_user_topics}.")


if __name__ == '__main__':
    lines = read_chat("sample_logs/war.txt")
    user_msgs, ai_msgs = parse_chat(lines)
    print_summary(user_msgs, ai_msgs)