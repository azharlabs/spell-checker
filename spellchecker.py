import pyspellchecker


class SpellChecker:
    """
    A class for performing spell checking and correction tasks using PySpellChecker.
    """

    def __init__(self, dictionary=None):
        """
        Initializes a new instance of the SpellChecker class.

        Args:
            dictionary (str): The path to a custom dictionary file to use, if any.
        """
        self.spell = pyspellchecker.SpellChecker()
        if dictionary:
            self.spell.load_dictionary(dictionary)

    def check_spelling(self, text):
        """
        Checks the spelling of the input text and returns a list of misspelled words.

        Args:
            text (str): The text to check for spelling errors.

        Returns:
            A list of misspelled words.
        """
        # Split the text into words
        words = text.split()

        # Use PySpellChecker to find misspelled words
        misspelled = self.spell.unknown(words)

        # Return a list of misspelled words
        return list(misspelled)

    def correct_spelling(self, text):
        """
        Corrects the spelling of the input text and returns the corrected text.

        Args:
            text (str): The text to correct the spelling of.

        Returns:
            The corrected text.
        """
        # Split the text into words
        words = text.split()

        # Use PySpellChecker to find misspelled words
        misspelled = self.spell.unknown(words)

        # Replace misspelled words with the corrected version
        for word in misspelled:
            corrected_word = self.spell.correction(word)
            text = text.replace(word, corrected_word)

        # Return the corrected text
        return text

    def export_dictionary(self, path):
        """
        Exports the current dictionary used by the SpellChecker instance to a text file.

        Args:
            path (str): The path to save the dictionary file to.
        """
        self.spell.export(path)

    def import_dictionary(self, path):
        """
        Imports a dictionary file into the SpellChecker instance.

        Args:
            path (str): The path to the dictionary file to import.
        """
        self.spell.import_dictionary(path)
