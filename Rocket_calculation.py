m_0 = 2950000
m_e = 1000000
t_e = 130
Relativgeschwindigkeit = 2220
delta_t = 5
F_schub = 33 * 10 ** 6

Zeit = []
Masse = [m_0]
Beschleunigung = []
Geschwindigkeit = [0]
Schwerkraft = [Masse[0] * 9.81]
Endkraft = []
Höhe = [0, 0]

for i in range(0, 13):
    Zeit.append(delta_t * i)
    Masse.append(Masse[i] - 75000)
    Schwerkraft.append(Masse[i + 1] * 9.81)
    Endkraft.append(F_schub - Schwerkraft[i])
    Beschleunigung.append(Endkraft[i] / Masse[i])
    Geschwindigkeit.append(Geschwindigkeit[i] + Beschleunigung[i] * delta_t)
    if i >= 2:
        Höhe.append(5 * Geschwindigkeit[i - 1] + Höhe[i - 1])

print("{:<10} {:<15} {:<15} {:<20} {:<25} {:<30} {:<35}".format('Zeit(s)', 'Masse(kg)', 'Beschleunigung', 'Höhe',
                                                                'Geschwindigkeit', 'Endkraft', 'Schwerkraft'))
print()
for i in range(0, len(Zeit)):
    print("{:<10.2f} {:<15.2f} {:<15.2f} {:<20.2f} {:<25.2f} {:<30.2f} {:<35.2f}".format(Zeit[i], Masse[i],
                                                                                         Beschleunigung[i], Höhe[i],
                                                                                         Geschwindigkeit[i],
                                                                                         Endkraft[i], Schwerkraft[i]))
