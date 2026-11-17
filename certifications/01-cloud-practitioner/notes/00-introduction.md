# 00 — Introduction

> **Curso:** Ultimate AWS Certified Cloud Practitioner CLF-C02 · **Slides:** p.1–11 · **Status:** ✅ concluída
> **Data:** 2026-11-16

## Resumo (com as minhas palavras)

A AWS (Amazon Web Services) é a plataforma de nuvem da Amazon, com mais de 200 serviços de computação, armazenamento, redes, segurança e bancos de dados, entre outros. O curso me prepara para a **CLF-C02**, a certificação de entrada da AWS, e cobre pouco mais de 40 desses serviços, misturando teoria com prática (hands-on) numa conta AWS própria. A prova não exige detalhe técnico profundo: exige saber **qual serviço resolve qual problema** e separar a resposta certa das alternativas que só parecem certas.

## Serviços e conceitos

| Serviço / conceito | O que é | Quando usar |
|---|---|---|
| AWS (Amazon Web Services) | Plataforma de nuvem da Amazon, com mais de 200 serviços | Hospedar sites e APIs, armazenar arquivos, executar aplicações e bancos de dados |
| CLF-C02 (Cloud Practitioner) | Certificação de nível Foundational: valida os fundamentos de nuvem e os principais serviços da AWS | Primeiro passo da trilha. Não exige experiência prévia |
| Hands-on | Praticar na própria conta AWS o que foi visto na teoria | Em todas as demos do curso: aprender fazendo é a técnica principal |
| Créditos do Free Tier | Uma conta nova recebe US$ 100 em créditos, que podem chegar a US$ 200 | Fazer os labs sem tirar dinheiro do bolso. Os recursos criados consomem os créditos |
| AWS Skill Builder | Plataforma oficial de treinamento da AWS. Tem o conjunto oficial de questões de prática da CLF-C02 | Simulados no fim do curso, junto com os da Udemy |

### Níveis de certificação da AWS

| Nível | Para quem | Na minha trilha |
|---|---|---|
| Foundational | Fundamentos de nuvem; não precisa de experiência prévia | CLF-C02, AIF-C01 |
| Associate | Habilidades centrais na AWS; experiência anterior com nuvem ou TI é recomendada | MLA-C01, SAA-C03 |
| Professional | Arquitetura e soluções avançadas; pede 2+ anos de experiência com AWS | AIP-C01 |
| Specialty | Especialização numa área específica | SCS-C03 |

A AIB-C01 é uma certificação nova, voltada a negócios (beta em 2026), e não aparece nesse quadro do curso.

### Como o curso funciona

- São 20 seções, de "O que é cloud computing" até a preparação para a prova. O roteiro com o progresso fica no [README da certificação](../README.md).
- Conhecimento básico de TI ajuda, mas não é obrigatório.
- É um curso longo: o importante é constância, não velocidade.

## Pegadinhas de prova

- **Formato da prova:** questões de cenário, de múltipla escolha (1 correta) ou de múltipla resposta (2 ou mais corretas).
- **As alternativas erradas são serviços reais** (distratores). Alguns eu vou estudar, outros o curso nem cobre. Eliminar o que não tem relação com o cenário já resolve muita questão.
- **O nome do serviço costuma dar a pista.** Ex.: "migrar um banco de dados para a AWS" → AWS **Database Migration** Service (DMS).
- **Nunca deixar questão em branco:** em branco conta como erro, e o chute não tira ponto.
- **Das 65 questões, 15 não valem nota** (são testes da AWS), mas não dá para saber quais. Tratar todas como valendo.

## Conexão com dados / ML

- Como a AWS oferece bancos de dados, armazenamento e poder de processamento, também dá para construir aplicações de ML e IA dentro dela.
- Dos serviços do curso, os que mais vão voltar na minha trilha de dados e ML são o **S3** (data lake), o **Athena** (SQL direto no S3), o **Glue** (ETL), o **Redshift** (data warehouse), o **SageMaker** (ML) e o **Bedrock** (IA generativa). A CLF apresenta esses serviços, e a AIF e a MLA aprofundam.

## Dúvidas

- [ ] Conferir as regras do plano gratuito na minha conta nova (créditos e prazo) antes de começar os labs.
