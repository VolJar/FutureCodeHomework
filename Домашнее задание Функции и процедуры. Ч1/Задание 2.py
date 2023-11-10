def register_user(fn, ln, mn, yr):
    return f"{ln} {fn} {mn} {yr} г.р. зарегистрирован"

ufn = input()
uln = input()
umn = input()
uyr = input()
print(register_user(ufn, uln, umn, uyr))
