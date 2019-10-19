filmes = {}

while True:
  print('''
  1 - cadastrar filmes
  2 - listar filmes disponíveis
  3 - atualizar filme
  4 - remover filme
  5 - emprestar filme
  6 - devolver filme
  7 - sair
  ''')
  op = input('escolha sua opção \n')
  if op == '7':
    break
  elif op == '1':
    titulo = input('qual o titulo do filme: ')
    ano = int(input('qual o ano do filme: '))
    quantidade = int(input('quantidade: '))
    filmes[titulo] = {"titulo": titulo, "ano": ano, 'quantidade': quantidade}
  elif op == '2':
    try:
      titulo = input('digite o titulo ')
      if not titulo in filmes:
        raise Exception('o filme não existe')
    except Exception:
        continue
  elif op == '3':
    filme = input('qual o nome do filme que desejas atualizar: ')
    for item in filmes:
     if item == filme:
       quantidade = int(input('quantidade: '))
       filmes[item].update({'quantidade':quantidade})
    else:
      print('Filme atualizado com sucesso')
  elif op == '4':
    filme = input('qual filme deverá ser removido: ')
    del filmes[filme]
    print('filme excluido')
  elif op == '5':
    titulo = input('qual o titulo do filme: ')
    data = int(input('quantos: '))
    if filmes[titulo]['quantidade'] > 0:
      maior = 0
      print('disponivel')
    else:
      print('não disponivel')
  elif op == '6':
    titulo = input('qual o titulo do filme: ')
    data = int(input('devolução de: '))
    if filmes[titulo]['quantidade'] > 0:
      maior = 0
      print('obrigado')
  elif op == '7':
    print('volte sempre')
    break
    
Exemplo abaixo da parte do codigo aonde voce usara o  exception 
try:
      titulo = input('digite o titulo ')
      if not titulo in filmes:
        raise Exception('o filme não existe')
    except Exception:
        continue

