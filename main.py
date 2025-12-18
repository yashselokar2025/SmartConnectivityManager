from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():
    return {"message": "Backend running"}

# Network Check Route → Must match frontend fetch url: /check-network
@app.get("/check-network")
def check_network():
    # Temporary dummy response (Later we will connect real network checking code)
    return {"network_status": "Connected"}   # Frontend expects network_status key

# Auto Recharge Route
@app.get("/auto-recharge")
def recharge_now():
    # Temporary response (Later add real recharge script)
    return {"status": "Recharge Triggered Successfully ⚡"}
