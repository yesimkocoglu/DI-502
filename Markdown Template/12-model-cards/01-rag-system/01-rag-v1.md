# RAG v1

This template is created according to Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., ... & Gebru, T. (2019, January). Model cards for model reporting. In Proceedings of the conference on fairness, accountability, and transparency (pp. 220-229).

The template is modified to have relevant fields applicable to RAG systems

You can access the paper here:

Model Cards for Model Reporting

The model card can be updated during the experiments. When you are done with all the experiments related to the model, it should be finalized accordingly.

| Data Updated: |  |
|---|---|
| Last Updated by: |   |
| Team Name: |   |
| Team Members: |   |

- LLM Details
- Intended Use
- Embedder Details
- Intended Use
- Factors
- Metrics
- Evaluation Set
- Quantitative Analyses
- Ethical Considerations
- Caveats and Recommendations

## LLM Details

Basic information about the responding LLM.

| Person or organization developing the model: |  |
|---|---|
| Release date: |   |
| Version: |   |
| Model type: |   |
| Information about training algorithms, parameters, fairness constraints or other applied approaches, and features: |   |
| Paper or another resource for more information: |   |
| Citation details: |   |
| License: |   |
| Where to send questions or comments about the model: |   |

## Intended Use

Use cases that were envisioned during development.

| Primary intended uses: |  |
|---|---|
| Primary intended users: |   |
| Out-of-scope use cases: |   |

## Embedder Details

Basic information about the embedding model.

| Person or organization developing the model: |  |
|---|---|
| Release date: |   |
| Version: |   |
| Model type: |   |
| Information about training algorithms, parameters, fairness constraints or other applied approaches, and features: |   |
| Paper or another resource for more information: |   |
| Citation details: |   |
| License: |   |
| Where to send questions or comments about the model: |   |

## Intended Use

Use cases that were envisioned during development.

| Primary intended uses: |  |
|---|---|
| Primary intended users: |   |
| Out-of-scope use cases: |   |

## Factors

Factors could include demographic or phenotypic groups, environmental conditions, and technical attributes.

While filling out this card don't forget to consider Groups, Instrumentation, and Environment. See the paper for details.

| Relevant Factors: What are foreseeable salient factors for which RAG performance may vary, and how were these determined? |  |
|---|---|
| Evaluation Factors: Which factors are being reported, and why were these chosen? If the relevant factors and evaluation factors are different, why? |   |

## Metrics

Metrics should be chosen to reflect the potential real-world impacts of the model

| RAG Performance Measures: |  |
|---|---|
| Decision Thresholds: |   |
| Approaches to uncertainty and variability: |   |

## Evaluation Set

Details on the question-answer pairs used for the quantitative analyses in the card.

| Datasets: What datasets were used to evaluate the model? |  |
|---|---|
| Motivation: Why were these datasets chosen? |   |
| Generation: How was the data generated for evaluation? |   |
| Postprocessing: Were the question-answer pairs post processed? How was it done? |   |

## Quantitative Analyses

Quantitative analyses should be disaggregated, that is, broken down by the chosen factors. Quantitative analyses should provide the results of evaluating the model according to the chosen metrics, providing confidence interval values when possible

| Unitary Results: How did the RAG system perform concerning each factor? |  |
|---|---|
| Intersectional Results: How did the model perform concerning the intersection of evaluated factors? |   |

## Ethical Considerations

This section is intended to demonstrate the ethical considerations that went into model development, surfacing ethical challenges and solutions to stakeholders.

| Data: Does the model use any sensitive data (e.g. court documents)? |  |
|---|---|
| Human life: Is the RAG system intended to inform decisions about matters central to human life or flourishing – e.g., health or safety? Or could it be used in such a way? |   |
| Mitigations: What risk mitigation strategies were used during model development? |   |
| Risks and harms: What risks may be present in RAG usage? Try to identify the potential recipients, likelihood, and magnitude of harm. If these cannot be determined, note that they were considered but remain unknown. |   |
| Use cases: Are there any known model use cases that are especially fraught? |   |

## Caveats and Recommendations

This section should list additional concerns that were not covered in the previous sections.

| Did the results suggest any further testing? |  |
|---|---|
| Were there any relevant groups that were not represented in the evaluation set? |   |
| Are there additional recommendations for model use? |   |

## Subpages

- [Experiment 4](01-rag-v1/01-experiment-4.md)
- [Experiment 3](01-rag-v1/02-experiment-3.md)
