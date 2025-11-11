import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Use regex to find the src attribute of the iframe containing a YouTube URL
    match = re.search(r'<iframe[^>]*\s+src="(https?://(?:www\.)?youtube\.com/embed/[\w\-]+)"', s)

    if match:
        # Extract the video ID from the embed URL and convert it to a shareable URL
        url = match.group(1)
        video_id = url.split("/")[-1]  # Extract the video ID from the URL
        return f"https://youtu.be/{video_id}"  # Ensure no extra spaces

    # Return None if no valid YouTube URL is found
    return None

if __name__ == "__main__":
    main()