# 01 — What is Cloud Computing

> **Curso:** Ultimate AWS Certified Cloud Practitioner CLF-C02 · **Slides:** p.12–40 · **Status:** ✅ concluída
> **Data:** 2026-11-16

## Resumo (com as minhas palavras)

Cloud computing é a entrega de servidores, armazenamento, redes e bancos de dados pela internet, sob demanda e com escala. A cobrança é feita conforme o uso (*pay-as-you-go*).

A AWS tem uma infraestrutura global distribuída, com servidores no mundo inteiro. Ela combina **Regiões**, **Availability Zones (AZs)** e **Edge Locations** para oferecer escala, resiliência e baixa latência.

## Serviços e conceitos

| Serviço / conceito | O que é | Quando usar |
|---|---|---|
| Computação | Servidores virtuais na nuvem que executam aplicações e processam dados | Rodar sites, APIs e processamentos, contratando só a capacidade necessária |
| Armazenamento | Espaço para guardar arquivos e dados | Backups, documentos, imagens, data lake |
| Bancos de dados | Bancos gerenciados pela AWS, sem precisar cuidar do servidor | Guardar e consultar os dados das aplicações |
| Região | Área geográfica independente que reúne vários serviços da AWS | Escolher pela regulamentação dos dados (compliance), pela latência até os usuários, pelos serviços disponíveis e pelo preço |
| Availability Zone (AZ) | Um ou mais data centers isolados dentro de uma região | Distribuir a aplicação em mais de uma AZ para ter redundância e alta disponibilidade |
| Edge Location | Ponto próximo aos usuários que entrega conteúdo com baixa latência | Distribuir conteúdo (sites, vídeos) para usuários no mundo todo |

## Pegadinhas de prova

- **Região ≠ AZ:** uma região tem várias AZs (normalmente 3). Alta disponibilidade = usar mais de uma AZ.
- **Nem todo serviço existe em todas as regiões.** A disponibilidade do serviço é um dos critérios para escolher a região.
- **"Os dados não podem sair do país"** no enunciado → a região é escolhida por compliance.
- **Transferência de dados:** entrar na AWS é grátis; sair da AWS é cobrado.

## Conexão com dados / ML

- **Amazon SageMaker** é uma plataforma (PaaS) de ML: estrutura completa para treinar e rodar modelos, construir pipelines e acompanhar o ciclo de vida, incluindo o retreino.
- **Amazon Bedrock** oferece modelos de IA generativa como serviço, consumidos por API.

## Dúvidas

- [ ] Aprofundar a diferença entre SageMaker e Bedrock (assunto da AIF-C01 e da MLA-C01).
