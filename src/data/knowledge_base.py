import re
import unicodedata

# Base de dados epidemiológicos de suporte à decisão clínica (RAG)
BREED_KNOWLEDGE = {
    "Dachshund": {
        "predisposicoes": ["Doença do Disco Intervertebral (DDIV)", "Hérnia de disco", "Problemas de coluna mecânicos"],
        "peso_limite_alerta": 8.5,
        "diretriz_cientifica": "Evitar que o animal salte de sofás, camas ou utilize escadas. Reduzir a carga mecânica na coluna espinhal através do controle restrito de peso corpóreo. Exercícios de baixo impacto para fortalecimento lombar."
    },
    "Golden Retriever": {
        "predisposicoes": ["Displasia Coxofemoral", "Problemas articulares", "Cardiomiopatias"],
        "peso_limite_alerta": 36.0,
        "diretriz_cientifica": "Evitar pisos escorregadios em casa para proteger articulações coxofemorais. Suplementação preventiva com condroprotetores pode ser avaliada pelo clínico."
    },
    "Shih Tzu": {
        "predisposicoes": ["Ceratoconjuntivite seca (olho seco)", "Problemas respiratórios (braquicefálico)"],
        "peso_limite_alerta": 7.5,
        "diretriz_cientifica": "Limpeza periocular frequente. Monitorar exposição prolongada ao calor intenso devido à restrição anatômica de troca de temperatura."
    }
}


def _normalize(raca: str) -> str:
    # "Shih-tzu", "shih tzu" e "Shih Tzu" viram a mesma chave
    sem_acento = unicodedata.normalize("NFKD", raca).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", sem_acento.lower())


_BREED_INDEX = {_normalize(nome): nome for nome in BREED_KNOWLEDGE}


def get_breed_info(raca: str) -> tuple[str, dict] | None:
    nome = _BREED_INDEX.get(_normalize(raca))
    return (nome, BREED_KNOWLEDGE[nome]) if nome else None


def get_breed_context(raca: str, peso: float) -> str:
    encontrada = get_breed_info(raca)
    if not encontrada:
        return "Raça não mapeada com alertas graves específicos de comportamento genético."
    nome, info = encontrada

    alerta_peso = ""
    if peso > info["peso_limite_alerta"]:
        alerta_peso = f" ATENÇÃO: O peso atual ({peso}kg) excede o limite preventivo sugerido de {info['peso_limite_alerta']}kg, gerando sobrecarga física crítica."

    return (
        f"Predisposições genéticas da raça {nome}: {', '.join(info['predisposicoes'])}.{alerta_peso} "
        f"Diretriz preventiva recomendada em artigos: {info['diretriz_cientifica']}"
    )
