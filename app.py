from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

# HTML Template for Adil Bajwa AI Frontend
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adil Bajwa AI - Studio</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; margin: 0; }
        .container { max-width: 600px; margin: auto; background: #1e293b; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
        h1 { text-align: center; color: #38bdf8; }
        textarea { width: 100%; height: 100px; background: #0f172a; color: white; border: 1px solid #475569; border-radius: 8px; padding: 10px; margin-bottom: 10px; resize: none; }
        button { width: 100%; background: #38bdf8; color: #0f172a; border: none; padding: 12px; font-weight: bold; border-radius: 8px; cursor: pointer; }
        button:hover { background: #0ea5e9; }
        .output { margin-top: 20px; background: #0f172a; padding: 15px; border-radius: 8px; border-left: 4px solid #38bdf8; white-space: pre-wrap; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Adil Bajwa AI 🚀</h1>
        <p>Apna idea dein (e.g., Cartoon, Drama, Story), Adil Bajwa AI usay scenes mein divide karega!</p>
        <textarea id="userPrompt" placeholder="Yahan apni story ya video ka idea likhein..."></textarea>
        <button onclick="generateScript()">Generate AI Script & Scenes</button>
        <div class="output" id="outputBox">Result yahan show hoga...</div>
    </div>

    <script>
        async function generateScript() {
            const prompt = document.getElementById('userPrompt').value;
            const outputBox = document.getElementById('outputBox');
            if(!prompt) { alert('Pehle kuch likhein!'); return; }
            
            outputBox.innerText = "Adil Bajwa AI is processing your request...";
            
            const response = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: prompt })
            });
            const data = await response.json();
            outputBox.innerText = data.result;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_idea = data.get('prompt', '')
    
    # Yahan hum AI logic ya prompt splitter build kar rahe hain
    # Filhal hum ek smart breakdown simulate kar rahe hain jo baad mein AI model se connect hoga
    simulated_result = f"[Adil Bajwa AI Pipeline]\n\n" \
                       f"Original Idea: {user_idea}\n\n" \
                       f"Scene 1 (Character Setup): Cinematic opening shot, consistent face model active.\n" \
                       f"Scene 2 (Main Plot): Story progression with same character and voice lock.\n" \
                       f"Scene 3 (Climax & Ending): Final high-resolution render queued."
                       
    return jsonify({'result': simulated_result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    