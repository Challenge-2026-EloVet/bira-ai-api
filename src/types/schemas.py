from pydantic import BaseModel, Field
from typing import List, Literal, Optional

# Dados que chegam do Portal do Veterinário (Input)
class SoapInput(BaseModel):
    subjective: str = Field(..., description="Relato do tutor sobre comportamento e sintomas")
    objective: str = Field(..., description="Exame clínico físico feito pelo veterinário")
    assessment: str = Field(..., description="Pré-diagnóstico ou hipóteses identificadas")
    plan: str = Field(..., description="Tratamentos, exames e medicamentos sugeridos")

class PetInput(BaseModel):
    id: str = Field(..., example="ELO-1234")
    nome: str = Field(..., example="Thor")
    especie: str = Field(..., example="Cão")
    raca: str = Field(..., example="Dachshund")
    idade_anos: int = Field(..., example=4)
    peso_kg: float = Field(..., example=9.5)

class AnalysisRequest(BaseModel):
    pet: PetInput
    soap: SoapInput
    veterinario: Optional[str] = Field(None, example="Dra. Helena Costa", description="Responsável pelo atendimento")

# Estrutura de dados que a IA DEVE retornar (Structured Output)
class TreatmentTask(BaseModel):
    tarefa: str = Field(..., description="O que fazer de forma clara")
    horario: str = Field(..., description="Frequência ou horário da ação")

class AnalysisOutput(BaseModel):
    diagnostico_provavel: str = Field(..., description="Análise simplificada do caso para o Veterinário")
    risco_epidemiologico: Literal["BAIXO", "MÉDIO", "ALTO"] = Field(..., description="Nível de risco baseado na raça/peso")
    sugestoes_exames: List[str] = Field(..., description="Exames adicionais sugeridos com base científica")
    mensagem_acolhimento_tutor: str = Field(..., description="Texto afetuoso e leigo explicando a situação para o tutor")
    checklist_tratamento: List[TreatmentTask] = Field(..., description="Passo a passo terapêutico para o WhatsApp")
    checklist_prevencao: List[str] = Field(..., description="Recomendações de rotina e prevenção ligadas à raça")

# Resposta da API: o Structured Output + a origem da inferência (rastreabilidade do fallback)
class AnalysisResponse(AnalysisOutput):
    origem: Literal["gemini", "mock", "fallback"] = Field(..., description="gemini = inferência real; mock = sem chave configurada; fallback = Gemini indisponível")
