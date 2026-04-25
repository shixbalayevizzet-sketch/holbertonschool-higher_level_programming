#!/usr/bin/python3
"""
Pascal üçbucağını yaradan modul.
"""


def pascal_triangle(n):
    """
    n dərəcəli Pascal üçbucağını listlər siyahısı kimi qaytarır.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Hər yeni sətir həmişə 1 ilə başlayır
        row = [1]
        prev_row = triangle[i - 1]

        # Sətrin daxili elementlərini hesabla
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Hər sətir 1 ilə bitir (əgər sətir indeksi 0-dan böyükdürsə)
        row.append(1)
        triangle.append(row)

    return triangle
