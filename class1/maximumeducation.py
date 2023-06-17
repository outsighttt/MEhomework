def is_palindrome(string):
    return string == string[::-1]

while True:
    string = input('Введите слово, которое хотите проверить: ')
    print(is_palindrome(string))