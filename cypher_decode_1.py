from string import ascii_lowercase as letters

# palavra criptografada
word = input("Digite a palavra:")

# funcao de criar nova palavra
def letter_change(base_word,displacement=1):
    new_word=''
    for letter in base_word:
        if letter in letters:
            new_word=new_word+letters[(letters.index(letter)-displacement)%len(letters)]
        else:
            new_word+=letter
    return new_word

# criar palavras do dicionario
list_words = {move:letter_change(word,move) for move in range(1,26)}

# funcao de printar o dicionario
print(list_words)
