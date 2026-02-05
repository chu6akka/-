import re
from collections import OrderedDict

import pandas as pd
import pymorphy2


def analyze_text(text: str) -> pd.DataFrame:
    morph = pymorphy2.MorphAnalyzer()
    tokens = re.findall(r"[А-Яа-яЁё-]+", text)
    lemma_data = OrderedDict()

    for token in tokens:
        parse = morph.parse(token)[0]
        lemma = parse.normal_form
        pos = parse.tag.POS or "UNKN"
        form = parse.word

        if lemma not in lemma_data:
            lemma_data[lemma] = {"count": 0, "forms": OrderedDict()}

        lemma_data[lemma]["count"] += 1
        if form not in lemma_data[lemma]["forms"]:
            lemma_data[lemma]["forms"][form] = pos

    rows = []
    for lemma, data in lemma_data.items():
        forms_with_pos = [
            f"{form} ({pos})" for form, pos in data["forms"].items()
        ]
        rows.append(
            {
                "Lemma": lemma,
                "Wordform_Count": data["count"],
                "Wordforms": ", ".join(forms_with_pos),
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    input_text = input("Введите текст для анализа: ").strip()
    if not input_text:
        raise SystemExit("Текст не введен.")
    df = analyze_text(input_text)
    print(df.to_string(index=False))
