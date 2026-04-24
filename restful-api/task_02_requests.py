import requests
import csv

def fetch_and_print_posts():
    """
    JSONPlaceholder-dən bütün postları çəkir, status kodunu 
    və bütün postların başlıqlarını (title) çap edir.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Postları çəkir və onları 'posts.csv' adlı faylda saxlayır.
    Faylda yalnız id, title və body sütunları olacaq.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Məlumatı strukturlaşdırırıq (id, title, body)
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # CSV faylına yazırıq
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)
