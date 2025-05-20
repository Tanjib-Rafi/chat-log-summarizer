def parse_chat_log(file_path):
    """
    Parses a chat log file and separates messages into user and AI messages.

    Args:
        file_path (str): The path to the chat log file.

    Returns:
        tuple: A tuple containing two lists:
            - user_messages: List of messages from the user.
            - ai_messages: List of messages from the AI.
            - Ex. 
            (
                ["Hello!", "Can you explain what the India-Pakistan conflict is?", etc..........],
                ["i! How can I assist you today?", "Certainly! The India-Pakistan conflict refers to the long-standing geopolitical and military tensions between India and Pakistan, primarily over the Kashmir region. It began after the partition of British India in 1947 and has led to several wars, skirmishes, and ongoing political disputes.", etc........]
            )
    """
    user_messages = []
    ai_messages = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line.replace("User:", "").strip())
            elif line.startswith("AI:"):
                ai_messages.append(line.replace("AI:", "").strip())
    return user_messages, ai_messages