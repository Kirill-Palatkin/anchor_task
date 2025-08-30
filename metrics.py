
from typing import Optional, Union, Dict

Number = Union[int, float]

def compute_metrics(impressions: Optional[Number], clicks: Optional[Number], cost: Optional[Number]) -> Dict[str, object]:
    """Рассчитывает CTR и CPC.

    Правила:
    - Если есть None, отрицательные значения, или возникает деление на ноль для любой метрики — статус "no_answer".
    - Метрики вычисляются по отдельности; если хотя бы одна из них не может быть вычислена, она будет None,
      а общий статус станет "no_answer". Иначе статус "ok".

    CTR = clicks / impressions        (если impressions > 0)
    CPC = cost / clicks               (если clicks > 0)
    """
    # Проверка на None
    if impressions is None or clicks is None or cost is None:
        return {"ctr": None, "cpc": None, "status": "no_answer"}

    # Попытка привести к float
    try:
        imp = float(impressions)
        clk = float(clicks)
        cst = float(cost)
    except (TypeError, ValueError):
        return {"ctr": None, "cpc": None, "status": "no_answer"}

    # Отрицательные значения не допускаются
    if imp < 0 or clk < 0 or cst < 0:
        return {"ctr": None, "cpc": None, "status": "no_answer"}

    insufficient = False

    # CTR
    if imp == 0:
        ctr = None
        insufficient = True
    else:
        ctr = clk / imp

    # CPC
    if clk == 0:
        cpc = None
        insufficient = True
    else:
        cpc = cst / clk

    status = "ok" if not insufficient else "no_answer"
    return {"ctr": ctr, "cpc": cpc, "status": status}

if __name__ == "__main__":
    # Пример запуска из консоли (необязательная секция)
    import os
    from llm import explain_metrics

    sample = compute_metrics(1000, 50, 25)
    print("metrics:", sample)
    print("explain:", explain_metrics(sample["ctr"], sample["cpc"], sample["status"], use_llm=os.getenv("USE_LLM") == "1"))
