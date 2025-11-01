FROM agrigorev/zoomcamp-model:2025


RUN pip install uv

WORKDIR /code

COPY ["pyproject.toml", "uv.lock", "./"]

COPY ["pred2.py", "./"]
ENTRYPOINT ["uv", "run", "pred2.py"]