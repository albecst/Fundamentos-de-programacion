# 1 Barn = 10^-28 m^2
# x Barn = y m^2

def conversor_Barns_a_m2(m2): 
    '''
    float, float --> float
    OBJ: programar un conversor de m2 a Barns
    PRE: m2 >= 0
    '''
    return (m2/10**-28)


def conversor_m2_a_Barns(Barns): 
    '''
    float, float --> float
    OBJ: programar un conversor de Barns a m2
    PRE: Barns >= 0
    '''
    return (Barns*10**-28)

m2 = float(input("Si quieres convertir x m2 a Barns, pon un valor > a 0\n"))
Barns = float(input("Si quieres convertir x Barns a m2, pon un valor > a 0\n"))

print(f"{m2} m2 son {conversor_Barns_a_m2(m2)} Barns")
print(f"{Barns} Barns son {conversor_m2_a_Barns(Barns)}, m2")