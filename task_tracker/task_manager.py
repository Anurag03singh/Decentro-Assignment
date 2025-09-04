from datetime import datetime, date
from typing import List, Dict, Any, Optional
from storage import TaskStorage


class TaskManager:
    
    def __init__(self, storage_filename: str = "tasks.json"):
        self.storage = TaskStorage(storage_filename)
        self.tasks = self.storage.load_tasks()
        self._next_id = self._get_next_id()
    
    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def add_task(self, title: str, description: str = "", due_date: str = "") -> Dict[str, Any]:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        parsed_due_date = None
        if due_date.strip():
            try:
                parsed_due_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Due date must be in YYYY-MM-DD format")
        
        task = {
            'id': self._next_id,
            'title': title.strip(),
            'description': description.strip(),
            'status': 'Pending',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'due_date': due_date.strip() if due_date.strip() else None
        }
        
        self.tasks.append(task)
        self._next_id += 1
        self._save_tasks()
        
        return task
    
    def list_tasks(self, sort_by_due_date: bool = False) -> List[Dict[str, Any]]:
        if not sort_by_due_date:
            return self.tasks.copy()
        
        def sort_key(task):
            if task['due_date']:
                try:
                    return datetime.strptime(task['due_date'], "%Y-%m-%d").date()
                except ValueError:
                    return date.max
            return date.max
        
        return sorted(self.tasks, key=sort_key)
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def mark_task_complete(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task['status'] = 'Completed'
            task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_tasks()
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self._save_tasks()
                return True
        return False
    
    def get_task_stats(self) -> Dict[str, int]:
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task['status'] == 'Completed'])
        pending = total - completed
        
        today = date.today()
        overdue = 0
        for task in self.tasks:
            if (task['status'] == 'Pending' and 
                task['due_date'] and 
                task['due_date'].strip()):
                try:
                    due_date = datetime.strptime(task['due_date'], "%Y-%m-%d").date()
                    if due_date < today:
                        overdue += 1
                except ValueError:
                    pass
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'overdue': overdue
        }
    
    def _save_tasks(self) -> None:
        self.storage.save_tasks(self.tasks)
    
    def reload_tasks(self) -> None:
        self.tasks = self.storage.load_tasks()
        self._next_id = self._get_next_id()
