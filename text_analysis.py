import re
import pandas as pd
import pymorphy2

def analyze_text(text: str) -> pd.DataFrame:
    morph = pymorphy2.MorphAnalyzer()
    tokens = re.findall(r"[А-Яа-яЁё-]+", text)
    rows = []
    for token in tokens:
        parses = morph.parse(token)
        best = parses[0]
        lemma = best.normal_form
        pos = best.tag.POS or "UNKN"
        wordforms = sorted({form.word for form in best.lexeme})
        rows.append(
            {
                "Word": token,
                "Lemma": lemma,
                "POS": pos,
                "Wordforms": ", ".join(wordforms),
                "Wordform_Count": len(wordforms),
            }
        )

    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    input_text = input("Введите текст для анализа: ").strip()
    if not input_text:
        raise SystemExit("Текст не введен.")
    df = analyze_text(input_text)
    print(df.to_string(index=False))
