import os
import requests
import yaml

# Semantic Scholar API base URL
API_URL = "https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"

# Replace with your Semantic Scholar author ID
AUTHOR_ID = "1796269096"
OUTPUT_DIR = "_publications"

# Fetch publications from Semantic Scholar API
def fetch_publications(author_id):
    params = {
        "fields": "title,venue,year,url,abstract"
    }
    response = requests.get(API_URL.format(author_id=author_id), params=params)
    response.raise_for_status()
    return response.json()["data"]

# Generate Markdown files for publications
def generate_markdown(publications):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    for pub in publications:
        filename = f"{pub['authors'][0]['name'].split()[-1].lower()}{pub['year']}{pub['title'].replace(' ', '-').lower()}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        front_matter = {
            "title": pub["title"],
            "collection": "publications",
            "permalink": f"/publication/{filename[:-3]}",
            "year": pub['year'],
            "venue": pub.get("venue", ""),
            "authors": ", ".join([author["name"] for author in pub["authors"]]),
            "paperurl": pub.get("url", ""),
            "excerpt": pub.get("abstract", "")
        }
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(front_matter, f, default_flow_style=False)
            f.write("---\n\n")

# Main function
def main():
    publications = fetch_publications(AUTHOR_ID)
    generate_markdown(publications)
    print(f"Generated {len(publications)} publication files in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
