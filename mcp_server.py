import sys, json
from client import MetaMuseEpisodicMemoryGraph

def handle_mcp():
    graph = MetaMuseEpisodicMemoryGraph()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(graph.run_benchmark_episodic_stream(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            
            if method == "initialize":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "genpark-meta-muse-episodic-memory-graph-mcp", "version": "1.0.0"},
                    "capabilities": {"tools": {}}
                }}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [
                    {"name": "record_episodic_memory", "description": "Ingest continuous interaction episode.", "inputSchema": {"type": "object", "properties": {"event_type": {"type": "string"}, "content": {"type": "object"}}}},
                    {"name": "query_decayed_memory", "description": "Retrieve personal memories weighted by Ebbinghaus retention.", "inputSchema": {"type": "object"}},
                    {"name": "resolve_preference_contradiction", "description": "Arbitrate between historical habits and current intent.", "inputSchema": {"type": "object", "properties": {"new_preference": {"type": "object"}, "existing_attribute": {"type": "string"}}}},
                    {"name": "run_benchmark_episodic_stream", "description": "Run memory retention benchmark.", "inputSchema": {"type": "object"}}
                ]}}
            elif method == "tools/call":
                tname = req.get("params", {}).get("name")
                args = req.get("params", {}).get("arguments", {})
                if tname == "record_episodic_memory":
                    res = graph.record_episodic_memory(args.get("event_type", "note"), args.get("content", {}), args.get("modality", "text"))
                elif tname == "query_decayed_memory":
                    res = graph.query_decayed_memory()
                elif tname == "resolve_preference_contradiction":
                    res = graph.resolve_preference_contradiction(args.get("new_preference", {}), args.get("existing_attribute", ""))
                else:
                    res = graph.run_benchmark_episodic_stream()
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            
            sys.stdout.write(json.dumps(resp) + "
")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "
")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_mcp()
