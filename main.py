import os
import logging
from parser import parse_chat_log
from analyzer import count_messages, extract_keywords_tfidf, generate_summary

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

chat_folder = "sample_logs"
import os
import logging
from parser import parse_chat_log
from analyzer import count_messages, extract_keywords_tfidf, generate_summary

# This script processes chat logs stored in the "sample_logs" folder.
# For each text file in the folder:
# 1. It parses the chat log to separate user and AI messages.
# 2. Counts the total number of messages and separates counts for user and AI.
# 3. Extracts the top keywords from the combined messages using TF-IDF.
# 4. Generates and logs a summary of the analysis.

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

chat_folder = "sample_logs"

for file in os.listdir(chat_folder):
    if file.endswith(".txt"):
        logger.info(f"\n--- Analyzing {file} ---")
        user_msgs, ai_msgs = parse_chat_log(os.path.join(chat_folder, file))
        stats = count_messages(user_msgs, ai_msgs)
        keywords = extract_keywords_tfidf(user_msgs + ai_msgs)

        generate_summary(stats, keywords, logger)
for file in os.listdir(chat_folder):
    if file.endswith(".txt"):
        logger.info(f"\n--- Analyzing {file} ---")
        user_msgs, ai_msgs = parse_chat_log(os.path.join(chat_folder, file))
        stats = count_messages(user_msgs, ai_msgs)
        keywords = extract_keywords_tfidf(user_msgs + ai_msgs)

        generate_summary(stats, keywords, logger)
