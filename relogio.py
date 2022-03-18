from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') #Localização BR.
hoje = datetime.now() #variável com data deste momento

horario_final = hoje.strftime("%d/%B/%Y - %H:%M") #Formatação para data, hora e minuto. %B em maiusculo para exibir nome do mês inteiro.

print(horario_final)

