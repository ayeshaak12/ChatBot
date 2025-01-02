from tkinter import *
from translate import Translator

# Function to translate text
def translate_text():
    source_text = source_text_box.get("1.0", END).strip()  # Get the text from the source text box
    target_language = target_language_entry.get().strip()  # Get the target language code

    if not source_text:
        result_label.config(text="Please enter text to translate.")
        return

    if not target_language:
        result_label.config(text="Please enter the target language code (e.g., 'es' for Spanish).")
        return

    try:
        # Create a Translator object
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(source_text)  # Translate the text
        result_label.config(text=translated_text)  # Display the result
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = Tk()
root.title("Language Translator")

# Source text label and text box
source_label = Label(root, text="Enter text to translate:")
source_label.pack(pady=5)
source_text_box = Text(root, height=10, width=50)
source_text_box.pack(pady=5)

# Target language label and entry
target_language_label = Label(root, text="Enter target language code (e.g., 'es' for Spanish):")
target_language_label.pack(pady=5)
target_language_entry = Entry(root, width=10)
target_language_entry.pack(pady=5)

# Translate button
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Result label
result_label = Label(root, text="", wraplength=400, justify="left", fg="blue")
result_label.pack(pady=5)

# Run the GUI
root.mainloop()
