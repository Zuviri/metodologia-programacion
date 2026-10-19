# ======================================================================
# PORTADA
# ======================================================================
# Nombre:    Emiliano Zuviri Castillo
# Matrícula: 2630326
# Grupo:     IM 1-2
# Materia:   Metodología de la Programación
# Repositorio de GitHub: https://github.com/Zuviri/metodologia-programacion

# ======================================================================
# RESUMEN EJECUTIVO
# ======================================================================
# Una lista (list) guarda varios datos en orden, se escribe con corchetes
# [ ] y se puede cambiar: agregar, quitar o modificar elementos "es
# mutable". Una tupla (tuple) también guarda datos en orden se escribe
# con paréntesis ( ) pero no se puede cambiar después de crearla "es
# inmutable" por eso sirve para datos fijos como las coordenadas de un
# punto. Por indicación de Charly, en esta tarea no se usan
# diccionarios:  De los problemas 3 a 6 se resuelven con listas y tuplas.
# Este documento tiene 6 problemas con su descripción, entradas, salidas,
# validaciones, 3 casos de prueba y el código.

# ======================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ======================================================================
# - Usar listas cuando se necesite agregar o quitar elementos seguido.
# - Usar tuplas para datos que no deben cambiar, como un punto (x, y).
# - Evitar modificar una lista mientras se recorre con un for.
# - Cuando dos datos van juntos (nombre y precio), guardarlos en una
#   tupla o en dos listas en el mismo orden.
# - Revisar que una lista no esté vacía antes de calcular un promedio.
# - Escribir código legible y mensajes claros para el usuario.

# ======================================================================
# CONSTANTS
# ======================================================================
PASSING_GRADE = 70.0
PUNCTUATION_MARKS = ".,;:!?"
VALID_ACTIONS = ["ADD", "SEARCH", "DELETE"]


# ======================================================================
# PROBLEM 1: Shopping list basics (list operations)
# ======================================================================
# Description: Builds a list of products from a text separated by commas,
#   adds a new product at the end, shows how many items the list has and
#   tells if a product is in the list.
#
# Decisions:
# - The inputs do not ask for quantities, so only product names are used.
# - Names are changed to lowercase.
# - An empty item (like "apple,,orange") is an error.
#
# Inputs:
# - initial_items_text
# - new_item
# - search_item
#
# Outputs:
# - "Items list: <items_list>"
# - "Total items: <number>"
# - "Found item: true|false" (true = search_item is in the list)
#
# Validations:
# - initial_items_text is not empty after strip().
# - Each item is cleaned with strip() and none of them is empty.
# - new_item and search_item are not empty.
#
# Test cases:
# 1) Normal: "apple, banana ,orange", "grape", "banana"
#    -> Items list: ['apple', 'banana', 'orange', 'grape'] / Total items: 4 / Found item: true
# 2) Border: "apple", "pear", "kiwi"
#    -> Items list: ['apple', 'pear'] / Total items: 2 / Found item: false
# 3) Error:  "   ", "grape", "banana" -> Error: invalid input
#    Also: "apple,,orange" -> Error: invalid input

print("--- Problem 1: Shopping list basics ---")
initial_items_text = input("Enter initial items separated by commas: ")
new_item = input("Enter a new item to add: ")
search_item = input("Enter an item to search: ")

new_item = new_item.strip().lower()
search_item = search_item.strip().lower()

if initial_items_text.strip() == "":
    print("Error: invalid input")
elif new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = []
    has_empty_item = False
    for piece in initial_items_text.split(","):
        clean_piece = piece.strip().lower()
        if clean_piece == "":
            has_empty_item = True
        else:
            items_list.append(clean_piece)

    if has_empty_item:
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = search_item in items_list
        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", str(is_in_list).lower())


# ======================================================================
# PROBLEM 2: Points and distances with tuples
# ======================================================================
# Description: Uses tuples to save two points of a plane, calculates the
#   distance between them and creates a new tuple with the midpoint.
#   The distance and the midpoint are rounded to 2 decimals.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A: (x1, y1)"
# - "Point B: (x2, y2)"
# - "Distance: <distance>"
# - "Midpoint: (mx, my)"
#
# Validations:
# - The four values can be converted to float.
#
# Test cases:
# 1) Normal: 0, 0, 3, 4  Distance: 5.0 / Midpoint: (1.5, 2.0)
# 2) Border: 2, 2, 2, 2  Distance: 0.0 / Midpoint: (2.0, 2.0) (same point)
# 3) Error:  abc, 0, 3, 4  Error: invalid input
#    Also: -1, -1, 1, 1  Distance: 2.83 / Midpoint: (0.0, 0.0)

print("--- Problem 2: Points and distances with tuples ---")
x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
    is_input_ok = True
except ValueError:
    is_input_ok = False

if not is_input_ok:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = (round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2))
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)


