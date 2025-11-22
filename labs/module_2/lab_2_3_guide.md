# Lab 2.3: Financial Data Ingestion (ROI Agent)

## Goal

Build an **ROI Agent** that can ingest structured financial data (JSON) and combine it with risk scores to calculate a **Risk-Adjusted Return**. This teaches you how to handle "Business Logic" within an agentic system.

## Concepts

### 1. Structured Data Ingestion

Agents often need to read CSVs, JSONs, or Database rows. We use **Pandas** or standard Python libraries to load this data into a format the LLM (or code) can process.

### 2. Deterministic vs. Probabilistic

* **LLM (Probabilistic)**: "Summarize this report."
* **Code (Deterministic)**: "Calculate (Revenue - Cost) / Cost."
* **Hybrid**: The agent uses code tools to perform the math, ensuring accuracy.

### 3. Risk-Adjusted Return on Capital (RAROC) - Simplified

We will use a simplified formula:
$$ \text{Adjusted ROI} = \text{Projected ROI} \times (1 - \text{Risk Score}) $$

* If Risk Score is 0.0 (No Risk), Adjusted ROI = Projected ROI.
* If Risk Score is 1.0 (Max Risk), Adjusted ROI = 0.

## Instructions

1. **Open `lab_2_3_starter.py`**.
2. **Step 1**: Define a `FinancialReport` Pydantic model.
3. **Step 2**: Implement `calculate_adjusted_roi(roi, risk_score)`.
4. **Step 3**: Create an agent that takes a JSON string of financial data and a risk score, and outputs a recommendation ("Approve" or "Reject") based on a threshold.

## Resources

* [Pandas Documentation](https://pandas.pydata.org/)
