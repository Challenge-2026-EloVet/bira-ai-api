# 🐾 Bira AI — Microsserviço de IA Clínica & RAG (Sprint 3)

> **FIAP Challenge 2026 — Clyvo Vet** | **Disciplina:** Disruptive Architectures: IoT, IoB & Generative AI

---

Integrantes:

| Nome               | RM       |
| ------------------ | -------- |
| Arthur Graciani    | RM561728 |
| Gustavo Oliveira   | RM566358 |
| João Pedro Scarpin | RM565421 |
| Lucas Hideki       | RM565355 |
| Wesley Andrade     | RM563593 |

## 🎯 Objetivo da Sprint 3

O **Bira AI** é o microsserviço em Python/FastAPI do ecossistema **Elo Vet**, responsável por:

1. **Interpretação SOAP:** Consumir notas brutas de anamnese veterinária (_Subjetivo, Objetivo, Avaliação e Plano_).
2. **RAG Epidemiológico:** Cruzar dados de raça e peso do pet com regras científicas de predisposição médica.
3. **Structured Outputs (Pydantic v2):** Garantir retornos JSON determinísticos e validados para o frontend.
4. **Handoff Tutor (IoB):** Converter a conduta médica em um plano de cuidados humanizado enviado via WhatsApp.

---

## 🛠️ Tech Stack & Arquitetura

- **API & Core:** Python 3.12 | FastAPI | Uvicorn
- **Motor de IA & Schemas:** OpenAI API (GPT-4o-mini) | Pydantic v2 | RAG Local
- **Infraestrutura & Mensageria:** MongoDB | RabbitMQ | Docker & Docker Compose

---

## 🚀 Como Executar

```bash
# 1. Acessar a pasta do microsserviço
cd services/clinical-ai

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1

# 3. Instalar dependências e rodar a aplicação
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

- **Swagger UI:** `http://localhost:8000/docs`
- **Health Check:** `http://localhost:8000/health`
- **Docker:** `docker-compose up -d --build`

---

## 📡 Endpoint Principal: `POST /api/ai/analyze`

### 📥 Payload de Entrada (SOAP + Pet):

```json
{
  "pet": {
    "id": "ELO-1234",
    "nome": "Thor",
    "raca": "Dachshund",
    "idade_anos": 4,
    "peso_kg": 9.5
  },
  "soap": {
    "subjective": "Thor está amuado há dois dias e chora ao ser pego no colo.",
    "objective": "Dor à palpação toracolombar. Sem déficit neurológico.",
    "assessment": "Suspeita de dor lombar / Discopatia intervertebral.",
    "plan": "Repouso estrito em espaço delimitado e analgésico por 5 dias."
  }
}
```

### 📤 Resposta Estruturada (Pydantic Output):

```json
{
  "diagnostico_provavel": "Suspeita de discopatia por sobrecarga mecânica na coluna (Dachshund, 9.5kg).",
  "risco_epidemiologico": "ALTO",
  "sugestoes_exames": ["Radiografia Lombo-Sacra", "Avaliação Fisioterápica"],
  "mensagem_acolhimento_tutor": "Compreendemos sua preocupação com o Thor. A raça Dachshund exige cuidados redobrados com a coluna. Mantenha o repouso estrito prescrito.",
  "checklist_tratamento": [
    {
      "tarefa": "Administrar analgésico veterinário",
      "horario": "A cada 12h durante 5 dias"
    },
    {
      "tarefa": "Restrição estrita de espaço",
      "horario": "Contínuo (24h)"
    }
  ]
}
```

---

## 🔗 Links da Entrega (Sprint 3)

- 📹 **Vídeo Pitch (YouTube Unlisted):** `https://youtu.be/Nh5_oaTWsOI`
- 🐙 **Repositório GitHub:** `https://github.com/Challenge-2026-EloVet/bira-ai-api`

---

_Elo Vet — Cuidar de quem amamos: é isso que nos une._ 🐾
