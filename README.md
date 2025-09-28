# Backend MVP Carteira de Ativos
Backend do MVP Desenvolvimento Fullstack da Pós Graduação PUC-Rio

---

## Como rodar

1. Criar a virtualenv:
```bash
python -m venv .venv
```
2. Ative a virtualenv:
```bash
# Linux/Mac
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode a aplicação
```bash
flask run --host=0.0.0.0 --port=5000
```

Para abrir a documentação no navegador, abra http://localhost:5000/openapi/swagger