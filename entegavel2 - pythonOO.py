class AUVs_naut:

    def __init__(self, n_thursters: int, temposimulacao: int, sensores: list, anocostrucao: int, nome: str):
        self.numero_thursters = n_thursters
        self.tempo_de_simulacao = temposimulacao
        self.sensores = sensores
        self.ano_de_construcao = anocostrucao
        self.nome = nome
    

    '''exibe uma tabela com as informações do robo'''
    def __repr__(self):
        r = (f'nome                       | {self.nome}\n'
        '-------------------------------------------------------------------\n'
        f'numero de thursters:       | {self.numero_thursters}\n'
        '-------------------------------------------------------------------\n'
        f'tempo de teste: simulacao  | {self.tempo_de_simulacao}h\n'
        '-------------------------------------------------------------------\n'
        f'lsta de sensores           | {self.sensores}\n'
        '-------------------------------------------------------------------\n'
        f'ano de construcao          | {self.ano_de_construcao}\n')
        
        return r



    '''exibi as informações dos dois robos em uma tabela'''
    #não sabia se podia usar as biblotecas pra fazer um tabela
    def exibir_all(self,AUV2):
        print('--------------------------------------------------------------------------------------------------------|\n'
              f'nome                     | {self.nome}                           |   {AUV2.nome}                                 |\n'
               '--------------------------------------------------------------------------------------------------------|\n'
              f'numero de thursters      | {self.numero_thursters}                             |   {AUV2.numero_thursters}                                          |\n'
               '--------------------------------------------------------------------------------------------------------|\n'
              f'tempo de teste: simulacao| {self.tempo_de_simulacao}h                          |   {AUV2.tempo_de_simulacao}h                                       |\n'
               '--------------------------------------------------------------------------------------------------------|\n'
              f'lsta de sensores         | {self.sensores}  |   {AUV2.sensores}|\n'
               '--------------------------------------------------------------------------------------------------------|\n'
              f'ano de construcao        | {self.ano_de_construcao}                          |   {AUV2.ano_de_construcao}                                       |\n'
               '--------------------------------------------------------------------------------------------------------|')


    '''faz um rank pra ver qual dos dois robos é o mais novo'''
    def caçula(self,AUV2):


        modelo1 = self.ano_de_construcao
        modelo2 = AUV2.ano_de_construcao

        if modelo1 > modelo2:
            print(f' modelo do mais novo para o mas velho\n'
                   ' -----------------------------------\n'
                  f'        {self.ano_de_construcao} -- {self.nome}\n'
                  f'        {AUV2.ano_de_construcao} -- {AUV2.nome}\n'
                   '-----------------------------------')
        
        elif modelo1 < modelo2:
            print(f' modelo do mais novo para o mas velho\n'
                   ' -----------------------------------\n'
                  f'        {AUV2.ano_de_construcao} -- {AUV2.nome}\n'
                  f'        {self.ano_de_construcao} -- {self.nome}\n'
                   '-----------------------------------')
        
        else:
            print('--------------------------------------\n'
                f'ambos modelos foram constridos em {self.ano_de_construcao}\n'
                '--------------------------------------')



    '''faz um rank pra ver qual dos robos tiveram um maior tempo de teste em simulação'''
    def comparar_temp(self,AUV2):
        
        t1 = self.tempo_de_simulacao
        t2 = AUV2.tempo_de_simulacao

        if t1 > t2:

             print(f' modelo que teve maior tempo de teste em simulação para o menor\n'
                  ' --------------------------------------------------------------\n'
                  f'        {self.tempo_de_simulacao}h -- {self.nome}\n'
                  f'        {AUV2.tempo_de_simulacao}h -- {AUV2.nome}\n'
                   '---------------------------------------------------------------')
            
        if t1 < t2:

             print(f' modelo que teve maior tempo de teste em simulação para o menor\n'
                    ' --------------------------------------------------------------\n'
                   f'        {AUV2.tempo_de_simulacao}h -- {AUV2.nome}\n'
                   f'        {self.tempo_de_simulacao}h -- {self.nome}\n'
                    '---------------------------------------------------------------')

        else:
            print('---------------------------------------------------------\n'
                  'ambos modelos tiveram o mesmo tempo de teste em simulação\n'
                  f'         tempo de teste em simulação = {self.tempo_de_simulacao}h\n'
                  '---------------------------------------------------------')
                  


#testes realizados
veiculo1 = AUVs_naut(8,200,['BAR30','BMP180','L298N'],2022,'Lua')
veiculo2 = AUVs_naut(6,250,['presure sensor','external depth sensor'],2020,'BrHUE 2020')
print(veiculo1)
print(veiculo2)
veiculo1.exibir_all(veiculo2)
veiculo1.caçula(veiculo2)
veiculo1.comparar_temp(veiculo2)