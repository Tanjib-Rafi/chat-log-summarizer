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
    if not all_texts or all(len(text.strip()) == 0 for text in all_texts):
        return []

    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_df=0.85,
        min_df=1,
        max_features=1000,
        smooth_idf=True,
        norm='l2',
    )
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    scores = tfidf_matrix.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    ranked = sorted(zip(words, scores), key=lambda x: -x[1])

    bigram_words = set()
    bigrams = []
    unigrams = []

    for word, score in ranked:
        if " " in word:
            bigrams.append((word, score))
            bigram_words.update(word.split())
        else:
            unigrams.append((word, score))

    selected_keywords = []

    for word, _ in bigrams:
        selected_keywords.append(word)
        if len(selected_keywords) >= top_n:
            return selected_keywords

    for word, _ in unigrams:
        if word not in bigram_words:
            selected_keywords.append(word)
            if len(selected_keywords) >= top_n:
                return selected_keywords
            
    # If still fewer than top_n, fill with remaining unigrams or bigrams
    for word, _ in unigrams + bigrams:
        if word not in selected_keywords:
            selected_keywords.append(word)
            if len(selected_keywords) >= top_n:
                break

    return selected_keywords


def generate_summary(stats, keywords, logger, file_name=None):
    if not keywords:
        logger.warning(f"No keywords extracted from {file_name}")
        topic = "No Topic Found"
        logger.info("\nSummary:")
        logger.info(f"- The conversation had {stats['total']} exchanges.")
        logger.info(f"- The user asked mainly about topics related to '{topic}'.")
        return

    topic = keywords[0]

    logger.info("\nSummary:")
    logger.info(f"- The conversation had {stats['total']} exchanges.")
    if " " in topic:
        logger.info(f"- The user asked mainly about topics related to '{topic}'.")
    else:
        logger.info(f"- The user asked mainly about '{topic}' and its uses.")
    logger.info(f"- Most common keywords: {', '.join(keywords)}")


