import requests


isbn = "9780140328721"  # Matilda by Roald Dahl
book = requests.get(f"https://openlibrary.org/isbn/{isbn}.json").json()
print(book['title'], "by", book.get('by_statement', 'Unknown'))
