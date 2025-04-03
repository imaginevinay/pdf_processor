from flask import Flask, request
import os
# from supabase import create_client

app = Flask(__name__)

# Load environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase
# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/process", methods=["POST"])
def process_pdf():
    file_id = request.json.get("fileId")
    print(f"Received PDF ID: {file_id}")
    
    # TODO: Add PDF processing here
    return {"status": "success", "file_id": file_id}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)