import bpy
import base64
import json
import tempfile
import websocket


from .protocol import Auth, PromptData, TaskStatus, TaskUpdate


def request_model(prompt: str) -> None | str:
    url = bpy.context.preferences.addons[__name__.partition(".")[0]].preferences.url
    api_key = bpy.context.preferences.addons[__name__.partition(".")[0]].preferences.token
    filepath = None

    def on_message(ws, message):
        nonlocal filepath
        update = TaskUpdate(**json.loads(message))
        if update.status == TaskStatus.STARTED:
            print("Task started")
        elif update.status == TaskStatus.FIRST_RESULTS:
            score = update.results.score if update.results else None
            assets = update.results.assets or "" if update.results else ""
            print(f"First results. Score: {score}. Size: {len(assets)}")
        elif update.status == TaskStatus.BEST_RESULTS:
            score = update.results.score if update.results else None
            assets = update.results.assets or "" if update.results else ""
            print(f"Best results. Score: {score}. Size: {len(assets)}")
            print(f"Stats: {update.statistics}")

            if assets:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".ply") as temp_file:
                    temp_file.write(base64.b64decode(assets.encode("utf-8")))
                    filepath = temp_file.name
                    ws.close()

    def on_error(ws, error):
        print(f"WebSocket connection error: {error}")

    def on_close(ws, close_status_code, close_msg):
        print("WebSocket connection closed")

    def on_open(ws):
        auth_data = Auth(api_key=api_key).dict()
        prompt_data = PromptData(prompt=prompt, send_first_results=True).dict()
        ws.send(json.dumps(auth_data))
        ws.send(json.dumps(prompt_data))

    # Initialize WebSocket connection
    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

    return filepath