# ======================================================================
# PROBLEM 3: Product catalog with a list of tuples
# ======================================================================
# Description: Keeps a small catalog as a list of tuples (name, price).
#   It reads a product name and a quantity and calculates the total to
#   pay if the product exists. If it does not exist it shows an error.
#   Names are searched in lowercase.
#
# Inputs:
#  product_name
#  quantity (int)
#
# Outputs:
#  If the product exists: "Unit price: <price>", "Quantity: <quantity>"
#   and "Total: <total>"
# If the product does not exist: "Error: product not found"
#
# Validations:
#  quantity can be converted to int and is greater than 0.
# product_name is not empty after strip().
# product_name is searched in the catalog.
#
# Test cases:
# 1) Normal: "apple", 3       Unit price: 10.0 / Quantity: 3 / Total: 30.0
# 2) Border: "  BANANA ", 1   Unit price: 5.5 / Quantity: 1 / Total: 5.5
# 3) Error:  "grape", 2       Error: product not found
#    Also: "apple", 0 -> Error: invalid input

print("--- Problem 3: Product catalog ---")
catalog = [("apple", 10.0), ("banana", 5.5), ("orange", 8.0)]

product_name = input("Enter product name: ")
quantity_text = input("Enter quantity: ")
product_name = product_name.strip().lower()

try:
    quantity = int(quantity_text)
    is_input_ok = True
except ValueError:
    is_input_ok = False

if product_name == "":
    print("Error: invalid input")
elif not is_input_ok:
    print("Error: invalid input")
elif quantity <= 0:
    print("Error: invalid input")
else:
    found = False
    unit_price = 0.0
    for item_name, item_price in catalog:
        if item_name == product_name:
            found = True
            unit_price = item_price

    if found:
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", round(total_price, 2))
    else:
        print("Error: product not found")


# ======================================================================
# PROBLEM 4: Student grades with two lists
# ======================================================================
# Description: Keeps a list of student names and, in the same order, a
#   list with the grades of each student. It reads a name calculates the
#   average of the grades and tells if the student passed "70.0 or more".
#   Names are searched with the first letter in uppercase.
#
# Inputs:
#  student_name
#
# Outputs:
#  If the student exists: "Grades: <list>", "Average: <average>"
#   and "Passed: true|false" (true = average of 70.0 or more)
#  If the student does not exist: "Error: student not found"
#
# Validations:
#  student_name is not empty after strip().
# student_name is in the list of names.
#  The list of grades is not empty before calculating the average.
#
# Test cases:
# 1) Normal: "Alma" -> Grades: [90.0, 85.0, 100.0] / Average: 91.67 / Passed: true
# 2) Border: "Camila" -> Grades: [70.0, 70.0] / Average: 70.0 / Passed: true (exactly 70)
# 3) Error:  "Zuviri"   -> Error: student not found
#    Also: "Buen rostro" -> Average: 65.0 / Passed: false
#    Also: "Delfina" -> Error: no grades for this student (empty list)

print("--- Problem 4: Student grades ---")
student_names = ["Alma", "Buen rostro", "Camila", "Delfina"]
student_grades = [[90.0, 85.0, 100.0], [60.0, 70.0], [70.0, 70.0], []]

student_name = input("Enter student name: ")
student_name = student_name.strip().title()

if student_name == "":
    print("Error: invalid input")
elif student_name not in student_names:
    print("Error: student not found")
else:
    position = student_names.index(student_name)
    grades_list = student_grades[position]
    if len(grades_list) == 0:
        print("Error: no grades for this student")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= PASSING_GRADE
        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", str(is_passed).lower())


# ======================================================================
# PROBLEM 5: Word frequency counter (two lists)
# ======================================================================
# Description: Counts how many times each word appears in a sentence. The
#   sentence is changed to lowercase and split into a list of words. One
#   list keeps the different words and another keeps how many times each
#   one appears.
#
# Decisions:
# - The simple punctuation marks . , ; : ! ? are replaced by spaces.
# - If two words have the same frequency, the first one found is shown.
#
# Inputs:
# - sentence
#
# Outputs:
# - "Words list: <list>"
# - "Frequencies: <list of (word, count) tuples>"
# - "Most common word: <word>"
#
# Validations:
# - sentence is not empty after strip().
# - The list of words is not empty after removing punctuation.
#
# Test cases:
# 1) Normal: "The cat and the dog and the bird"
#    -> Frequencies: [('the', 3), ('cat', 1), ('and', 2), ('dog', 1), ('bird', 1)] / Most common word: the
# 2) Border: "Hello" -> Words list: ['hello'] / Frequencies: [('hello', 1)] / Most common word: hello
# 3) Error:  "   "   -> Error: invalid input
#    Also: "Hello, hello!" -> Frequencies: [('hello', 2)]; "!!!" -> Error: invalid input

