import os
import logging
from parser import parse_chat_log
from analyzer import count_messages, extract_keywords_tfidf, generate_summary

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

chat_folder = "sample_logs"

for file in os.listdir(chat_folder):
    if file.endswith(".txt"):
        logger.info(f"\n--- Analyzing {file} ---")
        try:
            user_msgs, ai_msgs = parse_chat_log(os.path.join(chat_folder, file))
        except Exception as e:
            logger.error(f"Error parsing {file}: {e}")
            continue

        if not user_msgs and not ai_msgs:
            logger.warning(f"{file} is empty or contains no valid messages. Skipping.")
            continue

        stats = count_messages(user_msgs, ai_msgs)

        if not (user_msgs + ai_msgs):
            logger.warning(f"No valid content in {file} to extract keywords. Skipping.")
            keywords = []
        else:
            try:
                keywords = extract_keywords_tfidf(user_msgs + ai_msgs)
            except ValueError as e:
                logger.error(f"Error extracting keywords from {file}: {e}")
                keywords = []

        generate_summary(stats, keywords, logger, file_name=file)