from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
hoje = datetime.now()

horario_final = hoje.strftime("%d/%B/%Y - %H:%M")

print(horario_final)

