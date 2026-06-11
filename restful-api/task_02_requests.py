#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    da_request = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {da_request.status_code}")

    if da_request.status_code == 200:
        da_posts = da_request.json()

        for post in da_posts:
            print(post["title"])

def fetch_and_save_posts():
    da_request = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {da_request.status_code}")

    if da_request.status_code == 200:
        posts = da_request.json()

        da_posts_list = []

        for data in posts:
            post_dict = {"id": data["id"], "title": data["title"], "body": data["body"]}
            da_posts_list.append(post_dict)

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(da_posts_list)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
