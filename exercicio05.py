def f(a):
    if a:
        return "V"
    else:
        return "F"

print("┌─────────────┬──────────────┐")
print("│ Tabela de A │ Tabela de ~A │")
print("├─────────────┼──────────────┤")
A = True
print(f"│      {f(A)}      │      {f(not A)}       │")
print("├─────────────┼──────────────┤")
print(f"│      {f(A)}      │      {f(not A)}       │")
print("├─────────────┼──────────────┤")
A = False
print(f"│      {f(A)}      │      {f(not A)}       │")
print("├─────────────┼──────────────┤")
print(f"│      {f(A)}      │      {f(not A)}       │")
print("└─────────────┴──────────────┘")


print()


print("┌─────────────┬──────────────┐")
print("│ Tabela de B │ Tabela de ~B │")
print("├─────────────┼──────────────┤")
B = True
print(f"│      {f(B)}      │       {f(not B)}      │")
print("├─────────────┼──────────────┤")
B = False
print(f"│      {f(B)}      │       {f(not B)}      │")
print("├─────────────┼──────────────┤")
B = True
print(f"│      {f(B)}      │       {f(not B)}      │")
print("├─────────────┼──────────────┤")
B = False
print(f"│      {f(B)}      │       {f(not B)}      │")
print("└─────────────┴──────────────┘")


print()


print("┌─────────────┬─────────────┬───────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de A^B │")
print("├─────────────┼─────────────┼───────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │       {f(A and B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │       {f(A and B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │       {f(A and B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │       {f(A and B)}       │")
print("└─────────────┴─────────────┴───────────────┘")


print()


print("┌─────────────┬─────────────┬───────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de AvB │")
print("├─────────────┼─────────────┼───────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │       {f(A or B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │       {f(A or B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │       {f(A or B)}       │")
print("├─────────────┼─────────────┼───────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │       {f(A or B)}       │")
print("└─────────────┴─────────────┴───────────────┘")


print()


print("┌─────────────┬─────────────┬────────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de ~A^B │")
print("├─────────────┼─────────────┼────────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A and B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A and B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A and B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A and B)}       │")
print("└─────────────┴─────────────┴────────────────┘")


print()


print("┌─────────────┬─────────────┬────────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de A^~B │")
print("├─────────────┼─────────────┼────────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(A and not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(A and not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(A and not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(A and not B)}       │")
print("└─────────────┴─────────────┴────────────────┘")


print()


print("┌─────────────┬─────────────┬────────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de ~AvB │")
print("├─────────────┼─────────────┼────────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A or B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A or B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A or B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(not A or B)}       │")
print("└─────────────┴─────────────┴────────────────┘")


print()


print("┌─────────────┬─────────────┬────────────────┐")
print("│ Tabela de A │ Tabela de B │ Tabela de Av~B │")
print("├─────────────┼─────────────┼────────────────┤")
A = True
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(A or not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(A or not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
A = False
B = True
print(f"│      {f(A)}      │      {f(B)}      │        {f(A or not B)}       │")
print("├─────────────┼─────────────┼────────────────┤")
B = False
print(f"│      {f(A)}      │      {f(B)}      │        {f(A or not B)}       │")
print("└─────────────┴─────────────┴────────────────┘")
