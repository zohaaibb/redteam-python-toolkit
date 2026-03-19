# website_checker.py 
# A Banner Grabbing Script Which is essential for Information Gathering 
# A tool to check if websites are up and gather information about them
# Uses the requests library for HTTP requests

import requests
# Import the requests library which lets us send HTTP requests
# This is like opening a browser but from Python

# List of targets to check
# Each URL will be tested in order
targets = [
    "http://www.google.com",      # Google (HTTP version)
    "http://www.facebook.com",    # Facebook (HTTP version)
    "https://www.tesla.com"       # Tesla (HTTPS - secure version)
]

def check_website(url):
    """
    Check if a website is reachable and gather information about it.
    
    Args:
        url (str): The website URL to check (e.g., "https://google.com")
    
    Returns:
        None: This function prints results but doesn't return anything
    """
    
    try:
        # Try to send a GET request to the URL
        # timeout=5 means: wait max 5 seconds for a response
        # If no response in 5 seconds, raise a Timeout exception
        response = requests.get(url, timeout=5)
        
        # Check the HTTP status code
        # 200 = OK (success)
        # 404 = Not Found (page doesn't exist)
        # 403 = Forbidden (page exists but access denied)
        # 301/302 = Redirects (page moved)
        if response.status_code == 200:
            # Website is up and returned successfully
            # Include the URL in the output so we know which site we're talking about
            print(f" [+] {url} is UP")
            
            # Get the Server header if it exists
            # The .get() method with 'Unknown' as default means:
            # If 'Server' header exists, show it
            # If not, show 'Unknown' instead of None
            server = response.headers.get('Server', 'Unknown')
            print(f"     Server: {server}")
            
            # Show how big the page is (length of HTML content)
            # len() counts characters in the response text
            print(f"     Page Length: {len(response.text)} bytes")
            
            # Extract and display the page title
            # Call our custom function to find the title in HTML
            title = extract_title(response.text)
            
            # Check if title exists (not None) before using it
            # This prevents crashes if title extraction fails
            if title:
                print(f"     Title: {title}")
            else:
                print(f"     Title: Not found")
            
            # EXTRA FEATURE: Show how long the request took
            # response.elapsed is a timedelta object
            # .total_seconds() converts to seconds
            # :.3f formats to 3 decimal places
            print(f"     Response time: {response.elapsed.total_seconds():.3f} seconds")
            
        else:
            # Website returned an error status code (not 200)
            # Show the URL and what status code we got
            print(f" [-] {url} returned {response.status_code}")
    
    # Handle specific exceptions that might occur
    except requests.exceptions.ConnectionError:
        # This happens when:
        # - DNS lookup fails (site doesn't exist)
        # - Network is down
        # - Server refuses connection
        print(f" [!] Connection Failed - {url} is down or doesn't exist")
    
    except requests.exceptions.Timeout:
        # This happens when:
        # - Server exists but takes longer than 5 seconds to respond
        # - Network is slow
        print(f" [!] {url} - Connection Timed out (took >5 seconds)")
    
    except Exception as e:
        # This catches ANY other error not caught above
        # e contains the actual error message
        # Examples: SSL errors, invalid URLs, weird protocols
        print(f" [!] {url} - Error: {e}")
    
    # Print a separator line for readability between sites
    print("-" * 50)


def extract_title(html):
    """
    Extract the title from HTML content.
    
    Args:
        html (str): The HTML content of a webpage
    
    Returns:
        str or None: The page title if found, None otherwise
    """
    
    # Find where the opening <title> tag starts
    # .find() returns the index (position) where <title> begins
    # If not found, it returns -1
    start = html.find("<title>")
    
    # Find where the closing </title> tag starts
    end = html.find("</title>")
    
    # Check if BOTH tags were found
    # start != -1 means <title> exists
    # end != -1 means </title> exists
    if start != -1 and end != -1:
        # The title content starts AFTER the 7 characters of "<title>"
        # "<title>" is 7 chars: < t i t l e >
        # So if <title> starts at position 10, content starts at 17
        # html[start+7:end] slices from start+7 to end
        # Example: html[17:25] gets characters at positions 17 through 24
        return html[start+7:end]
    
    # If either tag wasn't found, return None
    # None means "no title found" - the caller should check for this
    return None


# Main program starts here
print("=" * 50)
print("Starting Website Checks")
print("=" * 50)

# Loop through each URL in our targets list
# For each URL, call the check_website function
for site in targets:
    check_website(site)

# All done
print("=" * 50)
print("All checks complete")
print("=" * 50)
