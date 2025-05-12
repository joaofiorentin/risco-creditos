# 🧠 Predição de Risco de Crédito com Dados Sintéticos

Este projeto apresenta um pipeline completo de Ciência de Dados aplicado à predição de risco de crédito, utilizando dados sintéticos gerados com a biblioteca `Faker`. O objetivo é treinar e avaliar modelos de machine learning capazes de prever inadimplência de clientes, simulando um cenário real de tomada de decisão em crédito.

---

## 📊 Visão Geral

- Geração de base de dados fictícia com características demográficas e financeiras.
- Análise exploratória para compreensão das variáveis.
- Pré-processamento com padronização e balanceamento via SMOTE.
- Modelagem supervisionada com:
  - Regressão Logística
  - Random Forest
- Avaliação com métricas robustas: AUC ROC, Matriz de Confusão e Classification Report.

---

## 🧱 Tecnologias Utilizadas

- **Python 3**
- Bibliotecas:
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `sklearn` (Scikit-learn)
  - `imbalanced-learn` (SMOTE)
  - `faker`

---

## ⚙️ Estrutura do Pipeline

```bash
📁 projeto-preditivo-credito/
├── README.md
├── notebook.ipynb
├── requirements.txt
└── src/
    └── gerar_dados.py
