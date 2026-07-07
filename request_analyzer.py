"""
Project Athena

request_analyzer.py
"""

from dataclasses import dataclass
from typing import List

from concept_dictionary import ConceptDictionary


@dataclass
class ConceptToken:

    word: str

    concept: str


class RequestAnalyzer:

    def __init__(self):

        self.dictionary = ConceptDictionary()

    def analyze(self, text: str) -> List[ConceptToken]:

        text = text.strip()

        if not text:
            return []

        results = []

        for word in text.split():

            results.append(
                ConceptToken(
                    word=word,
                    concept=self.dictionary.get_type(word),
                )
            )

        return results