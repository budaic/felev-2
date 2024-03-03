import os
import re

def check_links_and_content(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                # Check if the file has content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if not content.strip():
                        print(f"Warning: File '{file_path}' has no content.")

                # Check links in the Markdown file
                with open(file_path, 'r', encoding='utf-8') as f:
                    md_content = f.read()

                    # Extract all URLs from the Markdown content
                    urls = re.findall(r'\[.*?\]\((.*?)\)', md_content)

                    for url in urls:
                        if url.startswith("http") or url.startswith("www"):
                            pass
                        else:
                            if('#' in url):
                                link_path, header = url.split('#', 2)
                            else:
                                link_path = url
                            linked_file_path = os.path.join(os.path.dirname(file_path), link_path)

                            if not os.path.exists(linked_file_path):
                                print(f"Error in file '{file_path}': Linked file '{linked_file_path}' does not exist.")

if __name__ == "__main__":
    directory_to_check = "../"
    check_links_and_content(directory_to_check)
