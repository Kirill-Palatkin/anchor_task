
import os
from typing import Optional

def _fmt_pct(x: Optional[float]) -> str:
    if x is None:
        return "—"
    return f"{x*100:.2f}%"

def _fmt_money(x: Optional[float]) -> str:
    if x is None:
        return "—"
    return f"{x:.2f}"

class StubLLM:
    """Заглушка LLM. Возвращает короткое объяснение одной строкой."""
    def __init__(self, model_name: str = "stub") -> None:
        self.model_name = model_name

    def generate(self, ctr: Optional[float], cpc: Optional[float], status: str) -> str:
        if status != "ok" or ctr is None or cpc is None:
            return "Данных недостаточно для интерпретации CTR и CPC: соберите больше показов и/или кликов."
        return (
            f"CTR показывает долю кликов ({ctr*100:.2f}%), а CPC — среднюю стоимость клика ({cpc:.2f}); "
            f"вместе эти метрики характеризуют эффективность и стоимость трафика."
        )

def explain_metrics(ctr: Optional[float], cpc: Optional[float], status: str, use_llm: Optional[bool] = None, model_name: Optional[str] = None) -> str:
    """Возвращает короткое пояснение к метрикам.

    USE_LLM=1  -> одно предложение от StubLLM;
    USE_LLM=0  -> детерминированный шаблон "CTR=X%, CPC=Y; данных достаточно/недостаточно".
    """
    if use_llm is None:
        use_llm = os.getenv("USE_LLM", "0") == "1"
    if model_name is None:
        model_name = os.getenv("MODEL_NAME", "stub")

    if use_llm:
        return StubLLM(model_name=model_name).generate(ctr, cpc, status)
    else:
        suff = "достаточно" if status == "ok" else "недостаточно"
        return f"CTR={_fmt_pct(ctr)}, CPC={_fmt_money(cpc)}; данных {suff}."
