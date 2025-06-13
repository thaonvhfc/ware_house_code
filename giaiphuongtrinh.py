import math

def solve_quadratic(a, b, c):
    # Tính toán discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Hai nghiệm thực khác nhau
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Hai nghiệm thực: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        # Một nghiệm kép
        root = -b / (2 * a)
        return f"Một nghiệm kép: x = {root}"
    else:
        # Hai nghiệm phức
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Hai nghiệm phức: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"

# Ví dụ sử dụng
a = 1
b = -3
c = 2

result = solve_quadratic(a, b, c)
print(result)