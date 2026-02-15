import requests

def send_update(state: int, label: str, output: str, server_url: str = "http://localhost:8000/notify"):
    """Send a JSON notification to the FastAPI notify endpoint.

    Example:
        send_update(2, 'Planning', 'Created plan.md')
    """
    payload = {"state": state, "label": label, "output": output}
    try:
        resp = requests.post(server_url, json=payload, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"status": "error", "reason": str(e)}
