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
# En este trabajo se practican conceptos básicos de python como los tipos
# numericos int y float asi como valores lógicos bool.También se usan
# operaciones aritméticas, operadores relacionales y operadores lógicos
# como and y or, cada problema incluye validaciones para no tener errores
# comunes, como dividir entre cero o aceptar valores inválidos. Se usaron
# condicionales if, elif y else para tomar decisiones. De los seis problemas
# ayudan a comprender cómo python maneja calculos, comparaciones y
# condiciones en programas simples.

# ======================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ======================================================================
#  Validar siempre los datos antes de hacer cálculos.
#  Usar nombres de variables claros y en inglés.
# Evitar dividir entre cero.
#  Convertir entradas a int o float según corresponda.
#  Usar valores booleanos para representar condiciones.
#  Mostrar mensajes claros al usuario.
#  Mantener el código simple y fácil de explicar.

# ======================================================================
# PROBLEM 1: Temperature Converter
# ======================================================================
# Description: Converts Celsius to Fahrenheit and Kelvin. Checks if the
# temperature is high (>= 30°C).
#
# Inputs:
#  temp_c (float)
#
# Outputs:
#  Fahrenheit
# Kelvin
#  is_high_temperature (bool)
#
# Validations:
#  Input must be a float.
#  Temperature cannot be below -273.15°C.
#
# Test Cases:
# 1) Normal: 25 → F=77.0, K=298.15, High=False
# 2) Border: 30 → F=86.0, K=303.15, High=True
# 3) Error: -300 → Error: invalid temperature

print("--- Problem 1: Temperature Converter ---")
temp_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_text)
    if temp_c < -273.15:
        print("Error: invalid temperature")
    else:
        temp_f = (temp_c * 9 / 5) + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", is_high_temperature)
except ValueError:
    print("Error: invalid input")

# ======================================================================
# PROBLEM 2: Weekly Payment Calculator
# ======================================================================
# Description: Calculates weekly payment including overtime.
#
# Inputs:
# hours_worked (float)
#  hourly_rate (float)
#
# Outputs:
#  normal_hours
# overtime_hours
#  total_payment
#  has_overtime (bool)
#
# Validations:
#  hours_worked >= 0
# hourly_rate > 0
#
# Test Cases:
# 1) Normal: 35h, $100  normal=35, overtime=0, total=3500
# 2) Border: 40h, $80  normal=40, overtime=0, total=3200
# 3) Error: -5h  Error: invalid input

print("--- Problem 2: Weekly Payment Calculator ---")
hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        if hours_worked > 40:
            normal_hours = 40
            overtime_hours = hours_worked - 40
        else:
            normal_hours = hours_worked
            overtime_hours = 0

        has_overtime = overtime_hours > 0
        total_payment = (normal_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5)

        print("Normal hours:", normal_hours)
        print("Overtime hours:", overtime_hours)
        print("Total payment:", round(total_payment, 2))
        print("Has overtime:", has_overtime)
except ValueError:
    print("Error: invalid input")

# ======================================================================
# PROBLEM 3: Discount Eligibility
# ======================================================================
# Description: Determines if a customer receives a 10% discount.
#
# Inputs:
#  purchase_amount (float)
#  is_student (YES/NO)
#  is_senior (YES/NO)
#
# Outputs:
#  discount
#  final_total
#
# Validations:
#  purchase_amount >= 0
#  YES/NO answers only
#
# Test Cases:
# 1) Normal: 1200, YES, NO → discount applied
# 2) Border: 1000, NO, NO → discount applied
# 3) Error: -50 → Error: invalid input

print("--- Problem 3: Discount Eligibility ---")
amount_text = input("Enter purchase amount: ")

