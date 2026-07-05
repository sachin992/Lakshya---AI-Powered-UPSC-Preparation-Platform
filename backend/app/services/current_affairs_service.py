from datetime import date


SAMPLE_AFFAIRS = [
    {
        "id": 1,
        "title": "Quick Commerce Firms Halt 10-Minute Delivery",
        "description": "Major quick-commerce firms adjusted delivery SLAs due to logistics and compliance constraints.",
        "tags": ["Economy", "GS2-Social Justice"],
        "published_on": "2026-01-14",
    },
    {
        "id": 2,
        "title": "RBI Proposes Reopening UCB Licenses",
        "description": "RBI is considering a controlled reopening of licensing for urban co-operative banks.",
        "tags": ["Economy", "GS3-Economy"],
        "published_on": "2026-01-14",
    },
    {
        "id": 3,
        "title": "New Environmental Policy Framework Announced",
        "description": "A policy framework focuses on climate adaptation and sustainable development indicators.",
        "tags": ["Environment", "GS3-Environment"],
        "published_on": "2026-01-13",
    },
]


def list_affairs(selected_date: str | None = None, category: str | None = None):
    items = SAMPLE_AFFAIRS
    if selected_date:
        items = [item for item in items if item["published_on"] == selected_date]
    if category:
        items = [item for item in items if category in item["tags"]]
    return items


def today_iso() -> str:
    return date.today().isoformat()
