# Lab 2.1: Pydantic Validators for Compliance

## Goal

Learn how to force your agents to output **structured, validated data** instead of free text. This is critical for a "Judge Agent" that needs to pass a boolean `pass/fail` signal to a router.

## Concepts

### 1. Pydantic `BaseModel`

Pydantic allows you to define data schemas as Python classes.

```python
class RiskAssessment(BaseModel):
    risk_level: str
    score: int
```

### 2. Field Descriptions

LLMs use the `Field(description="...")` to understand what each field means. This is essentially "prompt engineering via code".

### 3. Validators

You can write custom logic to validate the LLM's output *before* your program continues.

* *Example*: Ensure `score` is between 0 and 10.
* *Example*: Ensure `risk_level` is one of ["Low", "Medium", "High"].

### 4. Structured Output (OpenAI/LangChain)

Modern LLMs support "Function Calling" or "JSON Mode" to guarantee the output matches your Pydantic schema. LangChain's `.with_structured_output(Schema)` method handles this automatically.

## Instructions

1. **Open `lab_2_1_starter.py`**.
2. **Step 1**: Define the `ComplianceReport` Pydantic model. It needs fields for:
    * `policy_name` (str)
    * `compliant` (bool)
    * `confidence_score` (float, 0.0 to 1.0)
    * `missing_controls` (List[str])
3. **Step 2**: Add a `@field_validator` to ensure `confidence_score` is valid.
4. **Step 3**: Create the LLM chain using `.with_structured_output()`.
5. **Step 4**: Run the agent with a sample policy text and see if it generates valid JSON.

## Resources

* [Pydantic Documentation](https://docs.pydantic.dev/)
* [LangChain Structured Output](https://python.langchain.com/docs/modules/model_io/chat/structured_output/)
