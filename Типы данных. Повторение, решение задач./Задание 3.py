usr_in1, usr_in2 = input(), input()
usr_in1, usr_in2 = usr_in1.replace(" ", ""), usr_in2.replace(" ", "")
if len(usr_in1) == len(usr_in2):
    usr_in1, usr_in2 = set(usr_in1), set(usr_in2)
    if usr_in1 - usr_in2 == set():
        print("ЯВЛЯЮТСЯ АНАГРАММАМИ")
    else:
        print("НЕ ЯВЛЯЮТСЯ АНАГРАММАМИ")
else:
    print("НЕ ЯВЛЯЮТСЯ АНАГРАММАМИ")
