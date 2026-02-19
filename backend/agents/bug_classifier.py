"""
Classifies bug types from pytest output.
"""


class BugClassifier:
    """Classifies bug types based on error text."""

    BUG_TYPES = [
        "IMPORT",
        "SYNTAX",
        "TYPE_ERROR",
        "LOGIC",
        "INDENTATION",
        "LINTING"
    ]

    def classify(self, failure_output):
        """Return detected bug types."""
        print("🧠 Classifying failures...")

        detected = set()

        text = failure_output.lower()

        if "importerror" in text or "modulenotfounderror" in text:
            detected.add("IMPORT")

        if "syntaxerror" in text:
            detected.add("SYNTAX")

        if "typeerror" in text:
            detected.add("TYPE_ERROR")

        if "indentationerror" in text:
            detected.add("INDENTATION")

        if "assert" in text:
            detected.add("LOGIC")

        if "pep8" in text or "lint" in text:
            detected.add("LINTING")

        if not detected:
            detected.add("LOGIC")

        print("Detected:", detected)
        return list(detected)
