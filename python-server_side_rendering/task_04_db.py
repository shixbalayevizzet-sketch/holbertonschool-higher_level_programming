#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    products = []

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


def read_sql():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()

    products = [dict(row) for row in rows]

    conn.close()
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            products = read_json()

        elif source == "csv":
            products = read_csv()

        elif source == "sql":
            products = read_sql()

        else:
            return render_template(
                "product_display.html",
                error="Wrong source"
            )

    except Exception:
        return render_template(
            "product_display.html",
            error="Database error"
        )

    if product_id:
        try:
            product_id = int(product_id)

            products = [
                product for product in products
                if int(product["id"]) == product_id
            ]

            if not products:
                return render_template(
                    "product_display.html",
                    error="Product not found"
                )

        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)
