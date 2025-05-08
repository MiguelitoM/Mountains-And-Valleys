abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def eh_territorio(territorio):
    if not isinstance(territorio, tuple) or not 0 < len(territorio) < 27:       # Confirma se o território é um tuplo, com comprimento entre 1 e 99
        return False
    for coluna in territorio:
        if not isinstance(coluna, tuple) or len(coluna) != len(territorio[0]) or not 0 < len(coluna) < 100:         # Confirma se os elementos do território são tuplos e confirma se todos os tuplos dentro do território têm o mesmo comprimento, que tem de estar entre 1 e 26.
            return False
        for intersecao in coluna:
            if not isinstance(intersecao, int) or not (intersecao == 0 or intersecao == 1):        # Confirma se os elementos dentro dos tuplos são apenas 1 ou 0 e se são inteiros.
                return False
    return True


def num_to_abc(num):        # Esta função irá ajudar a converter números para as respetivas colunas. (Por exemplo, a coluna nº5 é a coluna "E")
    if 0 < num < 27:
        return abc[num-1]
    return ('inválido')


def abc_to_num(caracter):
    return abc.index(caracter)+1        # Esta função faz o contrário da anterior: Converte uma letra para a posição dessa letra no alfabeto


def obtem_ultima_intersecao(territorio):
    ultima_intersecao = num_to_abc(len(territorio)), len(territorio[0])          # A última interseção é a letra correspondente ao número de colunas(Nv) e o número de linhas (Nh)
    return ultima_intersecao


def eh_intersecao(intersecao):
    if not (isinstance(intersecao, tuple) and len(intersecao) == 2 and isinstance(intersecao[0], str) and isinstance(intersecao[1], int) and intersecao[0] in abc and 0 < intersecao[1] < 100):      # Confirma se a interseção é um tuplo com 2 elementos, onde o primeiro elemento é uma letra do alfabeto e o segundo é um número entre 0 e 100.
        return False
    return True


def eh_intersecao_valida(territorio, intersecao):
    Nv = len(territorio)
    Nh = len(territorio[0])
    if not eh_intersecao(intersecao) or abc_to_num(intersecao[0]) > (Nv) or intersecao[1] > Nh:        # Confirma se a interseção não ultrapassa o número limite de colunas e linhas, para um dado território
        return False
    return True


def eh_intersecao_livre(territorio, intersecao):
    if territorio[abc_to_num(intersecao[0]) - 1][intersecao[1] - 1] == 0:      # Procura, no território, a entrada correspondente à interseção dada. Caso seja igual a 0 então o território está livre
       return True   
    return False


def obtem_intersecoes_adjacentes(territorio, intersecao):
    intersecao_adjacente= ()
    intersecao_cima = (intersecao[0], intersecao[1] + 1)        # Encontramos as 4 interseções ao somar/subtrair 1 valor à linha ou somar/subtrair 1 "passo" no alfabeto das colunas
    intersecao_direita = (num_to_abc(abc_to_num(intersecao[0]) + 1), intersecao[1])
    intersecao_baixo = (intersecao[0], intersecao[1] - 1)
    intersecao_esquerda = (num_to_abc(abc_to_num(intersecao[0]) - 1), intersecao[1])
    intersecao_adjacente= ()
    for candidato in [intersecao_baixo, intersecao_esquerda, intersecao_direita, intersecao_cima]:      # Confirma se a interseção adjacente é válida.
        if eh_intersecao_valida(territorio, candidato):
            intersecao_adjacente+= (candidato,)
    return intersecao_adjacente


def ordena_intersecoes(tuplo):
    def ordenador(tuplo):        # Devolve o 2o elemento e depois o 1o para a ordenação
        return tuplo[1], tuplo[0]
    tuplo_ordenado = tuple(sorted(tuplo, key=ordenador))     # Ordena o tuplo primeiro pelo segundo elemento e depois pelo primeiro. Transforma a lista resultante em tuplo.
    return tuplo_ordenado


def territorio_para_str(territorio):
    if not eh_territorio(territorio):       # Confirma a validade do argumento
        raise ValueError("territorio_para_str: argumento invalido")
    tamanho = abc_to_num(obtem_ultima_intersecao(territorio)[0]),obtem_ultima_intersecao(territorio)[1]
    linha_letras = "   " # 3 espaços
    linha_meio = ""

    letras = [letra for letra in abc[:tamanho[0]]]      # Adiciona as letras que aparecem na primeira e última linhas
    for letra in letras:
        linha_letras += f'{letra} '
    linha_letras = linha_letras[:-1]       # Retira o último espaço que estava a mais

    for i in range (tamanho[1], 0, -1): 
        if len(str(i)) == 2:      # Adiciona o número da linha
            linha = f'{i} '
        else:
            linha = f' {i} '
        for j in range(tamanho[0]):     # Adiciona o conteúdo de cada linha (. ou X)
            if territorio[j][i - 1] == 0:
                linha += ". "
            else:
                linha += "X "
        if len(str(i)) == 2:      # Adiciona o número da linha
            linha += f'{i}'
        else:
            linha += f' {i}'
        linha_meio += f'{linha}\n'

    string_territorio = f'{linha_letras}\n{linha_meio}{linha_letras}'       # Junta tudo numa só variável
    return string_territorio


