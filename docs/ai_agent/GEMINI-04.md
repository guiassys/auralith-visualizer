Este prompt herda todas as diretrizes e restrições do template principal: `@/docs/ai_agent/GEMINI.md`.

# 🚀 Proposta de Centralização de Configurações

## 🌍 Contexto

Atualmente, muitos dos parâmetros que controlam o comportamento da aplicação "Auramove" (como a duração do vídeo, qualidade da imagem, etc.) estão fixos diretamente no código-fonte. Isso significa que qualquer ajuste, por menor que seja, exige uma alteração técnica, tornando o processo lento e arriscado.

## 🎯 Objetivo Principal

Tornar a aplicação "Auramove" mais flexível e fácil de manter, movendo todas as configurações importantes para um local central e de fácil acesso. Isso permitirá que ajustes finos sejam feitos rapidamente, sem a necessidade de intervenção de um desenvolvedor.

---

## 🚀 Plano de Implementação

1.  **Criar um Arquivo de Configuração Central:** Identificaremos todos os parâmetros importantes que hoje estão fixos no código e os moveremos para um arquivo de configuração central. Parâmetros como duração do vídeo, dimensões e outros ajustes de qualidade serão incluídos.

2.  **Adaptar a Aplicação para Ler a Configuração:** Modificaremos a aplicação para que, em vez de usar valores fixos, ela leia e aplique as configurações definidas neste novo arquivo central.

3.  **Garantir a Manutenibilidade:** Essa mudança simplificará futuras atualizações e testes, pois permitirá que a equipe ajuste o comportamento da aplicação de forma rápida e segura, simplesmente editando o arquivo de configuração.

---

## 🛑 Mandato de Execução

👉 **NÃO INICIE A IMPLEMENTAÇÃO.**

A primeira etapa é apresentar uma **Proposta de Arquitetura** em linguagem de negócio, explicando como essa centralização de configurações facilitará a gestão do produto e quais benefícios trará para a agilidade da equipe. Aguarde a aprovação antes de prosseguir.

---

## 🎯 Definição de Concluído

-   Todas as configurações importantes da aplicação estão centralizadas em um único arquivo.
-   A aplicação carrega e utiliza essas configurações durante sua execução.
-   Ajustar parâmetros como a duração ou a qualidade do vídeo não exige mais alterações no código-fonte.
-   A manutenção e a experimentação com novas configurações tornaram-se mais rápidas e seguras.
