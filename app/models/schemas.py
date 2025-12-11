from pydantic import BaseModel
from typing import Dict, Optional

class CreateGraphRequest(BaseModel):
    preset: Optional[str] = None      # e.g., "code_review"
    graph_def: Optional[Dict] = None  # custom graph

class RunGraphRequest(BaseModel):
    graph_id: str
    initial_state: Dict
