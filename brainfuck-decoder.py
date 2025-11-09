#!/usr/bin/env python3
"""
Brainfuck Decoder
------------------------
Prompts for a Brainfuck program that uses '.' to print characters.
Runs it and shows the output.
"""

def run_brainfuck(code: str) -> str:
    """Execute Brainfuck code and return everything printed with '.'"""
    tape = [0] * 30000
    ptr = 0
    pc = 0
    output = []
    jump = {}
    stack = []

    # Build jump table for [ and ]
    for i, ch in enumerate(code):
        if ch == '[':
            stack.append(i)
        elif ch == ']':
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {i}")
            open_pos = stack.pop()
            jump[open_pos] = i
            jump[i] = open_pos
    if stack:
        raise SyntaxError("Unmatched '['")

    # Execute
    while pc < len(code):
        cmd = code[pc]

        if cmd == '+': tape[ptr] = (tape[ptr] + 1) & 0xFF
        elif cmd == '-': tape[ptr] = (tape[ptr] - 1) & 0xFF
        elif cmd == '>': ptr += 1
        elif cmd == '<': ptr -= 1
        elif cmd == '.': output.append(chr(tape[ptr]))
        elif cmd == '[' and tape[ptr] == 0: pc = jump[pc]
        elif cmd == ']' and tape[ptr] != 0: pc = jump[pc]

        pc += 1

    return ''.join(output)


def main():
    print("\nBrainfuck Decoder\n")
    print("Paste a Brainfuck program that prints text using '.'\n")
    code = input("Brainfuck code: ").strip()

    try:
        result = run_brainfuck(code)
        print("\nOutput:")
        print(repr(result))
        print("\nRaw (visible):")
        print(result if result else "(empty)")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
