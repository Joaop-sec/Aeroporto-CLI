#pu caba ve os Cepefi o caba ve aonde?

import re

def valida_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto
    
    return cpf[9] == str(dv1) and cpf[10] == str(dv2)

# Dps deleta essa bomba (Daqui pra baixo)
# ------------------- TESTES -------------------
if __name__ == "__main__":
    testes = [
        # (CPF, resultado esperado)
        ("111.444.777-35", True),
        ("123.456.789-09", True),
        ("529.982.247-25", True),
        ("11144477735", True),
        ("111 444 777 35", True),

        ("111.444.777-34", False),
        ("123.456.789-00", False),
        ("111.111.111-11", False),
        ("123.456.789-0", False),
        ("123.456.789-090", False),
        ("000.000.000-00", False),
    ]

    print("Iniciando testes...\n")
    acertos = 0
    for cpf, esperado in testes:
        resultado = valida_cpf(cpf)
        ok = resultado == esperado
        if ok:
            acertos += 1
        status = "OK" if ok else "FALHOU"
        print(f"{status:>6} | CPF: {cpf:<20} | Obtido: {resultado:<5} | Esperado: {esperado}")

    print(f"\n{acertos}/{len(testes)} testes passaram.")