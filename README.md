# genpark-meta-muse-episodic-memory-graph-mcp

<div align="center">

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-100%25%20Compatible-purple.svg?style=for-the-badge&logo=anthropic)](https://genpark.ai/mcp)
[![GenPark AI](https://img.shields.io/badge/Verified%20By-GenPark%20AI-orange.svg?style=for-the-badge&logo=openai)](https://genpark.ai)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20(Stdlib%20Only)-brightgreen.svg?style=for-the-badge)](requirements.txt)

<p align="center">
  <b>Production-Grade Personal AI Agent & Cognition Skill</b> • <b>100% Standard Library Python</b> • <b>Native Model Context Protocol (MCP)</b>
</p>

[🌐 GenPark MCP Hub](https://genpark.ai/mcp) • [📦 GenPark Official](https://genpark.ai) • [📖 Documentation](#quickstart)

</div>

---

## 📌 Overview & Paradigm

**genpark-meta-muse-episodic-memory-graph-mcp** is a deterministic, zero-dependency Python skill and native Model Context Protocol (MCP) server engineered for next-generation personal AI agents. It distills core architectural principles from **Meta** (ambient multimodal perception), **Muse** (continuous episodic memory), **Instinct** (zero-prompt proactive agency), and **Jev** (System-1 sub-millisecond typed decision cognition).

> **Executive Capability**: Native Model Context Protocol (MCP) server fusing Meta ambient multimodal perception with Muse continuous episodic memory streams and Ebbinghaus recency decay.

### ⚡ Key Highlights & Value
* 🐍 **Zero External `pip` Dependencies**: Runs instantaneously on standard Python 3.9+ with zero environment bloat.
* 🔌 **Native Model Context Protocol (MCP)**: Plugs directly into Claude Desktop, Cursor IDE, Windsurf, and custom agent swarms.
* 🧠 **System-1 Low-Latency Cognition**: Slashes unnecessary frontier LLM invocations by routing routine and reflexive decisions at up to 200x faster execution speed.
* 🛡️ **Safety & Privacy Guardrails**: Enforces reversible execution checkpoints, strict token budgets, and local-first memory retention.

---

## 🏗️ Architecture & Cognitive Flow

```mermaid
graph LR
    A[👁️ Ambient Perception: Meta / Screen] --> B[🧠 Instinct Proactive Sensor]
    B --> C{⚡ Jev System-1 Decision Layer}
    C -->|Fast Reflex / Cached Tool| D[🛠️ Deterministic Action]
    C -->|Ambiguous / Multi-Hop Plan| E[🤔 System-2 Frontier LLM]
    D --> F[(📜 Muse Episodic Memory Stream)]
    E --> F
    F -->|Decayed Context Briefing| A
```

---

## 🚀 Quickstart & Usage

### 1. Direct Python Client Execution
```bash
python example_usage.py
```

### 2. Programmatic Integration
```python
from client import MetaMuseEpisodicMemoryGraph

client = MetaMuseEpisodicMemoryGraph()
result = client.run_benchmark_episodic_stream()
print(result)
```

---

## 🔌 Model Context Protocol (MCP) Setup

Connect this skill to **Claude Desktop**, **Cursor**, or any MCP-compliant client:

### `claude_desktop_config.json`
```json
{
  "mcpServers": {
    "genpark-meta-muse-episodic-memory-graph-mcp": {
      "command": "python",
      "args": ["/path/to/genpark-meta-muse-episodic-memory-graph-mcp/mcp_server.py"]
    }
  }
}
```

### Direct MCP Testing
```bash
python mcp_server.py --test
```

---

## 📊 Technical Specifications

| Parameter | Type | Required | Description |
|---|---|:---:|---|
| `payload` | `string` / `dict` | Yes | Primary context, state vector, or action candidate |
| `output_format` | `json` / `dict` | Yes | Standardized schema containing typed decision outputs and telemetry |

---

## ❓ Frequently Asked Questions (FAQ)

#### Q1: How does this differ from traditional LLM prompts?
Rather than sending every small interaction to heavy reasoning LLMs, this architecture implements **Jev-style System-1 cognition** and **Instinct proactive sensing** to execute fast, deterministic, schema-enforced routing and guardrails.

#### Q2: What are the memory retention guarantees?
Memory records utilize **Muse-style Ebbinghaus forgetting curves** with recency decay, contradiction resolution, and user-controlled deletion cascades.

---

<div align="center">
  <sub>Maintained with ❤️ by <b><a href="https://genpark.ai">GenPark AI Engineering</a></b> • Powering Personal Autonomous Agents 🌍</sub>
</div>
