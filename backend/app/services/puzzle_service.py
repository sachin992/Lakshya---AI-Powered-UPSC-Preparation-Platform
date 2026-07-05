import random


QUESTION_BANK = {
    "History & Culture": [
        {
            "question": "Who was the first President of India?",
            "options": ["A) Dr. Rajendra Prasad", "B) Dr. S. Radhakrishnan", "C) C. Rajagopalachari", "D) Sardar Patel"],
            "correct": "A",
            "year": "Prelims 2018",
        }
    ],
    "All CSAT Questions": [
        {
            "question": "If all Roses are Flowers and all Flowers fade, what follows?",
            "options": ["A) All Roses fade", "B) Some Roses fade", "C) No Roses fade", "D) None"],
            "correct": "A",
            "year": "Prelims 2023",
        }
    ],
}


def create_grid(seed: str, grid_size: int, total_questions: int):
    rnd = random.Random(seed)
    positions = sorted(rnd.sample(range(grid_size * grid_size), total_questions))
    return {"grid_size": grid_size, "question_positions": positions}


def pick_question(category: str):
    bank = QUESTION_BANK.get(category) or QUESTION_BANK["All CSAT Questions"]
    return bank[0]


def score_answer(selected: str, correct: str):
    return 10 if selected == correct else 0
