# Anchor: базовые KPI (CTR/CPC)

В репозитории реализована функция `compute_metrics(impressions, clicks, cost) -> {"ctr": float|None, "cpc": float|None, "status": "ok"|"no_answer"}` с обработкой краёв (None/нули/деление на ноль/отрицательные значения → `status="no_answer"`). 

Метрики считаются независимо: если одна не вычисляется, она становится `None`, а общий `status` — `no_answer`; при успехе обеих — `ok`. 

Для пояснения есть переключатель LLM: `USE_LLM=1` — класс `StubLLM` выдаёт одно предложение, `USE_LLM=0` — детерминированный шаблон `CTR=X%, CPC=Y; данных достаточно/недостаточно`. 

Артефакты: `metrics.py`, `llm.py`, `test_metrics.py`, `requirements.txt`, `.env.example`. 

Запуск тестов:

# Создать виртуальное окружение
python -m venv .venv

# Активировать виртуальное окружение
source .venv/bin/activate (.venv\Scripts\activate)

# Установить зависимости
pip install -r requirements.txt

# Запустить тесты
pytest -q
