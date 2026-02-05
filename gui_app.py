import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from text_analysis import analyze_text

current_df = None


def run_analysis():
    global current_df
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Нет текста", "Введите текст для анализа.")
        return

    df = analyze_text(text)
    current_df = df
    for item in result_table.get_children():
        result_table.delete(item)

    for _, row in df.iterrows():
        result_table.insert(
            "",
            tk.END,
            values=(
                row["Lemma"],
                row["Wordform_Count"],
                row["Wordforms"],
            ),
        )


def clear_all():
    global current_df
    current_df = None
    input_text.delete("1.0", tk.END)
    for item in result_table.get_children():
        result_table.delete(item)


def save_to_excel():
    if current_df is None or current_df.empty:
        messagebox.showwarning("Нет данных", "Сначала выполните анализ текста.")
        return

    filepath = filedialog.asksaveasfilename(
        title="Сохранить в Excel",
        defaultextension=".xlsx",
        filetypes=[("Excel файлы", "*.xlsx")],
    )
    if not filepath:
        return

    try:
        current_df.to_excel(filepath, index=False)
    except Exception as exc:
        messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить файл: {exc}")
        return

    messagebox.showinfo("Готово", f"Файл сохранен:\n{filepath}")


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

save_button = tk.Button(button_frame, text="Сохранить в Excel", command=save_to_excel)
save_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Очистить", command=clear_all)
clear_button.pack(side="left", padx=5)

columns = ("Lemma", "Wordform_Count", "Wordforms")
result_table = ttk.Treeview(app, columns=columns, show="headings")

result_table.heading("Lemma", text="Лемма")
result_table.heading("Wordform_Count", text="Кол-во форм")
result_table.heading("Wordforms", text="Словоформы (с частью речи)")

result_table.column("Lemma", width=160, anchor="w")
result_table.column("Wordform_Count", width=100, anchor="center")
result_table.column("Wordforms", width=760, anchor="w")

scrollbar_y = ttk.Scrollbar(app, orient="vertical", command=result_table.yview)
result_table.configure(yscrollcommand=scrollbar_y.set)

result_table.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
scrollbar_y.pack(side="right", fill="y", padx=(0, 10), pady=10)

app.mainloop()
