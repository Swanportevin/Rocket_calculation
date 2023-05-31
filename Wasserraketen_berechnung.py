import math


def calculate_c(pressure_Pa):
    # Berechnung die Konstante (c)
    c = math.sqrt((2 * pressure_Pa) / 1000)

    return c


def calculate_ve(c, m0, mf, tb):
    # Berechnung ve
    ve = c * math.log((m0 / mf) - (9.81 * tb))

    return ve


def calculate_tb(c, Vw, A):
    # Berechnung tb
    tb = Vw / (c * A)

    return tb


def calculate_h(ve, tb):
    s = 0.5 * ve * tb
    h = ve ** 2 / (2 * 9.81) + s
    return h


while True:
    # Daten werden gesammelt
    mass_rocket = float(input("Geben Sie die Masse der Rakete(kg): "))
    mass_water = float(input("Geben Sie der Volum Wasser(l): "))
    pressure = float(input("Enter the pressure in the bottle (bar): "))
    if mass_rocket < 0 or mass_water < 0 or pressure < 0 or math.isnan(mass_rocket) or math.isnan(
            mass_water) or math.isnan(pressure):
        print('Alle Werten müssen positiv und ein Nummer sein. Probieren Sie Nochmal.')
    else:
        break

# Wir nehmen an die Öffnung der Flasche(Gummiband) ist 4mm
A = 0.004 ** 2 * math.pi

pressure_Pa = pressure * 10 ** 5

m0 = mass_water + mass_rocket
print(m0)
mf = mass_rocket
print(mf)
Vw = mass_water / 10 ** 3
# Calculate tb, c, ve
c = calculate_c(pressure_Pa)
print(c)
tb = calculate_tb(c, Vw, A)
print(tb)
ve = calculate_ve(c, m0, mf, tb)
h = calculate_h(ve, tb)

# Resultaten werden gedrückt
print()
print()
print("{:<10} {:<15} {:<15} {:<20} {:<25} {:<30} {:<35} {:<40}".format('m0(kg)', 'mf(kg)', 'Δ_p(Pascal)', 'tb(s)','Vw(m^3)', 'c(m/s)', 've(m/s)', 'h(m)'))
print()
print("{:<10} {:<15} {:<15} {:<20} {:<25} {:<30} {:<35} {:<40}".format(m0, mf, pressure_Pa, tb,Vw, c, ve, h))
