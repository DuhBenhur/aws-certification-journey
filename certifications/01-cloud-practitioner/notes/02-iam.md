# 02 — IAM

> **Curso:** Ultimate AWS Certified Cloud Practitioner CLF-C02 · **Slides:** p.41–58 · **Status:** 🟨 em andamento
> **Data:** 2026-11-16

## Resumo (com as minhas palavras)

O IAM (Identity and Access Management) controla **quem** acessa a conta AWS e **o que** cada um pode fazer. É um serviço **global**. As identidades (usuários, grupos e roles) recebem permissões por meio de **policies**, documentos JSON que devem seguir o **princípio do menor privilégio**.

## Serviços e conceitos

| Serviço / conceito | O que é | Quando usar |
|---|---|---|
| Conta root | Usuário criado junto com a conta, com acesso total | Só em tarefas de configuração da conta; nunca no dia a dia |
| IAM User | Identidade criada dentro da conta que representa uma pessoa ou um propósito específico. Tem credenciais próprias, que não devem ser compartilhadas | Uma pessoa = um usuário |
| IAM Group | Coleção de usuários com permissões em comum. Quem entra no grupo herda as permissões dele | Gerir acessos por equipe, função ou departamento, por exemplo quando vários times precisam de acessos diferentes |
| IAM Role | Identidade com permissões que pessoas, serviços ou outras contas assumem temporariamente | Dar a um serviço AWS (ex.: EC2, Lambda) acesso a outro recurso sem guardar senha ou chave |
| IAM Policy | Documento JSON que define o que é permitido ou negado, e em quais recursos | Anexar a usuários, grupos ou roles para conceder permissões |

### IAM Policies

Um usuário recebe as permissões de **todos os grupos** de que participa, mais as policies anexadas diretamente a ele.

Exemplo: policy que permite ler, mas não gravar, os arquivos de um bucket S3.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LerDadosDoBucket",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::meu-bucket-de-dados",
        "arn:aws:s3:::meu-bucket-de-dados/*"
      ]
    }
  ]
}
```

| Elemento | Para que serve |
|---|---|
| `Version` | Versão da linguagem de policy. Sempre `"2012-10-17"` |
| `Id` | Identificador da policy (opcional) |
| `Statement` | Lista de regras (obrigatório) |
| `Sid` | Nome da regra (opcional) |
| `Effect` | `Allow` (permite) ou `Deny` (nega) |
| `Principal` | Quem a regra afeta. Aparece em policies anexadas ao recurso, como a bucket policy do S3 |
| `Action` | As ações, no formato `serviço:Ação` (ex.: `s3:GetObject`) |
| `Resource` | Em quais recursos a regra vale, identificados pelo ARN |
| `Condition` | Quando a regra vale (opcional; ex.: só a partir de certo IP) |

**Como a AWS decide:** sem permissão explícita, o acesso é **negado**. Um `Deny` explícito **sempre vence** um `Allow`.

### Princípio do menor privilégio

Dar a cada identidade **só as permissões necessárias** para a tarefa, nada além. Na prática:

- começar com o mínimo e liberar mais só quando precisar;
- dar permissões a grupos e roles, não usuário por usuário;
- preferir roles a chaves de acesso fixas;
- revisar com as ferramentas do IAM: o **Access Advisor** mostra quais serviços cada usuário realmente usou (o que nunca é usado pode ser removido), e o **Credentials Report** lista os usuários da conta e o estado das credenciais.

**Paralelo com SQL:** a policy é o `GRANT` da AWS.

| SQL | IAM Policy |
|---|---|
| `GRANT` / `DENY` | `"Effect": "Allow"` / `"Deny"` |
| `SELECT`, `INSERT` | `"Action": "s3:GetObject"`, `"s3:PutObject"` |
| `ON vendas` | `"Resource"`: o ARN do bucket |
| `TO app_relatorios` | o usuário, grupo ou role que recebe a policy |

```sql
-- Menor privilégio: só leitura, só na tabela necessária
GRANT SELECT ON vendas TO app_relatorios;

-- Excesso de permissão: dono do banco inteiro (o equivalente a AdministratorAccess)
ALTER ROLE db_owner ADD MEMBER app_relatorios;
```

No SQL Server, `DENY` também vence `GRANT`: é a mesma lógica do `Deny` explícito.

## Pegadinhas de prova

- **IAM é global:** não se escolhe região para ele.
- **Conta root:** não usar no dia a dia nem compartilhar. Crie um usuário administrador para o trabalho diário.
- **Grupos só contêm usuários**, nunca outros grupos. Um usuário pode estar em vários grupos ou em nenhum.
- **Serviço AWS acessando outro serviço** (ex.: EC2 lendo do S3) → a resposta é **IAM Role**, não uma chave de acesso guardada na instância.
- **"Conceder apenas as permissões necessárias"** no enunciado → princípio do menor privilégio.
- **`Deny` explícito vence `Allow`**, e o que não foi permitido está negado.
- **Uma pessoa = um usuário.** Credenciais nunca são compartilhadas.

## Conexão com dados / ML

- Uma instância EC2 pode assumir uma role para **ler** objetos de um bucket S3, sem permissão para **gravar** nele. É o menor privilégio na prática, e é exatamente a policy de exemplo acima.
- Vale o mesmo para SageMaker, Glue e Lambda: cada job recebe uma role com acesso só aos buckets de que precisa.

## Dúvidas

- Nenhuma por enquanto.
