from random import shuffle, sample

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''
cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
if digOn == 'y':
    chars += digits
if ABCon == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += punctuation
if excOn == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


def generate_password(length, chars):
    return sample(chars, length)


for i in range(1, cntPw):
    print("".join(generate_password(lenPw, chars)))
