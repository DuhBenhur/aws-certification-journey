# Guia de Git: fluxo, commits e boas práticas

Como versiono este repositório. O objetivo é que qualquer pessoa, lendo apenas o histórico (`git log`), entenda a jornada: o que estudei, quando e em que ordem.

Os comandos funcionam iguais no Git Bash, no PowerShell e no terminal do VS Code.

---

## 1. O fluxo do dia a dia

```bash
git pull                     # (início) trazer o que estiver no GitHub, se usar mais de um PC
git status                   # o que mudou?
git diff                     # ver as mudanças linha a linha
git add <arquivo>            # preparar para o commit (stage); "git add ." prepara tudo
git diff --staged            # revisar exatamente o que vai entrar no commit
git commit -m "notes(clf): seção 02 IAM"
git push                     # (fim) enviar para o GitHub
```

> No VS Code, o painel **Source Control** (`Ctrl+Shift+G`) faz o mesmo visualmente: `+` prepara o arquivo, a caixa de texto recebe a mensagem e ✓ faz o commit.

**Hábito:** terminou uma seção ou um lab? Commit. Terminou a sessão de estudo? Push.

---

## 2. Mensagens de commit

### Formato

```
tipo(escopo): resumo curto no presente, sem ponto final

Corpo opcional explicando o PORQUÊ da mudança.
O diff já mostra O QUE mudou; a mensagem conta o motivo.
```

