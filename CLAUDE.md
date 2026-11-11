# CLAUDE.md

Repositório de estudos para certificações AWS (trilha de Cientista de Dados / Engenheiro de ML). Também serve de portfólio público no GitHub.

## Sobre quem estuda

- Usa AWS no dia a dia e domina SQL; está em transição de carreira para Data Science / ML Engineering.
- **Python ainda é ponto fraco.** Explique código Python passo a passo e, sempre que ajudar, compare com o equivalente em SQL.
- Conteúdo em **português (pt-BR)**. Nomes de pastas e arquivos em inglês, kebab-case.

## Estrutura

- `certifications/NN-nome/`: uma pasta por certificação, na ordem da trilha (ver README.md)
  - `notes/NN-secao.md`: uma nota por seção do curso, no modelo `templates/section-notes.md`
  - `labs/NN-nome/README.md`: hands-on, no modelo `templates/lab.md` (sempre com custo e limpeza)
  - `practice-exams/`: registro de simulados, no modelo `templates/practice-exam.md`
  - `course-materials/`: **material do curso, protegido por direitos autorais, fora do git. Nunca versionar, copiar trechos longos ou reproduzir slides.**
- `python/`: trilha de Python para dados (SQL → pandas → boto3 → ML)
- `docs/`: setup do ambiente e método de estudo
- `scripts/check_env.py`: valida o ambiente

## Contexto atual

Se existir `HANDOFF.local.md` na raiz (local, fora do git), **leia antes de começar**: ele traz o estado atual, as decisões tomadas e as pendências.

## Regras

- Commits no formato `tipo(escopo): descrição` (ver `docs/git-guide.md`). Escopos: clf, aif, aib, mla, saa, aip, scs.
- Nunca commitar credenciais, account IDs, ARNs completos ou dados do trabalho. O hook `.githooks/pre-commit` ajuda, mas não substitui atenção.
- Labs rodam só no perfil AWS `estudos` (conta pessoal), nunca no `default`.
- Ao concluir uma seção: marcar o checkbox no README da certificação e atualizar o status da nota.
- Ao passar numa prova: atualizar a tabela e o diagrama da trilha no README principal.
