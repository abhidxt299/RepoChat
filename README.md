# 🌊 Project Drift: Real-Time ML Stock Predictor

An end-to-end Machine Learning Engineering system designed to ingest real-time market data, engineer technical features on-the-fly, and predict price movements using Deep Learning.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[Upstox/INDstocks WebSocket] -->|Raw Ticks| B(Ingestion Layer)
    B -->|Validation| C{Data Integrity Check}
    C -->|Pass| D[Feature Engineer]
    C -->|Fail| E[Logger / Alert]
    D -->|Rolling Windows| F[LSTM Inference Engine]
    F -->|Signal| G[Mock Portfolio/Dashboard]