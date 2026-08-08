FROM python:3.13-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-quantum.txt .
RUN pip install --user --no-cache-dir -r requirements-quantum.txt

COPY . .
RUN pip install --user --no-cache-dir .

FROM python:3.13-slim AS runner

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app
COPY --from=builder /build/src ./src
COPY --from=builder /build/*.txt ./
COPY --from=builder /build/*.py ./

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

ENV PYTHONPATH=/app:$PYTHONPATH
ENV QUANTUM_ENABLED=true
ENV PQC_ENABLED=true

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD python -c "import sys; sys.path.insert(0, '/app/src'); from quantum.circuits.risk_circuit import RiskScoringCircuit; print('healthy')" || exit 1

LABEL org.opencontainers.image.source="https://github.com/quantumworld-dpdns-io/adult-creator-deplatforming-insurance"
LABEL org.opencontainers.image.description="Adult creator deplatforming insurance with quantum computing and PQC"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
