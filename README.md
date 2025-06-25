# Text-Processing-Project

Text Processing Project
This project demonstrates basic text processing functionality using Python. It includes both a script-based and an object-oriented implementation for tasks like counting words, filtering characters, and preprocessing short text files.

🧠 Features
Clean and filter raw text

Count words and characters

Modular design with a reusable class

Easy-to-use interface with text_processor_class.py

Simple example input (short text.txt)

📁 File Structure
text_processor.py: Functional approach to text processing.

text_processor_class.py: Class-based version for better structure and reusability.

short text.txt: Example text file for testing.

🚀 How to Use
1. Functional Version
   
```bash
python text_processor.py
```


You can import and use TextProcessor class in your own scripts:

```
from text_processor_class import TextProcessor

processor = TextProcessor("short text.txt")
processor.process()
print(processor.word_count)
```


🛠 Requirements
Python 3.6+

No external libraries required

📌 Note
This is a simple educational project and can be extended with features like:

Tokenization with nltk or spaCy

Stopword removal

Lemmatization or stemming

File I/O improvements

