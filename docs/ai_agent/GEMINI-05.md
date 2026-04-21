Este prompt herda todas as diretrizes e restrições do template principal: `@/docs/ai_agent/GEMINI.md`.

# 🚀 Proposta de Implementação: Aba de Configurações do Usuário

## 🌍 Contexto

Atualmente, os usuários da aplicação "Auramove" não têm controle sobre os parâmetros de geração da animação. Todas as configurações são predefinidas pelo sistema, o que limita a capacidade de usuários mais avançados de ajustarem o resultado final de acordo com suas necessidades específicas.

Além disso, ao permitir que os arquivos sejam salvos em pastas de rede personalizadas, descobrimos que a interface do usuário (Gradio) impõe restrições de segurança e bloqueia o acesso a essas pastas por padrão, resultando em erros durante o download ou visualização do vídeo gerado.

## 🎯 Objetivo Principal

Capacitar os usuários, dando a eles mais controle sobre o processo criativo, e garantir que a experiência de salvamento e visualização de arquivos em locais personalizados (como pastas de rede) funcione perfeitamente.

---

## 🚀 Plano de Implementação

1.  **Adicionar uma Aba de "Configurações" à Interface:** Criaremos uma nova aba na interface principal da aplicação, claramente identificada como "Settings" (Configurações).

2.  **Exibir as Opções de Ajuste:** Dentro desta nova aba, apresentaremos de forma organizada e intuitiva os controles que os usuários poderão modificar. Isso incluirá ajustes relacionados à duração, qualidade e estilo da animação. Os valores padrão serão carregados automaticamente.

3.  **Integrar as Escolhas do Usuário:** A aplicação será modificada para que, ao clicar no botão "Gerar", ela utilize as configurações personalizadas definidas pelo usuário na aba "Settings", em vez dos valores padrão do sistema.

4.  **Permitir Caminhos de Rede Personalizados:** Permitir que o arquivo gerado seja salvo em um diretório de rede Linux ou Windows.

---

## 🛑 Mandato de Execução

👉 **NÃO INICIE A IMPLEMENTAÇÃO.**

A primeira etapa é apresentar uma **Proposta de Arquitetura** em linguagem de negócio, focada na experiência do usuário. Descreva como a nova aba de configurações será apresentada e como as restrições de segurança da interface serão tratadas para permitir o uso fluido de pastas de rede. Aguarde a aprovação antes de prosseguir.

---

## 🎯 Definição de Concluído

-   A interface da aplicação "Auramove" possui uma nova aba "Settings".
-   Nesta aba, os usuários podem visualizar e alterar os principais parâmetros de geração da animação.
-   A aplicação utiliza as configurações personalizadas pelo usuário para gerar o vídeo.
-   O usuário pode especificar um caminho de rede (Windows ou Linux) no campo de diretório de saída, e o arquivo é salvo com sucesso nesse local.
-   A interface do usuário permite a exibição e o download do vídeo gerado na pasta personalizada, sem apresentar erros de restrição de caminho.
-   A experiência do usuário é aprimorada, oferecendo maior flexibilidade e controle sobre o resultado final.