print("--- Problem 5: Word frequency counter ---")
sentence = input("Enter a sentence: ")
clean_sentence = sentence.strip().lower()
for mark in PUNCTUATION_MARKS:
    clean_sentence = clean_sentence.replace(mark, " ")
words_list = clean_sentence.split()

if len(words_list) == 0:
    print("Error: invalid input")
else:
    unique_words = []
    word_counts = []
    for word in words_list:
        if word in unique_words:
            word_position = unique_words.index(word)
            word_counts[word_position] = word_counts[word_position] + 1
        else:
            unique_words.append(word)
            word_counts.append(1)

    frequency_list = []
    most_common_word = unique_words[0]
    highest_count = word_counts[0]
    for word_position in range(len(unique_words)):
        frequency_list.append((unique_words[word_position], word_counts[word_position]))
        if word_counts[word_position] > highest_count:
            highest_count = word_counts[word_position]
            most_common_word = unique_words[word_position]

    print("Words list:", words_list)
    print("Frequencies:", frequency_list)
    print("Most common word:", most_common_word)


# ======================================================================
# PROBLEM 6: Simple contact book (two lists)
# ======================================================================
# Description: A small contact book with a list of names and a list of
#   phone numbers in the same order. The user chooses ADD, SEARCH or
#   DELETE: ADD saves a new contact or updates the phone of an existing
#   one, SEARCH shows the phone and DELETE removes the contact.
#
# Decisions:
# - Names are searched with the first letter in uppercase.
#
# Inputs:
# - action_text (ADD, SEARCH or DELETE)
# - name
# - phone (only for ADD)
#
# Outputs:
# - ADD: "Contact saved: <name> <phone>"
# - SEARCH: "Phone: <phone>" or "Error: contact not found"
# - DELETE: "Contact deleted: <name>" or "Error: contact not found"
#
# Validations:
# - action_text is changed to uppercase and must be one of the three.
# - name is not empty after strip().
# - For ADD, phone is not empty after strip().
#
# Test cases:
# 1) Normal: SEARCH, "Alma"             > Phone: 1234567890
# 2) Border: ADD, "  buen rostro  ", 5550000000  > Contact saved: Bob 5550000000 (updates an existing contact)
# 3) Error:  DELETE, "Zuviri"               > Error: contact not found
#    Also: "jump" > Error: invalid input; DELETE, "Camila" > Contact deleted: Camila

print("--- Problem 6: Simple contact book ---")
contact_names = ["Alma", "Buen rostro", "Camila"]
contact_phones = ["8311105113", "8318983022", "8311180941"]

action_text = input("Enter action (ADD, SEARCH or DELETE): ")
action_text = action_text.strip().upper()

if action_text not in VALID_ACTIONS:
    print("Error: invalid input")
else:
    name = input("Enter contact name: ")
    name = name.strip().title()

    if name == "":
        print("Error: invalid input")
    elif action_text == "ADD":
        phone = input("Enter phone number: ")
        phone = phone.strip()
        if phone == "":
            print("Error: invalid input")
        elif name in contact_names:
            contact_position = contact_names.index(name)
            contact_phones[contact_position] = phone
            print("Contact saved:", name, phone)
        else:
            contact_names.append(name)
            contact_phones.append(phone)
            print("Contact saved:", name, phone)
    elif action_text == "SEARCH":
        if name in contact_names:
            contact_position = contact_names.index(name)
            print("Phone:", contact_phones[contact_position])
        else:
            print("Error: contact not found")
    else:
        if name in contact_names:
            contact_position = contact_names.index(name)
            contact_names.pop(contact_position)
            contact_phones.pop(contact_position)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


# ======================================================================
# CONCLUSIONES
# ======================================================================
# Las listas conviene usarlas cuando los datos cambian porque se puede
# agregar y quitar elementos con append() y pop(). Las tuplas sirven para
# datos que no deben cambiar, como el punto (x, y) del problema 2. Sin
# diccionarios, aprendí a guardar datos que van juntos con una lista de
# tuplas (nombre y precio) o con dos listas en el mismo orden, y a buscar
# con in e index(). Antes de calcular un promedio hay que revisar que la
# lista no esté vacía, para evitar errores.
# 

# ======================================================================
# REFERENCIAS
# ======================================================================
# 1) Platzi. Tuplas en Python: ordenadas e inmutables.
#    https://platzi.com/cursos/fundamentos-python/tuplas-en-python-ordenadas-e-inmutables/
# 2) Avino, D. Python for non-programmers Ep. 4: Lists and tuples in Python.
#    https://davideavino.substack.com/p/python-for-non-programmers-ep-4
# 3) Chaganti, R. Day 6: Data Structures - Lists and Tuples.
#    https://learn.ravichaganti.com/python/day-06
# 4) W3Schools. Python Lists.
#    https://www.w3schools.com/python/python_lists.asp
# 5) W3Schools. Python Tuples.
#    https://www.w3schools.com/python/python_tuples.asp