Baseado em [Conventional Commits](https://www.conventionalcommits.org/pt-br/), adaptado para estudo.

### Tipos

| Tipo | Uso | Exemplo |
|---|---|---|
| `notes` | anotações de seção | `notes(clf): seção 06 S3 e classes de armazenamento` |
| `lab` | hands-on | `lab(clf): site estático no S3 com política pública` |
| `exam` | simulados e provas | `exam(clf): simulado 2, 78% (Security abaixo de 70%)` |
| `python` | estudo de Python | `python: groupby e merge comparados com SQL` |
| `docs` | README, guias, trilha | `docs: marca CLF-C02 como aprovada` |
| `fix` | correção de algo errado | `fix(clf): corrige diferença entre SG e NACL na nota 13` |
| `chore` | estrutura, configs, dependências | `chore: adiciona scikit-learn ao requirements` |

**Escopos:** `clf`, `aif`, `aib`, `mla`, `saa`, `aip`, `scs` (um por certificação).

### Regras

- **Resumo com até 72 caracteres** (o ideal é ~50). É o que aparece no GitHub e no `git log --oneline`.
- **Verbo no presente, 3ª pessoa:** "adiciona", "corrige", "conclui". Mantém o histórico uniforme.
- **Um assunto por commit.** Se a mensagem precisa de "e", provavelmente são dois commits.
- **Corpo quando houver contexto:** uma decisão, um erro que levou à mudança, um link.

### Bons vs ruins

| ❌ Evitar | ✅ Preferir |
|---|---|
| `update` | `notes(clf): seção 03 EC2, tipos de instância` |
| `wip` / `aaa` / `coisas` | `lab(clf): servidor web com user data` |
| `arrumei umas notas` | `fix(clf): corrige limites do S3 na nota 06` |
| `simulado` | `exam(clf): simulado 1, 72% (Billing é o ponto fraco)` |

### Commit com corpo, pelo terminal

```bash
git commit -m "lab(clf): site estático no S3" -m "Bucket com website hosting e política de leitura pública. Recursos apagados ao final (ver seção Limpeza)."
```

Ou só `git commit` (sem `-m`), que abre o editor para escrever título, linha em branco e corpo.

---

## 3. Commits atômicos

Cada commit deve ser **uma unidade que faz sentido sozinha**: uma seção, um lab, um simulado.

```bash
git add certifications/01-cloud-practitioner/notes/02-iam.md   # só um arquivo
git add -p                                                     # escolher trechos (hunks) um a um
```

Commits pequenos e frequentes deixam o **gráfico de contribuições** do GitHub constante. Para quem avalia o portfólio, constância vale mais que volume.

---

## 4. Branches e Pull Requests (para labs maiores)

Notas do dia a dia podem ir direto na `main`. Para um **lab maior**, uma branch com Pull Request mostra o fluxo usado em times de verdade:

```bash
git switch -c lab/clf-s3-static-site       # cria a branch e muda para ela
# ... trabalha e faz commits ...
git push -u origin lab/clf-s3-static-site  # publica a branch
```

No GitHub: **Compare & pull request**. Descreva o objetivo, as evidências e a limpeza, e faça o merge. Depois:

```bash
git switch main
git pull
git branch -d lab/clf-s3-static-site       # apaga a branch local já mesclada
```

**Nomes de branch:** `lab/<cert>-<tema>`, `notes/<cert>-<secao>`, `docs/<tema>`.

---

## 5. Tags e Releases: os marcos da jornada

Ao passar numa prova, marque o momento no histórico:

```bash
git tag -a clf-c02 -m "AWS Certified Cloud Practitioner: aprovado em AAAA-MM-DD"
git push origin clf-c02
```

No GitHub, vá em **Releases → Draft a new release**, escolha a tag e cole a retrospectiva e o link do Credly. A página de Releases vira uma **linha do tempo das certificações**.

---

## 6. Desfazer coisas (cola)

| Situação | Comando | Cuidado |
|---|---|---|
| Descartar mudanças de um arquivo (não commitado) | `git restore <arquivo>` | Irreversível |
| Tirar um arquivo do stage | `git restore --staged <arquivo>` | Mantém as mudanças |
| Corrigir a mensagem do último commit | `git commit --amend -m "nova mensagem"` | **Só antes do push** |
| Esqueci um arquivo no último commit | `git add <arquivo>` e depois `git commit --amend --no-edit` | **Só antes do push** |
| Desfazer o último commit, mantendo as mudanças | `git reset --soft HEAD~1` | **Só antes do push** |
| Desfazer um commit que já está no GitHub | `git revert <hash>` | Seguro: cria um commit inverso |

> **Regra de ouro:** depois do push, não reescreva o histórico da `main` (nada de `--amend`, `reset` ou `push --force`). Use `git revert`.

---

## 7. Investigar o histórico

```bash
git log --oneline --graph --decorate -20   # visão geral
git log --stat -5                          # quais arquivos cada commit mudou
git show <hash>                            # detalhes de um commit
git log -- <arquivo>                       # histórico de um arquivo
git log --grep="clf"                       # commits que citam a CLF
git blame <arquivo>                        # quem/quando mudou cada linha
```

---

## 8. Segurança

- O hook [`.githooks/pre-commit`](../.githooks/pre-commit) bloqueia chaves AWS, chaves privadas, arquivos acima de 5 MB e material do curso. **Num clone novo, ative de novo:** `git config core.hooksPath .githooks`
- **Nunca versionar:** credenciais, `.env`, prints com account ID ou ARN completo, dados do trabalho.
- `git commit --no-verify` pula o hook. Use só depois de revisar e ter certeza de que é falso positivo.

### Se uma chave vazar

1. **Primeiro desative e apague a chave no IAM, imediatamente.** Robôs varrem o GitHub em minutos, e apagar o arquivo não tira a chave do histórico nem de forks.
2. Confira o CloudTrail e o Billing atrás de uso indevido.
3. Só depois limpe o histórico, se ainda fizer sentido.

---

## 9. Git como portfólio

- **Histórico legível:** o `git log --oneline` deve contar a jornada sozinho.
- **Constância:** pequenas sessões commitadas com frequência.
- **README vivo:** atualize a tabela da trilha a cada avanço.
- **Releases por certificação** (seção 5).
- **Issues como backlog (opcional):** uma issue por seção do curso. Um commit com `closes #N` fecha a issue automaticamente ao chegar na `main`:
  `notes(clf): seção 02 IAM (closes #3)`
- **Repositório fixado** no perfil do GitHub.

---

## 10. Configurações úteis (uma vez por máquina)

```bash
git config --global user.name "Seu Nome Completo"   # nome que aparece nos commits
git config --global init.defaultBranch main
git config --global pull.rebase true                # histórico linear ao dar pull
git config --global alias.lg "log --oneline --graph --decorate -20"   # atalho: git lg
```

O e-mail do commit (`git config user.email`) precisa ser um e-mail **verificado na sua conta do GitHub** para os commits contarem no gráfico de contribuições.
