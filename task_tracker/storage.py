import json
import os
from typing import List, Dict, Any


class TaskStorage:
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self) -> None:
        if not os.path.exists(self.filename):
            self.save_tasks([])
    
    def load_tasks(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_tasks(self, tasks: List[Dict[str, Any]]) -> bool:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def backup_tasks(self) -> bool:
        try:
            backup_filename = f"{self.filename}.backup"
            tasks = self.load_tasks()
            with open(backup_filename, 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error creating backup: {e}")
            return False
