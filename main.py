def nuqtalar_orasidagi_masofa(nuqtalar):
    masofalar = []
    for i in range(len(nuqtalar) - 1):
        x1, y1 = nuqtalar[i]
        x2, y2 = nuqtalar[i + 1]
        masofa = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        masofalar.append(masofa)
    return masofalar

nuqtalar = [(1, 2), (3, 4), (5, 6)]
print(nuqtalar_orasidagi_masofa(nuqtalar))
