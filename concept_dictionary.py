"""
Project Athena

concept_dictionary.py
"""


class ConceptDictionary:

    def __init__(self):

        self.character = {
            "緋雪",
            "守岸人",
        }

        self.feature = {
            "黑絲",
            "白絲",
            "獸耳",
            "白髮",
            "黑髮",
        }

        self.purpose = {
            "桌布",
            "手機桌布",
        }

    def get_type(self, word):

        if word in self.character:
            return "character"

        if word in self.feature:
            return "feature"

        if word in self.purpose:
            return "purpose"

        return "unknown"