"""
WSN_Attack_Detector_N36.py

Modelo em Python equivalente ao arquivo GeNIe/XDSL ajustado para apenas uma topologia:
N36 = rede com 36 nós.

Este script usa pgmpy para representar a Rede Bayesiana:

TOPOLOGIA -> TIPO_DE_ATAQUE
TOPOLOGIA + TIPO_DE_ATAQUE -> PDR
TOPOLOGIA + TIPO_DE_ATAQUE -> DELAY
TOPOLOGIA + TIPO_DE_ATAQUE -> THROUGHPUT
TOPOLOGIA + TIPO_DE_ATAQUE -> ENERGIA

Instalação necessária:
    pip install pgmpy

Execução:
    python WSN_Attack_Detector_N36.py
"""

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def build_model():
    """
    Cria e retorna o modelo Bayesiano para a topologia N36.
    """

    model = DiscreteBayesianNetwork([
        ("TOPOLOGIA", "TIPO_DE_ATAQUE"),
        ("TOPOLOGIA", "PDR"),
        ("TIPO_DE_ATAQUE", "PDR"),
        ("TOPOLOGIA", "DELAY"),
        ("TIPO_DE_ATAQUE", "DELAY"),
        ("TOPOLOGIA", "THROUGHPUT"),
        ("TIPO_DE_ATAQUE", "THROUGHPUT"),
        ("TOPOLOGIA", "ENERGIA"),
        ("TIPO_DE_ATAQUE", "ENERGIA"),
    ])

    # Estados
    topologia_states = ["N36"]

    ataque_states = [
        "Backoff",
        "Blackhole",
        "Flooding",
        "Normal",
        "Wormhole",
    ]

    metric_states = ["Low", "Medium", "High"]

    # CPT da topologia: agora existe apenas N36.
    cpd_topologia = TabularCPD(
        variable="TOPOLOGIA",
        variable_card=1,
        values=[[1.0]],
        state_names={"TOPOLOGIA": topologia_states},
    )

    # CPT do tipo de ataque condicionado à topologia.
    # Como só existe N36, temos uma coluna.
    cpd_tipo_ataque = TabularCPD(
        variable="TIPO_DE_ATAQUE",
        variable_card=5,
        values=[
            [0.2],  # Backoff
            [0.2],  # Blackhole
            [0.2],  # Flooding
            [0.2],  # Normal
            [0.2],  # Wormhole
        ],
        evidence=["TOPOLOGIA"],
        evidence_card=[1],
        state_names={
            "TOPOLOGIA": topologia_states,
            "TIPO_DE_ATAQUE": ataque_states,
        },
    )

    # A ordem das colunas nas CPTs abaixo é:
    # TOPOLOGIA=N36 e TIPO_DE_ATAQUE =
    # Backoff, Blackhole, Flooding, Normal, Wormhole

    # PDR original para N36:
    # Backoff   -> 0.076923 0.461538 0.461538
    # Blackhole -> 0.692308 0.230769 0.076923
    # Flooding  -> 0.384615 0.307692 0.307692
    # Normal    -> 0.076923 0.076923 0.846154
    # Wormhole  -> 0.615385 0.307692 0.076923
    cpd_pdr = TabularCPD(
        variable="PDR",
        variable_card=3,
        values=[
            [0.076923, 0.692308, 0.384615, 0.076923, 0.615385],  # Low
            [0.461538, 0.230769, 0.307692, 0.076923, 0.307692],  # Medium
            [0.461538, 0.076923, 0.307692, 0.846154, 0.076923],  # High
        ],
        evidence=["TOPOLOGIA", "TIPO_DE_ATAQUE"],
        evidence_card=[1, 5],
        state_names={
            "TOPOLOGIA": topologia_states,
            "TIPO_DE_ATAQUE": ataque_states,
            "PDR": metric_states,
        },
    )

    # DELAY original para N36:
    # Backoff   -> 0.153846 0.384615 0.461538
    # Blackhole -> 0.461538 0.307692 0.230769
    # Flooding  -> 0.076923 0.230769 0.692308
    # Normal    -> 0.538462 0.384615 0.076923
    # Wormhole  -> 0.615385 0.307692 0.076923
    cpd_delay = TabularCPD(
        variable="DELAY",
        variable_card=3,
        values=[
            [0.153846, 0.461538, 0.076923, 0.538462, 0.615385],  # Low
            [0.384615, 0.307692, 0.230769, 0.384615, 0.307692],  # Medium
            [0.461538, 0.230769, 0.692308, 0.076923, 0.076923],  # High
        ],
        evidence=["TOPOLOGIA", "TIPO_DE_ATAQUE"],
        evidence_card=[1, 5],
        state_names={
            "TOPOLOGIA": topologia_states,
            "TIPO_DE_ATAQUE": ataque_states,
            "DELAY": metric_states,
        },
    )

    # THROUGHPUT original para N36:
    # Backoff   -> 0.538462 0.307692 0.153846
    # Blackhole -> 0.538462 0.307692 0.153846
    # Flooding  -> 0.692308 0.076923 0.230769
    # Normal    -> 0.076923 0.230769 0.692308
    # Wormhole  -> 0.307692 0.230769 0.461538
    cpd_throughput = TabularCPD(
        variable="THROUGHPUT",
        variable_card=3,
        values=[
            [0.538462, 0.538462, 0.692308, 0.076923, 0.307692],  # Low
            [0.307692, 0.307692, 0.076923, 0.230769, 0.230769],  # Medium
            [0.153846, 0.153846, 0.230769, 0.692308, 0.461538],  # High
        ],
        evidence=["TOPOLOGIA", "TIPO_DE_ATAQUE"],
        evidence_card=[1, 5],
        state_names={
            "TOPOLOGIA": topologia_states,
            "TIPO_DE_ATAQUE": ataque_states,
            "THROUGHPUT": metric_states,
        },
    )

    # ENERGIA original para N36:
    # Backoff   -> 0.384615 0.230769 0.384615
    # Blackhole -> 0.230769 0.615385 0.153846
    # Flooding  -> 0.307692 0.153846 0.538462
    # Normal    -> 0.692308 0.230769 0.076923
    # Wormhole  -> 0.307692 0.461538 0.230769
    cpd_energia = TabularCPD(
        variable="ENERGIA",
        variable_card=3,
        values=[
            [0.384615, 0.230769, 0.307692, 0.692308, 0.307692],  # Low
            [0.230769, 0.615385, 0.153846, 0.230769, 0.461538],  # Medium
            [0.384615, 0.153846, 0.538462, 0.076923, 0.230769],  # High
        ],
        evidence=["TOPOLOGIA", "TIPO_DE_ATAQUE"],
        evidence_card=[1, 5],
        state_names={
            "TOPOLOGIA": topologia_states,
            "TIPO_DE_ATAQUE": ataque_states,
            "ENERGIA": metric_states,
        },
    )

    model.add_cpds(
        cpd_topologia,
        cpd_tipo_ataque,
        cpd_pdr,
        cpd_delay,
        cpd_throughput,
        cpd_energia,
    )

    model.check_model()
    return model