try:
    purchase_amount = float(amount_text)
    if purchase_amount < 0:
        print("Error: invalid input")
    else:
        student_text = input("Are you a student? (YES/NO): ").strip().upper()
        senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

        if student_text not in ["YES", "NO"] or senior_text not in ["YES", "NO"]:
            print("Error: invalid input")
        else:
            is_student = student_text == "YES"
            is_senior = senior_text == "YES"

            has_discount = is_student or is_senior or purchase_amount >= 1000.0

            if has_discount:
                discount = purchase_amount * 0.10
                final_total = purchase_amount - discount
                print("Discount:", round(discount, 2))
                print("Final total:", round(final_total, 2))
            else:
                print("Final total:", round(purchase_amount, 2))
except ValueError:
    print("Error: invalid input")

# ======================================================================
# PROBLEM 4: Basic Statistics of Three Integers
# ======================================================================
# Description: Calculates sum, average, max, min, and checks if all are even.
#
# Inputs:
#  n1, n2, n3 (int)
#
# Outputs:
#  sum
#  average
#  max
#  min
#  all_even (bool)
#
# Validations:
#  Inputs must be integers.
#
# Test Cases:
# 1) Normal: 4, 6, 8 → sum=18, avg=6, max=8, min=4, all_even=True
# 2) Border: -2, 0, 2 → works with negatives
# 3) Error: "abc" → Error: invalid input

print("--- Problem 4: Basic Statistics ---")
n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    total_sum = n1 + n2 + n3
    average = total_sum / 3
    maximum = max(n1, n2, n3)
    minimum = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", total_sum)
    print("Average:", round(average, 2))
    print("Max:", maximum)
    print("Min:", minimum)
    print("All even:", all_even)
except ValueError:
    print("Error: invalid input")

# ======================================================================
# PROBLEM 5: Loan Eligibility
# ======================================================================
# Description: Determines if a person is eligible for a loan.
#
# Inputs:
#  monthly_income (float)
#  monthly_debt (float)
#  credit_score (int)
#
# Outputs:
#  debt_ratio
#  is_eligible (bool)
#
# Validations:
#  monthly_income > 0
#  monthly_debt >= 0
#  credit_score >= 0
#
# Test Cases:
# 1) Normal: 9000, 2000, 700 → eligible
# 2) Border: 8000, 3200, 650 → eligible (ratio=0.4)
# 3) Error: income=0 → Error: invalid input
#
# Note: Academic example, not real banking evaluation.

print("--- Problem 5: Loan Eligibility ---")
income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt: ")
score_text = input("Enter credit score: ")

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        is_eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", is_eligible)
except ValueError:
    print("Error: invalid input")

# ======================================================================
# PROBLEM 6: Body Mass Index (BMI)
# ======================================================================
# Description: Calculates BMI and determines category.
#
# Inputs:
#  weight_kg (float)
#  height_m (float)
#
# Outputs:
#  BMI
#  is_underweight
#  is_normal
# is_overweight
#
# Validations:
#  weight_kg > 0
#  height_m > 0
#
# Test Cases:
# 1) Normal: 70kg, 1.75m → BMI=22.86 (normal)
# 2) Border: 50kg, 1.80m → BMI=15.43 (underweight)
# 3) Error: height=0 → Error: invalid input
#
# Note: Academic exercise, not medical diagnosis.

print("--- Problem 6: BMI Calculator ---")
weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except ValueError:
    print("Error: invalid input")

# ======================================================================
# CONCLUSIONES
# ======================================================================
# En estos ejercicios aprendí cómo Python usa números, valores booleanos
# y condiciones para resolver problemas sencillos. Practiqué validar
# entradas para evitar errores y usé operadores lógicos para combinar
# condiciones. También aprendí a calcular promedios, razones y
# conversiones. Estos problemas me ayudaron a entender cómo los programas
# toman decisiones y la importancia de revisar los datos antes de hacer
# cálculos.

# ======================================================================
# REFERENCIAS
# ======================================================================
# 1) Documentación oficial de Python:
#    https://docs.python.org/3/tutorial/
# 2) Programiz - Tutorial de Python:
#    https://www.programiz.com/python-programming
# 3) W3Schools - Python:
#    https://www.w3schools.com/python/
# 4) Aprende Python (en español):
#    https://aprendepython.es/
# 5) El Libro de Python (en español):
#    https://ellibrodepython.com/
