Este prompt herda todas as diretrizes e restrições do template principal: `@/docs/ai_agent/GEMINI.md`.

# 🚀 Proposta de Organização de Arquivos de Animação

## 🌍 Contexto

Atualmente, todos os vídeos e áudios gerados pela aplicação "Auramove" são salvos em um local fixo e com nomes pouco descritivos. Isso cria desorganização e torna difícil para os usuários encontrarem e gerenciarem seus arquivos posteriormente.

## 🎯 Objetivo Principal

Melhorar a organização dos arquivos gerados, permitindo que os usuários definam onde desejam salvar suas animações e estabelecendo um padrão de nomenclatura claro e consistente para todos os arquivos.

---

## 🚀 Plano de Implementação

1.  **Permitir a Escolha do Local de Salvamento:** Introduziremos uma configuração que permitirá aos usuários (ou administradores do sistema) definir uma pasta específica para salvar todas as animações geradas. Por padrão, os arquivos continuarão a ser salvos em um local predefinido se nenhuma pasta for especificada.

2.  **Padronizar os Nomes dos Arquivos:** Implementaremos um sistema de nomenclatura automático para garantir que cada arquivo de áudio tenha um nome único e informativo. O nome incluirá a data, a hora e o nome do projeto, facilitando a identificação.

3.  **Garantir a Consistência:** O sistema será responsável por criar a pasta de destino, se ela não existir, e por aplicar o novo padrão de nomenclatura a todos os arquivos gerados, garantindo uma organização consistente em toda a aplicação.

---

## 🛑 Mandato de Execução

👉 **NÃO INICIE A IMPLEMENTAÇÃO.**

A primeira etapa é apresentar uma **Proposta de Arquitetura** em linguagem de negócio, descrevendo como essa nova funcionalidade de organização de arquivos será integrada à experiência do usuário. Aguarde a aprovação antes de prosseguir.

---

## 🎯 Definição de Concluído

-   A aplicação permite configurar um diretório de saída personalizado para os arquivos gerados.
-   Todos os arquivos de áudio são salvos com um nome padronizado, incluindo data, hora e nome do projeto.
-   O sistema funciona de forma transparente para o usuário, gerenciando a criação de pastas e a nomeação de arquivos automaticamente.
-   A localização e a busca por arquivos gerados anteriormente tornaram-se mais fáceis e intuitivas.
