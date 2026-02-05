import tkinter as tk
from tkinter import messagebox, ttk

from text_analysis import analyze_text


def run_analysis():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Нет текста", "Введите текст для анализа.")
        return

    df = analyze_text(text)
    for item in result_table.get_children():
        result_table.delete(item)

    for _, row in df.iterrows():
        result_table.insert(
            "",
            tk.END,
            values=(
                row["Word"],
                row["Lemma"],
                row["POS"],
                row["Wordform_Count"],
                row["Wordforms"],
            ),
        )


def clear_all():
    input_text.delete("1.0", tk.END)
    for item in result_table.get_children():
        result_table.delete(item)


app = tk.Tk()
app.title("Анализатор текста")
app.geometry("1100x700")

input_label = tk.Label(app, text="Введите текст для анализа:")
input_label.pack(anchor="w", padx=10, pady=(10, 0))

input_text = tk.Text(app, height=8, wrap="word")
input_text.pack(fill="x", padx=10, pady=5)

button_frame = tk.Frame(app)
button_frame.pack(fill="x", padx=10, pady=5)

analyze_button = tk.Button(button_frame, text="Анализировать", command=run_analysis)
analyze_button.pack(side="left")

clear_button = tk.Button(button_frame, text="Очистить", command=clear_all)
clear_button.pack(side="left", padx=5)

columns = ("Word", "Lemma", "POS", "Wordform_Count", "Wordforms")
result_table = ttk.Treeview(app, columns=columns, show="headings")

result_table.heading("Word", text="Слово")
result_table.heading("Lemma", text="Лемма")
result_table.heading("POS", text="Часть речи")
result_table.heading("Wordform_Count", text="Кол-во форм")
result_table.heading("Wordforms", text="Словоформы")

result_table.column("Word", width=120, anchor="w")
result_table.column("Lemma", width=120, anchor="w")
result_table.column("POS", width=100, anchor="w")
result_table.column("Wordform_Count", width=100, anchor="center")
result_table.column("Wordforms", width=600, anchor="w")

scrollbar_y = ttk.Scrollbar(app, orient="vertical", command=result_table.yview)
result_table.configure(yscrollcommand=scrollbar_y.set)

result_table.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
scrollbar_y.pack(side="right", fill="y", padx=(0, 10), pady=10)

app.mainloop()
