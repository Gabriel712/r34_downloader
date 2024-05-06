"""
Returns a dict with information from the R34 API
{
    'owner':'',
    'file_url':'',
    'tags':'',
    'title':'',
    'hash':'', # This hash is defined by R34 itself - It is useful if you don't want to get the same video    
}
"""


import requests

def search_and_format_posts(search_terms):
    url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"
    params = {
        "tags": search_terms,
        "json": 1
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            posts = response.json()
            formatted_posts = []
            for post in posts:
                if post['image'].endswith('.mp4'):
                    title_tags = post['tags'].split()[-5:]
                    title = ' '.join(title_tags)
                    formatted_post = {
                        "owner": post['owner'],
                        "file_url": post['file_url'],
                        "tags": post['tags'],
                        "title": title,
                        "hash": post['hash']
                    }
                    formatted_posts.append(formatted_post)
            return formatted_posts
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", e)
        return []

# Usando a função

if __name__ == "__main__":
    search_terms = "video 9:16"
    results = search_and_format_posts(search_terms)
    if results:
        print("FIND:")
        for item in results:
            print(item)
    else:
        print("--> 0 MP4 FILES")
