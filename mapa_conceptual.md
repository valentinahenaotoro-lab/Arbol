```mermaid
graph TD
    A[Aprendizaje de Árboles de Decisión] --> B(Componentes Principales)
    A --> C(Conceptos Teóricos)
    A --> D(Extracción de Reglas)

    B --> B1[Nodo Raíz<br>Atributo más importante]
    B --> B2[Nodos de Decisión<br>Evaluación de variables]
    B --> B3[Nodos Hoja<br>Resultado final / Clasificación]

    C --> C1[Entropía<br>Mide el desorden de los datos]
    C --> C2[Ganancia de Información<br>Define qué variable divide mejor]

    D --> D1[Sentencias Lógicas<br>Si... Entonces...]

    style A fill:#2b6cb0,stroke:#2b6cb0,stroke-width:2px,color:#fff
    style B fill:#4299e1,stroke:#4299e1,stroke-width:2px,color:#fff
    style C fill:#4299e1,stroke:#4299e1,stroke-width:2px,color:#fff
    style D fill:#4299e1,stroke:#4299e1,stroke-width:2px,color:#fff
