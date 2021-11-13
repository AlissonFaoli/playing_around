dicio_nome = {}
dicio_sobrenome = {}

chaves_nome = ['12', '345', '678', '90']
nomes = ['Desenvolvedor', 'Programador', 'Estagiário', 'Gambiarrista']
sobrenomes = ['Bugado', 'do Ctrl C e Ctrl V', 'das Gambiarras', 'Que Culpa o Cache', 'Que Esquece Como Fez', 'do Git Vazio', 'dos Try/Catch Vazio', 'Famosinho do LinkedIn', 'Caçador de Bugs', 'do Windows Pirata', 'do Update Sem Where', 'do Commit Bugado']

for i in chaves_nome:
	for j in i:
		dicio_nome[j] = nomes[chaves_nome.index(i)]

for i in sobrenomes:
	dicio_sobrenome[sobrenomes.index(i)+1] = i

nome = input('Insira sua data de aniversário no formato DD/MM: ').strip().split('/')
try:
	print(f'Seu nome de programador é {dicio_nome[nome[0][-1]]} {dicio_sobrenome[int(nome[1])]}')
except Exception as erro:
	print(erro)
