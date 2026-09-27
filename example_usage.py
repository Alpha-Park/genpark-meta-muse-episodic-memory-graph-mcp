from client import MetaMuseEpisodicMemoryGraph
import json

def test_memory():
    graph = MetaMuseEpisodicMemoryGraph()
    print("=== Testing Meta Muse Episodic Memory Graph MCP ===")
    
    bench = graph.run_benchmark_episodic_stream()
    print(json.dumps(bench, indent=2))

if __name__ == "__main__":
    test_memory()