def obtem_cadeia(territorio, intersecao):
    if not eh_territorio(territorio) or not eh_intersecao_valida(territorio, intersecao):       # Confirma a validade do argumento
        raise ValueError("obtem_cadeia: argumentos invalidos")
    tipo_de_cadeia = eh_intersecao_livre(territorio, intersecao)
    def espalha_cadeia(territorio, cadeia = [intersecao]):
        for intersecao_cadeia in cadeia:        # A função passa por todos os elementos que vão sendo adicionados à cadeia. Desta forma, o processo repete-se até pararem de ser adicionados elementos à cadeia
            for intersecao_adjacente in obtem_intersecoes_adjacentes(territorio, intersecao_cadeia):           # Passa por todas as interseções adjacentes
                if intersecao_adjacente not in cadeia and eh_intersecao_livre(territorio, intersecao_adjacente) == tipo_de_cadeia:     # Confirma se as interseções fazem parte da cadeia e se ainda não estão na cadeia
                    cadeia.append(intersecao_adjacente)
        return cadeia
    cadeia_ordenada = ordena_intersecoes(espalha_cadeia(territorio))    # Ordena a cadeia e transforma em tuplo
    return cadeia_ordenada


def obtem_vale(territorio, intersecao):
    if not eh_territorio(territorio) or not eh_intersecao_valida(territorio, intersecao) or eh_intersecao_livre(territorio, intersecao):    # Confirma se o território e interseção são válidos e se a interseção corresponde a uma montanha
        raise ValueError("obtem_vale: argumentos invalidos")
    vales = ()
    for montanha in obtem_cadeia(territorio, intersecao):           # Obtem a cadeia de montanhas
        for intersecao_adjacente in obtem_intersecoes_adjacentes(territorio, montanha):         # Procura todas as interseções adjacentes à cadeia de montanhas
            if eh_intersecao_livre(territorio, intersecao_adjacente) and intersecao_adjacente not in vales:
                vales += (intersecao_adjacente,)
    return ordena_intersecoes(vales)        # Retorna os vales ordenados pela ordem de leitura


def verifica_conexao(territorio, intersecao1, intersecao2):
    if not(eh_territorio(territorio) and eh_intersecao_valida(territorio, intersecao1) and eh_intersecao_valida(territorio, intersecao2)):  # Confirma se o território e as interseções são válidas.
        raise ValueError("verifica_conexao: argumentos invalidos")
    if intersecao2 in obtem_cadeia(territorio, intersecao1):    # Confirma se a intersecao2 está conectada à intersecao1
        return True
    return False


def calcula_numero_montanhas(territorio):
    if not eh_territorio(territorio):       # Confirma se o território é válido
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    numero = 0
    for coluna in territorio:
        numero += coluna.count(1)       # Conta o número de elementos 1 dentro de cada tuplo.
    return numero


def calcula_numero_cadeias_montanhas(territorio):
    if not eh_territorio(territorio):       # Confirma se o território é válido
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    visto = ()
    cadeia_counter = 0
    for i in range(abc_to_num(obtem_ultima_intersecao(territorio)[0])):
        for j in range(obtem_ultima_intersecao(territorio)[1]):     # Passa por todo o território
            intersecao = num_to_abc(i + 1), (j + 1)     # Define todas as interseções
            if not eh_intersecao_livre(territorio, intersecao):   # Confirma se a interseção é uma montanha
                if intersecao not in visto:     # Confirma se a interseção não está repetida
                    visto += obtem_cadeia(territorio, intersecao)
                    cadeia_counter += 1
    return cadeia_counter


def calcula_tamanho_vales(territorio):
    if not eh_territorio(territorio):       # Confirma se o território é válido
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    vales_counter = 0
    for i in range(abc_to_num(obtem_ultima_intersecao(territorio)[0])):
        for j in range(obtem_ultima_intersecao(territorio)[1]):
            intersecao = num_to_abc(i + 1), (j + 1)     # Define todas as interseções
            if eh_intersecao_livre(territorio, intersecao):     # Confirma se a interseção está livre
                for talvez_montanha in obtem_intersecoes_adjacentes(territorio, intersecao):
                    if not eh_intersecao_livre(territorio, talvez_montanha):   # Confirma se pelo menos um das interseções adjacentes é montanha
                        vales_counter += 1
                        break
    return vales_counter