import re


def decrypt(symbols: str, message: str, english_words: list) -> str:
    decrypted_message, score = "", 0

    for i in range(1, 26):
        decrypt_symbols = symbols[i:] + symbols[:i]
        output = ""
        for letter in message:
            if letter in symbols:
                pos = symbols.find(letter)
                output += decrypt_symbols[pos]
                continue
            output += letter

        decrypted_message_score = score_decrypted_message(output, english_words)
        if score < decrypted_message_score:
            decrypted_message = output
            score = decrypted_message_score

    return decrypted_message


def score_decrypted_message(decrypted_text: str, english_words: list):
    unique_words_count = len(set(decrypted_text.split()))
    english_word_match_score = 0
    decrypted_text = re.sub(r"[^A-Za-z ]", "", decrypted_text)
    for word in set(decrypted_text.split()):
        if word in english_words:
            english_word_match_score += 1

    return english_word_match_score / unique_words_count


def main(symbols: str):
    with open("english_text.txt", "r") as file:
        english_words = [word.strip() for word in file.read().upper().split()]
    print("Enter the encrypted caesar cipher message to hack.")
    message = input("< ").upper()
    output = decrypt(symbols, message, english_words)
    print(output)


if __name__ == "__main__":
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    main(symbols)
