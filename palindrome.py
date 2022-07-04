# Python module to know if a string is palindrome

def in_palindrome(string: str) -> bool:
    # Return True if the string is palindrome
    string = string.replace(" ","")
    string = string.lower()
    string_reverse = string[::-1]
    return string == string_reverse

def run():
    string = int(input("Ingrese una palabra o una frase: "))
    if in_palindrome(string):
        print("Es un palindromo") 
    else:
        print("No es un palindromo")

if __name__ == '__main__':
    run()