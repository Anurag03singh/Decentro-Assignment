# Task Tracker CLI

A simple command-line task management application built with Python. This application allows you to add, list, mark complete, and delete tasks with persistent storage using JSON files.

## 🚀 Features

### Core Features
- ➕ **Add Tasks** - Create new tasks with titles and optional descriptions
- 📋 **List Tasks** - View all tasks with their details and status
- ✅ **Mark Complete** - Update task status to completed
- 🗑️ **Delete Tasks** - Remove tasks permanently
- 💾 **Data Persistence** - All tasks are automatically saved to `tasks.json`

### Bonus Features
- 📅 **Due Dates** - Add optional due dates to tasks (YYYY-MM-DD format)
- 🔄 **Sort by Due Date** - View tasks sorted by their due dates
- ⚠️ **Overdue Detection** - Automatically identifies overdue tasks
- 📊 **Statistics** - View completion rates and task statistics
- 🎨 **User-Friendly Interface** - Clean CLI with emojis and clear formatting

## 📁 Project Structure

```
task_tracker/
│
├── main.py                 # CLI entry point and user interface
├── task_manager.py         # Core task management functions
├── storage.py              # JSON file read/write operations
├── tasks.json              # Auto-generated task data storage
└── README.md               # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation
1. Download or clone the `task_tracker` directory
2. Navigate to the project directory:
   ```bash
   cd task_tracker
   ```

## 📖 How to Run

### Start the Application
```bash
python main.py
```

### Menu Options
Once the application starts, you'll see a menu with the following options:

1. **➕ Add a new task** - Create a task with title, description, and due date
2. **📋 List all tasks** - View all tasks with their current status
3. **✅ Mark task as completed** - Change a task's status to completed
4. **🗑️ Delete a task** - Permanently remove a task
5. **📊 Show task statistics** - View completion rates and overdue tasks
6. **🔄 Sort tasks by due date** - List tasks ordered by due date
7. **❌ Exit** - Close the application

### Example Usage

#### Adding a Task
```
Enter your choice (1-7): 1
Task title (required): Complete Python assignment
Task description (optional): Finish the task tracker CLI project
Due date (YYYY-MM-DD, optional): 2024-01-15
```

#### Listing Tasks
```
Enter your choice (1-7): 2

📋 ALL TASKS
------------------------------

⏳ Task ID: 1
   Title: Complete Python assignment
   Description: Finish the task tracker CLI project
   Status: Pending
   Created: 2024-01-10 14:30:00
   Due Date: 2024-01-15
```

#### Marking Task Complete
```
Enter your choice (1-7): 3
Enter task ID to mark as completed: 1
✅ Task 'Complete Python assignment' marked as completed!
```

## 💾 Data Storage

- Tasks are automatically saved to `tasks.json` in the same directory
- The file is created automatically when you first add a task
- Data persists between application runs
- Each task includes:
  - Unique ID
  - Title and description
  - Status (Pending/Completed)
  - Creation timestamp
  - Due date (optional)
  - Completion timestamp (when marked complete)

## 🛠️ Technical Implementation

### Core Modules

#### `storage.py`
- Handles JSON file operations
- Provides backup functionality
- Error handling for file operations

#### `task_manager.py`
- Core business logic for task operations
- Task validation and ID management
- Statistics calculation
- Due date handling and sorting

#### `main.py`
- Command-line interface
- User input validation
- Interactive menu system
- Error handling and user feedback

### Key Features Implementation

#### Due Date Support
- Accepts dates in YYYY-MM-DD format
- Validates date format on input
- Automatically detects overdue tasks
- Sorts tasks by due date when requested

#### Data Validation
- Required title validation
- Date format validation
- Task ID validation
- Safe file operations with error handling

## 🎯 Challenges Faced & Solutions

### Challenge 1: Data Persistence
**Problem**: Ensuring tasks persist between application runs
**Solution**: Implemented a robust JSON storage system with automatic file creation and error handling

### Challenge 2: User Input Validation
**Problem**: Handling invalid user inputs gracefully
**Solution**: Added comprehensive validation for all user inputs with clear error messages

### Challenge 3: Date Handling
**Problem**: Managing due dates and overdue detection
**Solution**: Used Python's datetime module for date parsing and comparison

### Challenge 4: User Experience
**Problem**: Making the CLI interface intuitive and user-friendly
**Solution**: Added emojis, clear formatting, and confirmation prompts for destructive operations

## 🧪 Testing

The application includes built-in error handling and validation. To test:

1. **Add tasks** with various combinations of title, description, and due dates
2. **List tasks** to verify display formatting
3. **Mark tasks complete** and verify status changes
4. **Delete tasks** and confirm removal
5. **Test invalid inputs** (empty titles, invalid dates, non-existent task IDs)
6. **Restart application** to verify data persistence

## 🔮 Future Enhancements

Potential improvements for future versions:
- Task categories/tags
- Priority levels
- Search and filter functionality
- Task editing capabilities
- Export to different formats
- Recurring tasks
- Command-line arguments for quick operations

## 📝 License
Feel free to use and modify as needed.


**Happy Task Tracking! 🎉**
