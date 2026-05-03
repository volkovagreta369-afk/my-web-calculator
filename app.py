import streamlit as st
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Налаштування сторінки
st.set_page_config(page_title="Інженерний калькулятор", layout="centered")
st.title("📟 Інженерний калькулятор")

# Список операцій точно як у твоєму коді
options = [
    "1. Додавання (+)", "2. Віднімання (-)", "3. Множення (*)", "4. Ділення (/)",
    "5. Степінь (^)", "6. Квадратний корінь (√)", "7. Косинус (cos)", "8. Синус (sin)",
    "9. Тангенс (tan)", "10. Факторіал (x!)", "11. Логарифм (log)", "12. Натуральний логарифм (ln)",
    "13. Ліміт (Limit)", "14. Інтеграл (Integral)", "15. Розв’язання рівняння",
    "17. Число π (pi)", "18. Число Єйлера (e)", "19. Графіки (x; y)", 
    "20. Квадратне рівняння (ax^2 + bx + c = 0)"
]

operation = st.selectbox("Оберіть операцію:", options)

# Логіка для кожної операції
if operation in options[0:5]:  # 1-5
    col1, col2 = st.columns(2)
    a = col1.number_input("Введіть число a", value=0.0)
    b = col2.number_input("Введіть число b", value=0.0)
    
    if st.button("Обчислити"):
        if "1." in operation: st.success(f"Результат: {a + b}")
        elif "2." in operation: st.success(f"Результат: {a - b}")
        elif "3." in operation: st.success(f"Результат: {a * b}")
        elif "4." in operation: 
            st.success(f"Результат: {a / b if b != 0 else 'Помилка: ділення на нуль!'}")
        elif "5." in operation: st.success(f"Результат: {a ** b}")

elif "6." in operation:
    a = st.number_input("Введіть число")
    if st.button("Обчислити"):
        if a >= 0: st.success(f"Результат: {math.sqrt(a)}")
        else: st.warning(f"Результат: {math.sqrt(-a)}i")

elif operation in options[6:9]: # 7-9 (Виправлено точність)
    a = st.number_input("Введіть кут (градуси)")
    if st.button("Обчислити"):
        rad = math.radians(a)
        if "7." in operation: st.success(f"Результат: {round(math.cos(rad), 10)}")
        elif "8." in operation: st.success(f"Результат: {round(math.sin(rad), 10)}")
        elif "9." in operation: 
            if a % 180 == 90: st.error("Результат: Не існує")
            else: st.success(f"Результат: {round(math.tan(rad), 10)}")

elif "10." in operation:
    a = st.number_input("Введіть ціле число", step=1)
    if st.button("Обчислити"):
        if a >= 0: st.success(f"Результат: {math.factorial(int(a))}")
        else: st.error("Помилка: факторіал тільки для невід’ємних чисел!")

elif "11." in operation:
    a = st.number_input("Число")
    b = st.number_input("Основа логарифму", value=10.0)
    if st.button("Обчислити"):
        if a > 0 and b > 0 and b != 1: st.success(f"Результат: {math.log(a, b)}")
        else: st.error("Помилка: некоректний логарифм!")

elif "12." in operation:
    a = st.number_input("Введіть число")
    if st.button("Обчислити"):
        if a > 0: st.success(f"Результат: {math.log(a)}")
        else: st.error("Помилка: натуральний логарифм тільки для позитивних чисел!")

elif "13." in operation:
    expr_str = st.text_input("Вираз (наприклад, sin(x)/x)")
    point = st.number_input("Точка, до якої прямує x", value=0.0)
    if st.button("Знайти ліміт"):
        x = sp.symbols('x')
        res = sp.limit(sp.sympify(expr_str), x, point)
        st.write(f"Ліміт: {res}")

elif "14." in operation:
    expr_str = st.text_input("Вираз для інтегралу (наприклад, x**2)")
    if st.button("Інтегрувати"):
        x = sp.symbols('x')
        res = sp.integrate(sp.sympify(expr_str), x)
        st.latex(f"\\int {sp.latex(sp.sympify(expr_str))} dx = {sp.latex(res)} + C")

elif "15." in operation:
    eq_str = st.text_input("Рівняння (наприклад, x**2 - 4 = 0)")
    if st.button("Розв'язати"):
        x = sp.symbols('x')
        if "=" in eq_str:
            left, right = eq_str.split("=")
            sol = sp.solve(sp.sympify(left) - sp.sympify(right), x)
            st.success(f"Розв’язок: {sol}")
        else:
            st.error("Помилка: використовуйте '='")

elif "16." in operation:
    st.info(f"Число π: {math.pi}")

elif "17." in operation:
    st.info(f"Число Єйлера e: {math.e}")

elif "18." in operation:
    func_str = st.text_input("Функція y(x):", value="x**2")
    if st.button("Побудувати"):
        x_vals = np.linspace(-10, 10, 400)
        x_sym = sp.symbols('x')
        f_sym = sp.sympify(func_str)
        f_num = sp.lambdify(x_sym, f_sym, "numpy")
        y_vals = f_num(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"y = {func_str}")
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

elif "19." in operation:
    a = st.number_input("a", value=1.0)
    b = st.number_input("b", value=0.0)
    c = st.number_input("c", value=0.0)
    if st.button("Розв'язати"):
        D = b**2 - 4*a*c
        if D > 0:
            st.success(f"x1 = {(-b + math.sqrt(D))/(2*a)}, x2 = {(-b - math.sqrt(D))/(2*a)}")
        elif D == 0:
            st.success(f"x = {-b/(2*a)}")
        else:
            real = -b/(2*a)
            imag = math.sqrt(-D)/(2*a)
            st.success(f"Комплексні корені: {real} ± {imag}i")
