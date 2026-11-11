# Python para dados: usando o SQL como ponte

Eu já penso em dados com SQL. A estratégia aqui é aprender Python **traduzindo o que eu já sei**, e depois aplicar direto na AWS.

## Fases

| Fase | Quando | Conteúdo | Pronto quando... |
|---|---|---|---|
| 1. Fundamentos | durante a CLF-C02 | tipos, listas, dicts, funções, loops, comprehensions, f-strings, ler/escrever arquivos | escrevo um script que lê um CSV e imprime um resumo |
| 2. pandas pensando em SQL | CLF-C02 → AIF-C01 | tabela abaixo; refazer em pandas consultas que já escrevi em SQL | traduzo qualquer query minha para pandas |
| 3. Python + AWS (`boto3`) | AIF-C01 | S3 (listar, upload, download), Athena (rodar SQL pelo Python), Bedrock (chamar um modelo) | automatizo um fluxo S3 → Athena → DataFrame |
| 4. Machine Learning | antes da MLA-C01 | scikit-learn (split, pipeline, métricas), SageMaker SDK | treino e avalio um modelo de ponta a ponta |

## Cola: SQL → pandas

| SQL | pandas |
|---|---|
| `SELECT a, b FROM t` | `df[["a", "b"]]` |
| `WHERE a > 10 AND b = 'x'` | `df.query("a > 10 and b == 'x'")` |
| `ORDER BY a DESC` | `df.sort_values("a", ascending=False)` |
| `LIMIT 10` | `df.head(10)` |
| `SELECT DISTINCT a` | `df["a"].unique()` |
| `COUNT(*) ... GROUP BY g` | `df.groupby("g").size()` |
| `SUM(v), AVG(v) ... GROUP BY g` | `df.groupby("g").agg(total=("v", "sum"), media=("v", "mean"))` |
| `HAVING SUM(v) > 100` | `...agg(total=("v", "sum")).query("total > 100")` |
| `INNER JOIN u ON t.id = u.id` | `df.merge(u, on="id", how="inner")` |
| `LEFT JOIN` | `df.merge(u, on="id", how="left")` |
| `UNION ALL` | `pd.concat([df1, df2])` |
| `CASE WHEN a > 10 THEN 'alto' ELSE 'baixo' END` | `np.where(df["a"] > 10, "alto", "baixo")` |
| `COALESCE(a, 0)` | `df["a"].fillna(0)` |
| `WHERE a IS NULL` | `df[df["a"].isna()]` |
| `SUM(v) OVER (PARTITION BY g)` | `df.groupby("g")["v"].transform("sum")` |
| `ROW_NUMBER() OVER (PARTITION BY g ORDER BY d)` | `df.sort_values("d").groupby("g").cumcount() + 1` |

> ⚠️ O ambiente usa **pandas 3**. Tutoriais antigos mostram padrões que mudaram. Atribuição encadeada como `df[df.a > 0]["b"] = 1` **não funciona** mais; use `df.loc[df.a > 0, "b"] = 1`.

## Organização

```
python/
├── notebooks/     # NN-tema.ipynb: um notebook por assunto
├── exercises/     # scripts .py de exercícios
└── data/          # amostras pequenas (data/raw/ fica fora do git)
```

## Rotina

- 2 sessões curtas por semana durante a CLF-C02
- Cada sessão termina com um commit: `python: <o que aprendi>`
- Nunca usar dados reais do trabalho: gerar dados fictícios ou usar datasets públicos
