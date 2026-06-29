import sys
import json
from orchestrator import MultiAgentOrchestratorClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Multi-Agent System Orchestrator Example ===")
    client = MultiAgentOrchestratorClient()
    
    registry = [
        {"agent_id": "billing_agent", "specialty": "handles payment failures refunds billing issues"},
        {"agent_id": "tech_support_agent", "specialty": "diagnoses system errors code compile exceptions api issues"}
    ]
    
    task = "My payment failed and I was double charged. Can you refund me?"
    
    result = client.dispatch_task(task, registry)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
