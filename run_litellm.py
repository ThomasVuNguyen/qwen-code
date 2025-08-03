import subprocess
import sys
from datetime import datetime

# The model and port you want to use
MODEL = "gpt-4.1-mini"
PORT = 8000

# Generate a log file name with the model name, date, and time
LOG_FILE_NAME = f"{MODEL.replace('/', '_')}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

# The command to run
command = [
    "llm/myenv/bin/litellm",
    "--model",
    MODEL,
    "--port",
    str(PORT),
    "--detailed_debug",
]

# Open a file to log the output
with open(LOG_FILE_NAME, "w") as log_file:
    # Start the process
    process = subprocess.Popen(
        command,
        stdout=log_file,
        stderr=subprocess.STDOUT,
    )

    print(f"Starting LiteLLM server with model {MODEL} on port {PORT}...")
    print(f"Logging to {LOG_FILE_NAME}")
    print(f"Process ID: {process.pid}")

    try:
        # Wait for the process to complete
        process.wait()
    except KeyboardInterrupt:
        # Terminate the process if the user presses Ctrl+C
        print("\nTerminating LiteLLM server...")
        process.terminate()
        process.wait()
        print("Server terminated.")