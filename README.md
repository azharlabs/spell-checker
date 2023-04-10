# SpellChecker


**SpellChecker** is a Python class that uses the **PySpellChecker** library to perform spell checking and correction tasks on input text.

------------



**Installation**
To use the SpellChecker class, you must first install the **PySpellChecker** library. You can do this using pip:

`pip install pyspellchecker`

**Usage**
To use the **SpellChecker** class, you must first import it:

`from spellchecker import SpellChecker`

Next, you can create an instance of the **SpellChecker** class with an optional custom dictionary file path:


`checker = SpellChecker('path/to/custom/dictionary.txt')`
or
`checker = SpellChecker()`

To check the spelling of some text, call the **check_spelling** method on the **SpellChecker** instance:



```python
    text = "The cat in the hath is a bit fat."
    misspelled = checker.check_spelling(text)
```
	

The **check_spelling** method returns a list of **misspelled words**. You can print this list or use it for further processing:

   ```python
 print(misspelled)
```
	

To correct the spelling of some text, call the **correct_spelling** method on the **SpellChecker** instance:



```python
corrected_text = checker.correct_spelling(text)
```

The **correct_spelling** method returns the **corrected version of the input text**. You can print this text or use it for further processing:

```python
print(corrected_text)
```

To export the current dictionary used by the **SpellChecker** instance, call the **export_dictionary** method on the instance:


```python
checker.export_dictionary('path/to/export')
```

This will export the dictionary to a file at the specified path.

To import a dictionary file into the **SpellChecker** instance, call the **import_dictionary** method on the instance:


```python
checker.import_dictionary('path/to/import')
```

This will import the specified dictionary file into the **SpellChecker** instance.

------------


**Contributing**
Contributions to this project are welcome! If you find a bug or would like to suggest a new feature, please open an issue or submit a pull request.

------------


**License**
This project is licensed under the MIT License - see the LICENSE file for details.
