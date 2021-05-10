# -*- coding: UTF-8 -*-
import datetime

print("Cadastre seu anúncio")
nome=input("Informe o nome do anúncio: ")
cliente=input("Informe o nome do cliente:")
valordia=float(input("Informe o valor investido por dia:" ))
print("Informe as datas de inicio e fim de campanha: ")
anoi = eval (input ("Ano de inicio do anúncio?: "))
mesi = eval (input ("Mês de inicio do anúncio?: "))
diai = eval (input ("Dia de inicio do anúncio?: "))
anof = eval (input ("Ano de fim do anúncio?:  "))
mesf = eval (input ("Mês de fim do anúncio?: "))
diaf = eval (input ("Dia de fim do anúncio?: "))
datai = datetime.date(anoi, mesi, diai)
dataf = datetime.date(anof, mesf, diaf)


diferenca = abs((dataf - datai).days)


valortotal=valordia*diferenca
visualizacao_original=valortotal*30
clicam=(visualizacao_original*12)/100
compartilhamento=(clicam*3)/20
visualizacao_new=compartilhamento*40
visu_total=visualizacao_new+visualizacao_original

    
print("Relatório de Anúncios:")
print("Situação                                Cliente    Valor investido   Total de Visualização       Compartilhamentos       Visualização original")
print("Anúncio: {0}                               {1}             R${2}                     {3:.0f}                        {4:.0f}                     {5:.0f}".format(nome, cliente,valordia, visu_total,compartilhamento,visualizacao_original))


        
     
