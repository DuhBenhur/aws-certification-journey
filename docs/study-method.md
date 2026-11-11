# Método de estudo

## O ciclo de cada seção

```
assistir → anotar → praticar → revisar → commitar
```

1. **Assistir** a seção do curso. Pausar nas demos e reproduzir junto.
2. **Anotar** no arquivo da seção em `notes/` (modelo em [templates/section-notes.md](../templates/section-notes.md)):
   - resumo em poucas linhas, com as **minhas palavras**
   - serviços: *o que é* e *quando usar* (é isso que a prova cobra)
   - pegadinhas de prova
   - **conexão com dados/ML**: como esse serviço aparece num pipeline de dados ou de ML
3. **Praticar**: demos que valem repetir viram um lab em `labs/` ([templates/lab.md](../templates/lab.md)), sempre com custo estimado e **limpeza**.
4. **Revisar**: no dia seguinte, reler o resumo e responder as pegadinhas sem olhar.
5. **Commitar** o avanço.

## Simulados

- Ao terminar o curso: simulados completos e cronometrados (Udemy + *Official Practice Question Set* no AWS Skill Builder).
- Registrar cada tentativa em `practice-exams/` ([templates/practice-exam.md](../templates/practice-exam.md)).
- Errei uma questão? Anotar **por que** a resposta certa é a certa e voltar à nota da seção.
- **Regra para agendar:** ≥ 80% em dois simulados seguidos, sem consultar nada.

## Depois de passar

1. Atualizar a tabela da trilha no [README](../README.md): status ✅, data e link da credencial (Credly).
2. Usar o **voucher de 50%** que a AWS libera após cada aprovação para agendar a próxima prova.
3. Escrever um mini-retrospectivo no README da certificação: o que funcionou, o que eu mudaria.

## Commits

Formato `tipo(escopo): descrição curta`, por exemplo `notes(clf): seção 02 IAM`. Faça um commit por seção, lab ou simulado.
Tipos, regras, branches, tags por certificação e a cola de comandos estão no [guia de Git](git-guide.md).

## Python em paralelo

Python é o ponto a fortalecer. A estratégia é usar o SQL como ponte. Veja [python/README.md](../python/README.md).
Meta realista: **2 sessões curtas de Python por semana** durante a CLF-C02, intensificando a partir da AIF-C01/MLA-C01, quando os labs passam a usar `boto3` e notebooks.
