import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

def process_file(file_path):
    output_file = os.path.splitext(file_path)[0] + '_output.csv'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        data = []
        current_character = None
        dialogue = []

        for line in lines:
            stripped_line = line.rstrip()

            if not stripped_line.startswith(' '):
                continue
            
            if stripped_line.startswith(' ' * 13):
                if current_character and dialogue:
                    data.append([current_character, '', ' '.join(dialogue)])
                    dialogue = []

                current_character = stripped_line.strip()
            
            elif stripped_line.startswith(' '):
                dialogue.append(stripped_line.strip())

        if current_character and dialogue:
            data.append([current_character, '', ' '.join(dialogue)])

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Character', '', 'Dialogue'])
            writer.writerows(data)

        messagebox.showinfo("Sukces", f"Plik CSV został zapisany jako: {output_file}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")]
    )
    if file_path:
        process_file(file_path)

root = tk.Tk()
root.title("Konwerter Scenariusza do CSV")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Wybierz plik tekstowy ze scenariuszem:")
label.pack(pady=5)

button = tk.Button(frame, text="Wybierz plik", command=select_file)
button.pack(pady=5)

root.mainloop()