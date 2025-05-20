from sklearn.feature_extraction.text import TfidfVectorizer

# Counts the total number of messages and separates counts for user and AI messages
def count_messages(user_msgs, ai_msgs):
    return {
        "total": len(user_msgs) + len(ai_msgs),
        "user": len(user_msgs),
        "ai": len(ai_msgs)
    }

# Extracts the top N keywords from a list of texts using TF-IDF scoring
def extract_keywords_tfidf(all_texts, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    scores = tfidf_matrix.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    ranked = sorted(zip(words, scores), key=lambda x: -x[1])
    return [word for word, _ in ranked[:top_n]]

def generate_summary(stats, keywords, logger):
    topic = keywords[0] if keywords else "various topics"

    logger.info("\nSummary:")
    logger.info(f"- The conversation had {stats['total']} exchanges.")
    logger.info(f"- The user asked mainly about {topic} and its uses.")
    logger.info(f"- Most common keywords: {', '.join(keywords)}.")


