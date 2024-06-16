import requests
import re

def extract_links(url):
    response = requests.get(url)
    content = response.text

    # Define the regular expression pattern for links
    link_pattern = re.compile(r'https://cdn5\.cdn-telegram\.org/file[^\s"\'>]+')

    # Find all matches in the content
    links = re.findall(link_pattern, content)

    return links

def save_links_to_file(links, output_file):
    with open(output_file, 'w') as file:
        for link in links:
            file.write(link + '\n')

if __name__ == "__main__":
    # Specify the URL of the webpage you want to extract links from
    target_url = "https://example.com"

    # Specify the output file where you want to save the links
    output_file = "extracted_links.txt"

    # Extract links from the webpage
    extracted_links = extract_links(target_url)

    # Save the links to a text file
    save_links_to_file(extracted_links, output_file)

    print(f"Links extracted from {target_url} and saved to {output_file}")
