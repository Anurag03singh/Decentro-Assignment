import sys
from datetime import datetime
from task_manager import TaskManager


class TaskTrackerCLI:
    
    def __init__(self):
        self.task_manager = TaskManager()
    
    def print_banner(self):
        print("=" * 50)
        print("📋 TASK TRACKER CLI")
        print("=" * 50)
    
    def print_menu(self):
        print("\n📌 What would you like to do?")
        print("1. ➕ Add a new task")
        print("2. 📋 List all tasks")
        print("3. ✅ Mark task as completed")
        print("4. 🗑️  Delete a task")
        print("5. 📊 Show task statistics")
        print("6. 🔄 Sort tasks by due date")
        print("7. ❌ Exit")
        print("-" * 30)
    
    def get_user_choice(self) -> str:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Goodbye!")
            sys.exit(0)
    
    def add_task_interactive(self):
        print("\n➕ ADD NEW TASK")
        print("-" * 20)
        
        try:
            title = input("Task title (required): ").strip()
            if not title:
                print("❌ Error: Task title cannot be empty!")
                return
            
            description = input("Task description (optional): ").strip()
            due_date = ""
            while True:
                due_date_input = input("Due date (YYYY-MM-DD, optional): ").strip()
                if not due_date_input:
                    break
                
                try:
                    datetime.strptime(due_date_input, "%Y-%m-%d")
                    due_date = due_date_input
                    break
                except ValueError:
                    print("❌ Invalid date format! Please use YYYY-MM-DD or leave empty.")
            
            task = self.task_manager.add_task(title, description, due_date)
            print(f"\n✅ Task added successfully!")
            print(f"   ID: {task['id']}")
            print(f"   Title: {task['title']}")
            if task['description']:
                print(f"   Description: {task['description']}")
            if task['due_date']:
                print(f"   Due Date: {task['due_date']}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except (EOFError, KeyboardInterrupt):
            print("\n❌ Task addition cancelled.")
    
    def list_tasks_interactive(self, sort_by_due_date: bool = False):
        sort_text = " (Sorted by Due Date)" if sort_by_due_date else ""
        print(f"\n📋 ALL TASKS{sort_text}")
        print("-" * 30)
        
        tasks = self.task_manager.list_tasks(sort_by_due_date)
        
        if not tasks:
            print("📭 No tasks found. Add some tasks to get started!")
            return
        
        for task in tasks:
            status_icon = "✅" if task['status'] == 'Completed' else "⏳"
            print(f"\n{status_icon} Task ID: {task['id']}")
            print(f"   Title: {task['title']}")
            
            if task['description']:
                print(f"   Description: {task['description']}")
            
            print(f"   Status: {task['status']}")
            print(f"   Created: {task['created_at']}")
            
            if task['due_date']:
                due_date = task['due_date']
                try:
                    due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
                    today = datetime.now().date()
                    if due_date_obj < today and task['status'] == 'Pending':
                        print(f"   Due Date: {due_date} ⚠️ OVERDUE")
                    else:
                        print(f"   Due Date: {due_date}")
                except ValueError:
                    print(f"   Due Date: {due_date}")
            
            if task['status'] == 'Completed' and 'completed_at' in task:
                print(f"   Completed: {task['completed_at']}")
    
    def mark_task_complete_interactive(self):
        print("\n✅ MARK TASK AS COMPLETED")
        print("-" * 25)
        
        try:
            task_id_input = input("Enter task ID to mark as completed: ").strip()
            
            if not task_id_input.isdigit():
                print("❌ Error: Please enter a valid task ID (number)!")
                return
            
            task_id = int(task_id_input)
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"❌ Error: Task with ID {task_id} not found!")
                return
            
            if task['status'] == 'Completed':
                print(f"ℹ️  Task '{task['title']}' is already completed!")
                return
            
            if self.task_manager.mark_task_complete(task_id):
                print(f"✅ Task '{task['title']}' marked as completed!")
            else:
                print(f"❌ Error: Could not mark task {task_id} as completed!")
                
        except ValueError:
            print("❌ Error: Please enter a valid task ID!")
        except (EOFError, KeyboardInterrupt):
            print("\n❌ Operation cancelled.")
    
    def delete_task_interactive(self):
        print("\n🗑️  DELETE TASK")
        print("-" * 15)
        
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            
            if not task_id_input.isdigit():
                print("❌ Error: Please enter a valid task ID (number)!")
                return
            
            task_id = int(task_id_input)
            
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(f"❌ Error: Task with ID {task_id} not found!")
                return
            
            print(f"⚠️  Are you sure you want to delete task '{task['title']}'?")
            confirm = input("Type 'yes' to confirm: ").strip().lower()
            
            if confirm == 'yes':
                if self.task_manager.delete_task(task_id):
                    print(f"✅ Task '{task['title']}' deleted successfully!")
                else:
                    print(f"❌ Error: Could not delete task {task_id}!")
            else:
                print("❌ Task deletion cancelled.")
                
        except ValueError:
            print("❌ Error: Please enter a valid task ID!")
        except (EOFError, KeyboardInterrupt):
            print("\n❌ Operation cancelled.")
    
    def show_statistics(self):
        """Display task statistics."""
        print("\n📊 TASK STATISTICS")
        print("-" * 20)
        
        stats = self.task_manager.get_task_stats()
        
        print(f"📋 Total Tasks: {stats['total']}")
        print(f"✅ Completed: {stats['completed']}")
        print(f"⏳ Pending: {stats['pending']}")
        print(f"⚠️  Overdue: {stats['overdue']}")
        
        if stats['total'] > 0:
            completion_rate = (stats['completed'] / stats['total']) * 100
            print(f"📈 Completion Rate: {completion_rate:.1f}%")
    
    def run(self):
        """Run the main CLI loop."""
        self.print_banner()
        
        while True:
            self.print_menu()
            choice = self.get_user_choice()
            
            if choice == '1':
                self.add_task_interactive()
            elif choice == '2':
                self.list_tasks_interactive()
            elif choice == '3':
                self.mark_task_complete_interactive()
            elif choice == '4':
                self.delete_task_interactive()
            elif choice == '5':
                self.show_statistics()
            elif choice == '6':
                self.list_tasks_interactive(sort_by_due_date=True)
            elif choice == '7':
                print("\n👋 Thank you for using Task Tracker CLI!")
                print("💾 All your tasks have been saved automatically.")
                sys.exit(0)
            else:
                print("❌ Invalid choice! Please enter a number between 1-7.")
            
            input("\nPress Enter to continue...")


def main():
    try:
        app = TaskTrackerCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Task Tracker CLI closed. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
