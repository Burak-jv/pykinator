import random

class AkinatorEngine:
    def __init__(self, knowledge):
        self.knowledge = knowledge
        self.questions = knowledge.get("questions", [])
        self.characters = knowledge.get("characters", {})

    def play(self):
        if not self.characters:
            return None

        remaining = list(self.characters.keys())
        answers = {}

        for question in self.questions:
            cevap = input(f"{question} (evet/hayır): ").strip().lower()
            answers[question] = cevap
            remaining = [name for name in remaining if self.characters[name].get(question) == cevap]

            if len(remaining) == 1:
                return remaining[0]

        if remaining:
            return random.choice(remaining)

        return None

    def learn_new_character(self, name):
        yeni_karakter = {}
        for question in self.questions:
            cevap = input(f"{question} (evet/hayır): ").strip().lower()
            yeni_karakter[question] = cevap
        self.characters[name] = yeni_karakter