def infer_attack(model, evidence):
    """
    Realiza inferência para estimar o tipo de ataque.

    Exemplo de evidence:
        {
            "PDR": "Low",
            "DELAY": "High",
            "THROUGHPUT": "Low",
            "ENERGIA": "High"
        }
    """

    inference = VariableElimination(model)

    result = inference.query(
        variables=["TIPO_DE_ATAQUE"],
        evidence={
            "TOPOLOGIA": "N36",
            **evidence,
        },
    )

    return result


if __name__ == "__main__":
    model = build_model()

    print("\nModelo criado com sucesso!")
    print("Nós do modelo:", model.nodes())
    print("Arestas do modelo:", model.edges())

    # Exemplo 1: cenário típico de ataque Flooding
    evidence_flooding = {
        "PDR": "Low",
        "DELAY": "High",
        "THROUGHPUT": "Low",
        "ENERGIA": "High",
    }

    print("\nInferência com evidências típicas de Flooding:")
    print(evidence_flooding)
    print(infer_attack(model, evidence_flooding))

    # Exemplo 2: cenário típico normal
    evidence_normal = {
        "PDR": "High",
        "DELAY": "Low",
        "THROUGHPUT": "High",
        "ENERGIA": "Low",
    }

    print("\nInferência com evidências típicas de cenário Normal:")
    print(evidence_normal)
    print(infer_attack(model, evidence_normal))
