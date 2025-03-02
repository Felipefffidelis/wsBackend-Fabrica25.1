# wsBackend-Fabrica25.1
 
Aqui está um exemplo de **`README.md`** para o seu projeto Django com integração da Fixer API. Ele inclui requisitos, exemplos de uso e instruções para configurar e rodar o projeto.

---

# Finance Manager

Este é um projeto Django para gerenciamento de transações financeiras com suporte a conversão de moedas usando a **Fixer API**. O sistema permite cadastrar moedas, transações e realizar conversões entre moedas com taxas de câmbio atualizadas.

---

## **Funcionalidades**

1. **Cadastro de Moedas:**
   - Adicione moedas com código (ex: USD, EUR, BRL) e nome (ex: Dólar Americano, Euro, Real Brasileiro).

2. **Cadastro de Transações:**
   - Registre transações com valor, moeda, data e descrição.

3. **Conversão de Moedas:**
   - Converta valores entre moedas usando taxas de câmbio em tempo real da Fixer API.

4. **Atualização Automática de Taxas:**
   - As taxas de câmbio são atualizadas automaticamente diariamente.

---

## **Requisitos**

- Python 3.8 ou superior
- Django 4.2 ou superior
- Fixer API Key (obtenha em [https://fixer.io](https://fixer.io))
- Redis (para agendamento de tarefas com Celery)

---

## **Instalação**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/finance-manager.git
   cd finance-manager
   ```

2. **Crie um ambiente virtual e instale as dependências:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure a Fixer API Key:**

   Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Fixer API:

   ```env
   FIXER_API_KEY=sua_chave_aqui
   ```

4. **Aplique as migrações:**

   ```bash
   python manage.py migrate
   ```

5. **Sincronize as moedas iniciais:**

   Execute o seguinte comando para cadastrar as moedas suportadas:

   ```bash
   python manage.py shell
   ```

   No shell do Django, execute:

   ```python
   from transactions.utils import sync_currencies
   sync_currencies()
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

7. **Inicie o Celery (para atualização automática de taxas):**

   Em um terminal separado, execute:

   ```bash
   celery -A Project worker --loglevel=info
   celery -A Project beat --loglevel=info
   ```

---

## **Como Usar**

### **1. Cadastrar Moedas**

Acesse a página de cadastro de moedas:

```
http://localhost:8000/currency/create/
```

- **Código:** Insira o código da moeda (ex: USD, EUR, BRL).
- **Nome:** Insira o nome da moeda (ex: Dólar Americano, Euro, Real Brasileiro).

### **2. Cadastrar Transações**

Acesse a página de cadastro de transações:

```
http://localhost:8000/transaction/create/
```

- **Valor:** Insira o valor da transação.
- **Moeda:** Selecione a moeda da transação.
- **Data:** Insira a data da transação.
- **Descrição:** Adicione uma descrição (opcional).

### **3. Converter Moedas**

Acesse a página de conversão de moedas:

```
http://localhost:8000/convert/
```

- **Moeda Base:** Selecione a moeda de origem.
- **Moeda Alvo:** Selecione a moeda de destino.
- Clique em **Converter** para ver a taxa de câmbio atual.

---

## **Exemplos**

### **Exemplo 1: Cadastrar uma Moeda**

- **Código:** `USD`
- **Nome:** `Dólar Americano`

### **Exemplo 2: Cadastrar uma Transação**

- **Valor:** `100.00`
- **Moeda:** `USD`
- **Data:** `2023-10-01`
- **Descrição:** `Compra de produtos`

### **Exemplo 3: Converter Moedas**

- **Moeda Base:** `USD`
- **Moeda Alvo:** `BRL`
- **Resultado:** `1 USD = 5.30 BRL`

---

## **Estrutura do Projeto**

```
finance-manager/
│
├── Project/                  # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── transactions/             # App de transações
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── utils.py
│   ├── tasks.py
│   └── templates/
│       └── transactions/
│           ├── base.html
│           ├── currency_list.html
│           ├── currency_form.html
│           ├── currency_confirm_delete.html
│           ├── transaction_list.html
│           ├── transaction_form.html
│           ├── transaction_confirm_delete.html
│           └── convert_currency.html
│
├── manage.py
├── requirements.txt
└── .env
```