from collections import defaultdict
from datetime import datetime


def aggregate_results(results):

    counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    timeline = defaultdict(lambda: {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    })

    for r in results:

        sentiment = r["sentiment"].lower()
        date = r["date"][:10]  # YYYY-MM-DD

        counts[sentiment] += 1
        timeline[date][sentiment] += 1

    timeline_list = []

    for date, values in sorted(timeline.items()):

        timeline_list.append({
            "date": date,
            "positive": values["positive"],
            "neutral": values["neutral"],
            "negative": values["negative"]
        })

    return counts, timeline_list