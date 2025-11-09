#!/usr/bin/env python3
"""
Brainfuck Encoder
-----------------
Prompts for plain text and generates a Brainfuck program that prints it.
"""

def encode_char(c: str) -> str:
    """
    Generate minimal Brainfuck to set the current cell to ord(c)
    and print it with '.'.
    """
    val = ord(c)
    # Use the smallest number of + or - to reach the value
    if val <= 127:
        plus = '+' * val
        minus = ''
    else:
        # For values > 127, go to 256 and subtract
        plus = '+' * (256 - (256 - val))
        minus = '-' * (256 - val)
    return f"{plus}{minus}." if minus else f"{plus}."

def encode_text(text: str) -> str:
    """
    Encode a full string into Brainfuck.
    - Start at cell 0
    - For each char: set cell to value, print, move right
    - Reset to 0 before next char (optional – keeps code tiny)
    """
    if not text:
        return ""

    parts = []
    current_cell = 0
    for i, char in enumerate(text):
        target = ord(char)

        # Move to the correct cell (only if needed)
        if i > 0:
            parts.append('>' * (i - current_cell))
            current_cell = i

        # Set the cell to the target value and print
        if target == 0:
            parts.append('[-].')  # clear and print NUL (rare)
        else:
            # Choose optimal path: +++++ or go via 256 and subtract
            if target <= 128:
                parts.append('+' * target)
            else:
                parts.append('+' * 256)
                parts.append('-' * (256 - target))
            parts.append('.')

        # Optional: zero the cell before moving on (makes code more uniform)
        # Comment next line if you want smaller code
        parts.append('[-]')

    # Move back to start (optional, for cleanliness)
    if current_cell > 0:
        parts.append('<' * current_cell)

    return ''.join(parts)


def main():
    print("\nBrainfuck Encoder\n")
    print("Enter any text (UTF-8) and get a Brainfuck program that prints it.\n")
    text = input("Text to encode: ")

    try:
        bf_code = encode_text(text)
        print("\nBrainfuck program:")
        print(bf_code)
        print(f"\nLength: {len(bf_code)} characters")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
