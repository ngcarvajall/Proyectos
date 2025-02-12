import random
      

def piedra_papel_tijeras(numero_rondas):
  puntos_user = 0
  puntos_computer = 0
  
  for i in range(numero_rondas):
    options = ['piedra','papel','tijera'] 
    user = input('piedra, papel, tijera').lower()
    user = user.lower()
    computer = random.choice(options)

    if not user in options:
      print('opcion invalida')
      
    print('Has elegido >',user)
    print('He elegido > ',computer)

    if user == computer:
      print('empate !')
    elif user == 'piedra':
      if computer == 'tijera':
        print('piedra gana a tijera')
        print('user win')
        puntos_user += 1
      else:
        print('papel gana a  piedra ')
        print( 'computer win ')
        puntos_computer += 1
    elif user == 'papel':
      if computer == 'piedra':
        print('papel gana a piedra')
        print('user win')
        puntos_user += 1
      else:
        print('tijera gana a  papel ')
        print( 'computer win ')
        puntos_computer += 1
    elif user == 'tijera':
      if computer == 'papel':
        print('tijera gana a papel')
        print('user win')
        puntos_user += 1
      else:
        print('piedra gana a tijera ')
        print( 'computer win ')
        puntos_computer += 1

  print(f'Los puntos que obtuviste fueron {puntos_user}')
  print(f'Los puntos que obtuve fueron {puntos_computer}')

def ppt_sl(num_rondas):
  puntos_user = 0
  puntos_computer = 0
  
  for i in range(num_rondas):
    options = ['piedra','papel','tijera','lagarto','spock'] 
    user = input('piedra, papel, tijera, lagarto, spock').lower()
    computer = random.choice(options)

    if not user in options:
      print('intenta de nuevo')
      
    print('Has elegido >',user)
    print('He elegido >',computer)

    if user == computer:
      print('🤝empate🤝')
    elif user == 'piedra':
      if computer == 'tijera':
        print('piedra gana a tijera')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'lagarto':
        print('piedra aplasta a lagarto')
        print('💁user win💁')
        puntos_user+= 1
      elif computer == 'spock':
        print('spock vaporiza piedra')
        print('💻computer win💻')
        puntos_computer += 1
      else:
        print('papel cubre la piedra')
        print('💻computer win💻')
        puntos_computer += 1
    elif user == 'papel':
      if computer == 'piedra':
        print('papel gana a piedra')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'spock':
        print('papel refuta a Spock')
        print( '💁user win💁')
        puntos_user += 1
      elif computer == 'lagarto':
        print('lagarto aplasta al papel')
        print('💻computer win💻')
        puntos_computer += 1
      else:
        print('la tijera corta al papel')
        print('💻computer win💻')
        puntos_computer += 1
    elif user == 'tijera':
      if computer == 'papel':
        print('tijera gana a papel')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'lagarto':
        print('tijera decapita lagarto')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'spock':
        print('spock rompe tijeras')
        print('💻computer win💻')
        puntos_computer += 1
      else:
        print('piedra aplasta tijera')
        print('💻computer win💻')
        puntos_computer += 1
    elif user == 'spock':
      if computer == 'tijera':
        print('spock aplasta tijeras')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'piedra':
        print('spock vaporiza piedra')
        print('💁user win💁')
        puntos_user += 1
      elif computer == 'papel':
        print('papel refuta spock')
        print('💻computer win💻')
        puntos_computer += 1
      else:
        print('lagarto envenena spock')
        print('💻computer win💻')
        puntos_computer += 1
    else:
      if computer == 'piedra':
        print('te aplasto')
        print('💻computer win💻')
        puntos_user += 1
      elif computer == 'papel':
        print('lagarto pisa papel')
        print('💁user win💁')
        puntos_computer += 1
      elif computer == 'tijeras':
        print('tijeras decapitan a lagarto')
        print('💻computer win💻')
        puntos_user += 1
      elif computer == 'spock':
        print('lagarto envenena a Spock')
        print('💁user win💁')
        puntos_user += 1

  print(f'\nLos puntos que obtuviste fueron {puntos_user}')
  print(f'Los puntos que obtuve fueron {puntos_computer}')

  if puntos_computer > puntos_user:
    print('\nTe he ganado marichocho')
  elif puntos_computer == puntos_user:
    print('🤝🤝🤝🤝🤝')
    print('\nHemos empatado, espabila')
    print('🤝🤝🤝🤝🤝')
  else:
    print('\nMe voy a llorar a la llorería')

def jugar_ppt():
    tipo_juego = input('Elige el tipo de juego: "Clasico o Big Bang Theory').lower()
    condition = True
    while condition:
        if tipo_juego == 'clasico':
            piedra_papel_tijeras(int(input('Elige número de rondas')))
            condition = False
        elif tipo_juego == 'big bang theory':
            ppt_sl(int(input('Elije el número de rondas')))
            condition = False
        else:
            print('Opción inválida')
            continue