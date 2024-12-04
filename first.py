from googletrans import Translator
import os

def read_book(file_path):
    """Reads text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_translated_text(file_path, text):
    """Saves translated text to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def translate_text(text, target_language):
    """Translates the given text to the target language."""
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    # Input and output file paths
    input_file = 'book.txt'  # Path to your book file
    output_file = 'translated_book.txt'  # Path to save the translated book
    
    # Language code (e.g., 'fr' for French, 'es' for Spanish)
    target_language = 'fr'  # Replace with your target language code
    
    if not os.path.exists(input_file):
        print("Input file does not exist!")
        return
    
    # Read the book
    book_text = read_book(input_file)
    
    # Translate the text
    print("Translating the book...")
    translated_text = translate_text(book_text, target_language)
    
    # Save the translated text
    save_translated_text(output_file, translated_text)
    print(f"Translation complete! Saved to {output_file}")

if __name__ == "__main__":
    main()
