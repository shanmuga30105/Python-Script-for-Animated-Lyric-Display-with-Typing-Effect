import time
import sys

def print_lyrics():
    """
    Prints the song title and then prints lyrics line by line
    with a typing effect and no pause between lines.
    """

    # --- Song Title ---
    song_title = "konte chooputho 🎶"
    print(song_title)
    print("-" * len(song_title))  # Separator line
    time.sleep(1.0)  # Short pause after title

    lyrics = [
        "Kallu raase nee kallu raase",
        "Oka chinni kavitha premenemoo",
        "Adi chadivinappudu"
    ]

    # Typing speed (delay between each character)
    CHAR_DELAY = 0.05

    time.sleep(1.5)

    # Loop through each line
    for line in lyrics:
        # Typing effect
        for char in line:
            print(char, end='', flush=True)
            time.sleep(CHAR_DELAY)
        print()  # Move to next line immediately

# Call the function
print_lyrics()
