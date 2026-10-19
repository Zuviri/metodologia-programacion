# ======================================================================
# PORTADA
# ======================================================================
# Nombre:    Emiliano Zuviri Castillo
# Matrícula: 2630326
# Grupo:     IM 1-2
# Materia:   Metodología de la Programación
# Repositorio de GitHub: https://github.com/Zuviri/metodologia-programacion.git

# ======================================================================
# RESUMEN EJECUTIVO
# ======================================================================
# Un string es un texto guardado en una variable, por ejemplo "hola".
# En Python un string no se puede cambiar por dentro: si usamos lower()
# o replace(), Python crea un texto nuevo. Con los strings podemos medir
# su longitud (len), unir textos (+), tomar partes (slicing), buscar
# (find, in), reemplazar (replace), separar palabras (split) y unirlas
# (join). Antes de poder usar un texto que escribe el usuario conviene
# limpiarlo con strip() y lower() y revisar que no este vacio para
# evitar errores. En este documento resuelvo 6 problemas. Cada uno
# tiene su descripción, entradas, salidas, validaciones, 3 casos de
# prueba y el código.

# ======================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ======================================================================
# - Los strings no se cambian por dentro: cada cambio crea un texto nuevo.
# - Limpiar la entrada con strip() y lower() antes de comparar.
# - No usar números sueltos en el código: se guardan en constantes.
# - Usar los métodos de string que ya existen.
# - Validar primero que no esté vacío y después el formato.
# - Usar nombres de variables claros y mensajes de error entendibles.

# ======================================================================
# CONSTANTS
# ======================================================================
MIN_NAME_WORDS = 2
MIN_PHRASE_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30


# ======================================================================
# PROBLEM 1: Full name formatter (name + initials)
# ======================================================================
# Description: Receives a full name, removes the extra spaces, shows it
#   in Title Case and shows the initials (example: J.C.T.).
#
# Inputs:
# - full_name
#
# Outputs:
# - "Formatted name: <name>"
# - "Initials: <initials>"
#
# Validations:
# - Not empty after strip().
# - At least two words.
#
# Test cases:
# 1) Normal: "emiliano zuviri castillo"  Formatted name: Emiliano Zuviri Castillo / Initials:E.Z.C
# 2) Border: "  ANA   lAVA  "    Formatted name: Ana Lava/ Initials: A.L.
# 3) Error:  "Juan"               Error: invalid input

print("--- Problem 1: Full name formatter ---")
full_name = input("Enter full name: ")
full_name = full_name.strip()
words = full_name.split()

if full_name == "":
    print("Error: invalid input")
elif len(words) < MIN_NAME_WORDS:
    print("Error: invalid input")
else:
    formatted_name = " ".join(words).title()
    initials = ""
    for word in words:
        initials = initials + word[0].upper() + "."
    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# ======================================================================
# PROBLEM 2: Simple email validator
# ======================================================================
# Description: Checks if an email has exactly one '@', at least one '.'
#   after the '@' and no spaces. If it is valid, it shows the domain.
#   I also check that there is some text before the '@'.
#
# Inputs:
# - email_text
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain>"
#
# Validations:
# - Not empty after strip().
# - Exactly one '@'.
# - No spaces.
#
# Test cases:
# 1) Normal: "juan@gmail.com"   Valid email: true / Domain: gmail.com
# 2) Border: "a@b.c"            Valid email: true / Domain: b.c
# 3) Error:  "juan@@gmail.com"  Valid email: false
#    Also: "   " (only spaces)  Error: invalid input

print("--- Problem 2: Simple email validator ---")
email_text = input("Enter email: ")
email_text = email_text.strip()

if email_text == "":
    print("Error: invalid input")
else:
    is_valid = True

    if " " in email_text:
        is_valid = False
    if email_text.count("@") != 1:
        is_valid = False

    if is_valid:
        at_position = email_text.find("@")
        domain_part = email_text[at_position + 1:]  # text after the '@'
        if at_position == 0:  # there is nothing before the '@'
            is_valid = False
        if "." not in domain_part:
            is_valid = False

    if is_valid:
        print("Valid email: true")
        print("Domain:", domain_part)
    else:
        print("Valid email: false")


# ======================================================================
# PROBLEM 3: Palindrome checker
# ======================================================================
# Description: Checks if a phrase reads the same forwards and backwards,
#   ignoring spaces and uppercase/lowercase.
#   Limitation: commas, dots and accents are not removed.
#
# Inputs:
# - phrase
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - "Normalized phrase: <text>"
#
# Validations:
# - Not empty after strip().
# - At least 3 characters after removing the spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina"  Is palindrome: true
# 2) Border: "Aba"                 Is palindrome: true
# 3) Error:  "ab"                  Error: invalid input
#    Also: "Hola mundo" -> Is palindrome: false

print("--- Problem 3: Palindrome checker ---")
phrase = input("Enter a phrase: ")
clean_phrase = phrase.strip().lower().replace(" ", "")

if len(clean_phrase) < MIN_PHRASE_LENGTH:  # this also covers an empty phrase
    print("Error: invalid input")
else:
    reversed_phrase = clean_phrase[::-1]  # [::-1] reads the text backwards
    if clean_phrase == reversed_phrase:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")
    print("Normalized phrase:", clean_phrase)


