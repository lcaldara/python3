alt = float(input('Digite a altura da parede a ser pintada: '))
compr = float(input('Digite o comprimento da parede a ser pintada: '))
area = alt*compr
litros = area/2
print(' ')
print('Será(ão) necessário(s) {:.2f} litro(s) de tinta.'.format(litros))
print('Será(ão) necessário(s) {:.2f} litro(s) de tinta.'.format((alt*compr)/2))
