import os
from typing import List, Dict, Any, Optional

class MultiAgentOrchestratorClient:
    """
    Client SDK for classifying task payloads and routing execution targets to specialty agent sub-nodes.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ORCHESTRATOR_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def dispatch_task(self, task: str, registry: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Classifies incoming tasks and routes them to matched agents.
        """
        task_lower = task.lower()
        selected_agent = "fallback_agent"
        reason = "No matching specialty found in agent registry. Routed to general fallback agent."
        confidence = 0.5

        # Heuristic matching
        for agent in registry:
            spec = agent["specialty"].lower()
            # If specialty keywords appear in task string
            words = spec.split()
            matches = sum(1 for w in words if w in task_lower)
            if matches > 0:
                selected_agent = agent["agent_id"]
                reason = f"Routed due to high overlap with agent specialty: '{agent['specialty']}'."
                confidence = 0.9
                break

        return {
            "dispatch_route": {
                "target_agent_id": selected_agent,
                "confidence": confidence,
                "routing_reason": reason
            }
        }
