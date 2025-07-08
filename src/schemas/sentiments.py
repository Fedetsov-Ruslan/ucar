from enum import Enum


class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


SENTIMENT_KEYWORDS = {
    "хорош": Sentiment.POSITIVE,
    "люблю": Sentiment.POSITIVE,

    "плохо": Sentiment.NEGATIVE,
    "ненавиж": Sentiment.NEGATIVE,
}
