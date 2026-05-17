import json
from flask import Flask, render_template

app = Flask(__name__)

# Əvvəlki tapşırıqdan olan marşrutlar (Home, About, Contact) bura daxildir...

@app.route('/items')
def get_items():
    try:
        # items.json faylını oxuyuruq
        with open('items.json', 'r') as file:
            data = json.load(file)
            # JSON-dan "items" siyahısını götürürük
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fayl tapılmadıqda və ya səhv olduqda boş siyahı təyin edirik
        items_list = []

    # Siyahını HTML şablonuna "items" dəyişəni olaraq göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
