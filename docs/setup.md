# Setup do ambiente

Guia para montar o ambiente do zero (ou num computador novo). Todos os comandos são para **PowerShell**, na raiz do repositório.

## 1. Pré-requisitos

| Ferramenta | Verificar | Instalar |
|---|---|---|
| Git | `git --version` | `winget install Git.Git` |
| Python 3.13 | `python --version` | `winget install Python.Python.3.13` |
| AWS CLI v2 | `aws --version` | `winget install Amazon.AWSCLI` |
| VS Code | `code --version` | `winget install Microsoft.VisualStudioCode` |
| GitHub CLI (opcional) | `gh --version` | `winget install GitHub.cli` |

## 2. Ambiente Python (venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Se o PowerShell bloquear o `Activate.ps1`, rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

No VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → escolha `.venv`.
Para notebooks: `jupyter lab` (ou abra o `.ipynb` direto no VS Code e escolha o kernel `.venv`).

## 3. Conta AWS de estudos ⚠️

**Não faça os labs na conta do trabalho.** Crie uma conta pessoal só para estudo. O curso ensina boa parte disso na seção de IAM; quando chegar lá, volte aqui.

1. Crie a conta em <https://aws.amazon.com/> e ative **MFA no usuário root**. Depois disso, não use o root no dia a dia.
2. Crie um usuário administrador para você (IAM Identity Center ou usuário IAM, como no curso).
3. Configure um **perfil nomeado** na CLI, separado do `default`:
   ```powershell
   aws configure --profile estudos      # chaves de acesso
   # ou
   aws configure sso                    # Identity Center (recomendado)
   ```
4. Crie o `.env` (ignorado pelo git) apontando para esse perfil:
   ```powershell
   Copy-Item .env.example .env
   ```
5. Teste: `aws sts get-caller-identity --profile estudos`

## 4. Proteção de custos (fazer no primeiro dia)

- **AWS Budgets** → *Create budget* → template **Zero spend budget**. Você recebe um e-mail no primeiro centavo gasto.
- Confira as condições do Free Tier da sua conta em *Billing and Cost Management*.
- Todo lab tem uma seção **Limpeza**. Só considere o lab concluído depois de apagar os recursos.

## 5. Git

```powershell
git config core.hooksPath .githooks   # ativa o hook anti-vazamento de segredos
```

O hook [`.githooks/pre-commit`](../.githooks/pre-commit) bloqueia commits que contenham chaves AWS, chaves privadas, arquivos > 5 MB ou qualquer coisa de `course-materials/`.

### Publicar no GitHub (primeira vez)

1. Em <https://github.com/new>, crie um repositório **vazio** (sem README, sem .gitignore). Sugestão de nome: `aws-certification-journey`.
2. Conecte e envie:
   ```powershell
   git remote add origin https://github.com/<seu-usuario>/aws-certification-journey.git
   git push -u origin main
   ```

## 6. Validar tudo

```powershell
python scripts/check_env.py
```

O script confere Python, venv, pacotes e credenciais AWS. Por segurança, ele só chama a AWS se `AWS_PROFILE` apontar para um perfil diferente de `default`.