# ======================================================================
# PROBLEM 4: Sentence word stats
# ======================================================================
# Description: Splits a sentence into words and shows how many words it
#   has, the first and last word, and the shortest and longest word.
#   If two words have the same length, the first one is shown.
#   Commas and dots count as part of the word.
#
# Inputs:
# - sentence
#
# Outputs:
# - "Word count: <n>"
# - "First word: <word>"
# - "Last word: <word>"
# - "Shortest word: <word>"
# - "Longest word: <word>"
#
# Validations:
# - Not empty after strip().
# - At least one word after split().
#
# Test cases:
# 1) Normal: "The quick brown fox"  Word count: 4 / First: The / Last: fox
#            / Shortest: The / Longest: quick
# 2) Border: "Hello"                Word count: 1 / all the words are Hello
# 3) Error:  "     "                Error: invalid input

print("--- Problem 4: Sentence word stats ---")
sentence = input("Enter a sentence: ")
sentence_words = sentence.strip().split()

if len(sentence_words) == 0:
    print("Error: invalid input")
else:
    shortest_word = sentence_words[0]
    longest_word = sentence_words[0]
    for word in sentence_words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
    print("Word count:", len(sentence_words))
    print("First word:", sentence_words[0])
    print("Last word:", sentence_words[-1])
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ======================================================================
# PROBLEM 5: Password strength classifier
# ======================================================================
# Description: Classifies a password as weak, medium or strong using
#   simple rules about its length and the type of characters it has.
#
# Rules:
# - strong: 8 or more characters with an uppercase letter, a lowercase
#   letter a digit and a symbol (like ! @ #).
# - medium: 8 or more characters, with uppercase and lowercase letters
#   together, or with a digit.
# - weak: anything else.
#
# Inputs:
# - password_input
#
# Outputs:
# - "Password strength: weak", "Password strength: medium"
#   or "Password strength: strong"
#
# Validations:
# - Not empty (a password with only spaces is also rejected).
# - The length is checked with len().
#
# Test cases:
# 1) Normal: "Str0ng#Pass" -> Password strength: strong
# 2) Border: "Abcdef12"    -> Password strength: medium (exactly 8 characters)
# 3) Error:  ""            -> Error: invalid input
#    Also: "abc" -> Password strength: weak

print("--- Problem 5: Password strength classifier ---")
password_input = input("Enter a password: ")

if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character != " ":
            has_symbol = True

    is_long_enough = len(password_input) >= MIN_PASSWORD_LENGTH

    if is_long_enough and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif is_long_enough and (has_digit or (has_upper and has_lower)):
        print("Password strength: medium")
    else:
        print("Password strength: weak")


# ======================================================================
# PROBLEM 6: Product label formatter
# ======================================================================
# Description: Builds the text "Product: <name> | Price: $<price>" with
#   exactly 30 characters. If it is shorter, spaces are added at the
#   end. If it is longer, it is cut at 30 characters.
#
# Inputs:
# - product_name
# - price_text
#
# Outputs:
# - 'Label: "<30 characters>"' (the quotes "" show the spaces)
# - "Length: 30"
#
# Validations:
# - product_name is not empty after strip().
# - price_text is a number greater than zero.
#
# Test cases:
# 1) Normal: "Pen", "12.5"   -> "Product: Pen | Price: $12.5   " (3 spaces added)
# 2) Border: "Pencil", "9.99" -> "Product: Pencil | Price: $9.99" (exactly 30)
# 3) Error:  "Pen", "abc"    -> Error: invalid input
#    Also: "Wireless Keyboard", "49.99" -> "Product: Wireless Keyboard | P" (cut)

print("--- Problem 6: Product label formatter ---")
product_name = input("Enter product name: ")
price_text = input("Enter price: ")
product_name = product_name.strip()
price_text = price_text.strip()

if product_name == "":
    print("Error: invalid input")
elif not price_text.replace(".", "", 1).isdigit():  # only digits and one dot
    print("Error: invalid input")
elif float(price_text) <= 0:
    print("Error: invalid input")
else:
    label = "Product: " + product_name + " | Price: $" + price_text
    if len(label) > LABEL_LENGTH:
        label = label[:LABEL_LENGTH]
    else:
        label = label + " " * (LABEL_LENGTH - len(label))
    print('Label: "' + label + '"')
    print("Length:", len(label))


# ======================================================================
# CONCLUSIONES
# ======================================================================
# Los strings sirven para leer y mostrar datos porque lo que escribe el
# usuario llega como texto. strip() quita espacios de mas, lower() y
# title() igualan las letras, split() separa palabras y join() las une.
# tiene uno que limpiar el texto antes de compararlo, porque "Ana" y "ana "
# serían distintos para python. Checar las entradas evita errores.
# Aprendi que un string no se cambia por dentro y que los slices
# ([a:b] y [::-1]) toman partes del texto o lo leen al reves.


# ======================================================================
# REFERENCIAS
# ======================================================================
# 1) W3Schools. Python Strings.
#    https://www.w3schools.com/python/python_strings.asp
# 2) W3Schools. Python String Methods.
#    https://www.w3schools.com/python/python_ref_string.asp
# 3) Platzi. Métodos de strings en Python: domina el poder de las cadenas de texto.
#    https://platzi.com/blog/metodos-de-strings-en-python-domina-el-poder-de-las-cadenas-de-texto/
# 4) DataCamp. Python String Tutorial.
#    https://www.datacamp.com/tutorial/python-string-tutorial
# 5) sajjadrahman56. String in Python. DEV Community.
#    https://dev.to/sajjadrahman56/string-in-python-2-2blb