from collections import defaultdict


def aggregate_results(results):

    counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    total_score = 0.0

    timeline = defaultdict(lambda: {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "score_sum": 0.0,
        "count": 0
    })

    for r in results:

        sentiment = r["sentiment"].lower()
        score = r["score"]
        date = r["date"][:10]

        counts[sentiment] += 1
        total_score += score

        timeline[date][sentiment] += 1
        timeline[date]["score_sum"] += score
        timeline[date]["count"] += 1

    timeline_list = []

    for date, values in sorted(timeline.items()):

        avg_score = 0
        if values["count"] > 0:
            avg_score = values["score_sum"] / values["count"]

        timeline_list.append({
            "date": date,
            "positive": values["positive"],
            "neutral": values["neutral"],
            "negative": values["negative"],
            "avg_score": avg_score
        })

    overall_score = total_score / len(results) if results else 0

    return counts, timeline_list, overall_score