def encrypt(symbols: str, key: int, message: str) -> str:
    encrypt_symbols = symbols[key:] + symbols[:key]
    output = ""
    for word in message:
        if word in symbols:
            pos = symbols.find(word)
            output += encrypt_symbols[pos]
            continue

        output += word

    return output


def decrypt(symbols: str, key: int, message: str) -> str:
    decrypt_symbols = symbols[key:] + symbols[:key]
    output = ""
    for word in message:
        if word in symbols:
            pos = decrypt_symbols.find(word)
            output += symbols[pos]
            continue

        output += word

    return output


def main(symbols: str):
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = ""
    while response not in ("e", "d"):
        response = input("< ")

    max_key = 25 if response == "e" else 26
    print(f"Please enter the key (0 to {max_key}) to use")
    key = ""
    while not key.isdigit() and key not in range(1, max_key + 1):
        key = input("< ")

    print("Enter the message.")
    message = input("< ").upper()

    if response == "e":
        output_message = encrypt(symbols, int(key), message)

    else:
        output_message = decrypt(symbols, int(key), message)

    print(output_message)


if __name__ == "__main__":
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    main(symbols)
