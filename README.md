# 🤖 Docyon: ChatGPT no Terminal com API da OpenAI

Este projeto implementa **Docyon**, um chatbot conversacional utilizando o modelo **GPT-3.5-Turbo** da OpenAI no terminal. Ele conta com histórico de mensagens e suporta um modo simulado (mock) para testar sem consumir créditos da API, sendo ideal para testes e experimentações. 🗨️

## Visão Geral  
O sistema simula uma conversa com o **Docyon** diretamente no terminal. Usuários podem enviar mensagens e receber respostas em tempo real do modelo GPT-3.5-Turbo. Um modo simulado também está disponível, permitindo respostas sem conexão com a API real — ótimo para desenvolvimento e testes. 🖥️

Esse projeto pode ser utilizado em diversas aplicações práticas, como suporte ao cliente, automação de tarefas, ou até mesmo como uma ferramenta educacional para interação com alunos. Ele também pode servir para prototipar chatbots customizados para empresas.

Principais funcionalidades deste projeto:
- 🧠 **Interação com o GPT-3.5-Turbo** via API da OpenAI  
- 🧪 **Suporte a respostas simuladas (mock)** para testes locais sem custo  
- 📝 **Manutenção do histórico de mensagens** durante a sessão para respostas contextuais  
- 🖥️ **Interface baseada no terminal**, simples e acessível  

## Como Usar
1. Instale o pacote necessário:
   *pip install openai*
   
2. Instale o pacote necessário:
   Para testar sem consumir a API real, basta manter a variável **<modo_teste>** como **<True>**.
   O mock já está implementado no script e pronto para uso.

## Modo Simulado
Este projeto inclui uma função mock que imita o comportamento da API. Quando **<modo_teste>** está definido como **<True>**, todas as entradas recebem uma resposta simulada baseada na última mensagem do usuário. Isso permite testar a funcionalidade sem internet ou chave da API ativa. 🧪
Ideal para momentos em que o lendário Docyon está só querendo brincar sem gastar tokens.

## Exemplo
*O que está pensando? Qual a capital da França?*  
Docyon: *Você disse: 'Qual a capital da França?'. Isso é muito interessante! =)*

*O que está pensando? sair*
