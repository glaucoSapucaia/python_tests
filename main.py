from calculator import soma

try:
    print(soma('10', 20))
except AssertionError as e:
    print(f'Valor inválido -> {e}')