import requests


def read_text_file_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the content of the response
            content = response.text

            return content
        else:
            return f"Failed to retrieve the file. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
url = 'https://firebasestorage.googleapis.com/v0/b/mandir-f4935.appspot.com/o/indian_temples.txt?alt=media&token=3ef895d6-cd70-4989-a1e3-93d319019802'
content = read_text_file_from_url(url)
print(content)