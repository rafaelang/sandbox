#!/usr/bin/python3.4
print (u'Troco')

#valor = int(input(u'Qual o valor que deseja trocar?'))

valor = 10

print (u'Ok, vamos trocar %.2f para você.' %(valor))

def get_melhor_troco(**kwargs):
	unidades = (.01,.05,.10,.25,.50,1,2,5,10,20,50,100)
	unidades = sorted(unidades, reverse=True)	
	
	limit_unidade = kwargs.get('limit_unidade', {})

	quantidade_por_unidade = dict(zip(unidades, (0,)*unidades.__len__()))

	tentativas = 0

	while quantidade_por_unidade[.01]*.01 != valor:
		resposta = []
		tentativas += 1
		troco = {}
		resto = valor;	
		for unidade_explorada in unidades:
			for unidade in unidades:
				quantidade = resto/unidade
							
				quantidade -= quantidade_por_unidade[unidade_explorada]

				if quantidade == 0:				
					continue				
				
				troco[unidade] = quantidade
				resto = resto - quantidade*unidade	
			
				resposta.append(u'%d %s de %.3f' %( quantidade, (u'moeda' if unidade<=1 else u'nota')+ u's' if quantidade>1 else u'', unidade))
				if resto == 0:
					break
			quantidade_por_unidade[unidade_explorada] += 1

		print (str(tentativas)+u' - '+u', '.join(resposta))

		if tentativas == 5:
			break

def get_troco(**kwargs):
	get_melhor_troco(**kwargs)

get_troco(valor=valor, limit_unidade={100:9})
