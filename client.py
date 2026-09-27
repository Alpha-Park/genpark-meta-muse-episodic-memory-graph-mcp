import sys, json, math, time

class MetaMuseEpisodicMemoryGraph:
    """
    Meta Muse Continuous Episodic Memory & Multimodal Knowledge Graph.
    Implements Ebbinghaus forgetting curves, contradiction detection,
    and recency-decayed personal briefing synthesis.
    """
    def __init__(self, half_life_days=7.0):
        self.half_life_seconds = half_life_days * 86400.0
        self.episodes = []
        self.preference_graph = {}

    def record_episodic_memory(self, event_type, content, modality="text", confidence=0.9):
        now = time.time()
        ep_id = f"ep_{len(self.episodes) + 1}_{int(now)}"
        episode = {
            "episode_id": ep_id,
            "timestamp": now,
            "event_type": event_type,
            "content": content,
            "modality": modality,
            "initial_confidence": confidence
        }
        self.episodes.append(episode)
        
        # Update preference graph if preference statement
        if event_type == "user_preference":
            attr = content.get("attribute", "general")
            self.preference_graph[attr] = {
                "value": content.get("value"),
                "updated_at": now,
                "episode_id": ep_id
            }

        return episode

    def query_decayed_memory(self, current_time=None, min_retention=0.2):
        now = current_time or time.time()
        decayed_episodes = []

        for ep in self.episodes:
            dt = max(0, now - ep["timestamp"])
            # Ebbinghaus exponential decay: R = exp(-dt / S)
            retention = math.exp(-dt / max(1.0, self.half_life_seconds))
            effective_weight = round(ep["initial_confidence"] * retention, 4)
            
            if effective_weight >= min_retention:
                decayed_episodes.append({
                    "episode_id": ep["episode_id"],
                    "event_type": ep["event_type"],
                    "content": ep["content"],
                    "retention_probability": round(retention, 4),
                    "effective_weight": effective_weight,
                    "age_hours": round(dt / 3600.0, 2)
                })

        # Sort by effective weight descending
        decayed_episodes.sort(key=lambda x: x["effective_weight"], reverse=True)
        return {
            "total_stored_episodes": len(self.episodes),
            "active_retained_episodes": len(decayed_episodes),
            "decayed_episodes": decayed_episodes
        }

    def resolve_preference_contradiction(self, new_preference, existing_attribute):
        existing = self.preference_graph.get(existing_attribute)
        if not existing:
            return {"has_conflict": False, "status": "NEW_PREFERENCE_STORED"}

        old_val = existing["value"]
        new_val = new_preference.get("value")

        if old_val == new_val:
            return {"has_conflict": False, "status": "CONFIRMED_IDENTICAL"}

        # Contradiction: Explicit current user intent ALWAYS supersedes historical memory
        resolution = {
            "has_conflict": True,
            "conflict_type": "VALUE_MUTATION",
            "historical_value": old_val,
            "superseding_value": new_val,
            "policy": "CURRENT_EXPLICIT_INTENT_SUPERSEDES_PAST_HABIT",
            "superseded_episode_id": existing["episode_id"],
            "resolution_status": "GRAPH_UPDATED_PRESERVING_AUDIT_LOG"
        }
        self.preference_graph[existing_attribute] = {
            "value": new_val,
            "updated_at": time.time(),
            "superseded": old_val
        }
        return resolution

    def run_benchmark_episodic_stream(self):
        # 1. Ingest historical episodes
        past_time = time.time() - (5 * 86400) # 5 days ago
        self.episodes.append({
            "episode_id": "ep_old_1",
            "timestamp": past_time,
            "event_type": "user_preference",
            "content": {"attribute": "delivery_speed", "value": "economy_shipping"},
            "modality": "text",
            "initial_confidence": 0.85
        })
        self.preference_graph["delivery_speed"] = {"value": "economy_shipping", "updated_at": past_time, "episode_id": "ep_old_1"}

        # 2. Ingest recent multimodal vision episode
        self.record_episodic_memory(
            event_type="multimodal_vision_anchor",
            content={"detected_object": "Sony WH-1000XM5", "bounding_box": [120, 45, 450, 380]},
            modality="ambient_camera",
            confidence=0.95
        )

        # 3. Test contradiction
        conflict = self.resolve_preference_contradiction(
            {"attribute": "delivery_speed", "value": "same_day_delivery"},
            "delivery_speed"
        )

        # 4. Decayed query
        decayed = self.query_decayed_memory()

        return {
            "benchmark": "Meta Muse Episodic Memory Suite",
            "contradiction_audit": conflict,
            "active_retention": decayed,
            "preference_graph_state": self.preference_graph
        }
