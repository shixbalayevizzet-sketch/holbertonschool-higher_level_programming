def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    # Mətndəki qabaqcadan olan boşluqları silmək üçün
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            # Nöqtədən sonra gələn boşluqları atırıq
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
