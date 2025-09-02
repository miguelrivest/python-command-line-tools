import webbrowser
import argparse
from urllib.parse import quote_plus

def main():
    parser = argparse.ArgumentParser(
        description="Open a Google search in Microsoft Edge."
    )
    parser.add_argument(
        'query', nargs='*', help='Search query to open in Edge'
    )
    parser.add_argument(
        '-s', '--site', help='Specific site to search within'
    )
    args = parser.parse_args()
    search_terms = ' '.join(args.query)
    if not search_terms:
        search_terms = input("Enter search query: ")
    if args.site:
        search_terms += f" site:{args.site}"
    encoded_query = quote_plus(search_terms)
    url = "https://www.google.com/search?q=" + encoded_query
    open_in_edge(url)

def open_in_edge(url):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open(url)

if __name__ == "__main__":
    main()