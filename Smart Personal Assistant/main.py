from modules import task_manager, weather, news, productivity, reminder

task_manager.create_db()

while True:
    print("\n========== SMART PERSONAL ASSISTANT ==========")
    print("1. ➕ Add Task")
    print("2. 📋 View Tasks")
    print("3. ❌ Delete Task")
    print("4. ✅ Mark Completed")
    print("5. 🌦 Check Weather")
    print("6. 📰 Show News")
    print("7. 📊 Show Chart")
    print("8. 🔔 Show Reminder")
    print("0. 🚪 Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        title = input("Enter task: ")
        date = input("Enter due date: ")
        task_manager.add_task(title, date)
        print("✅ Task added!")

    elif choice == "2":
        tasks = task_manager.view_tasks()
        print("\n📋 Your Tasks:")
        if not tasks:
            print("No tasks found 😴")
        else:
            for t in tasks:
                status = "✅ Done" if t[3] == 1 else "⏳ Pending"
                print(f"ID:{t[0]} | {t[1]} | {t[2]} | {status}")

    elif choice == "3":
        task_id = int(input("Enter task ID: "))
        task_manager.delete_task(task_id)
        print("🗑 Task deleted!")

    elif choice == "4":
        task_id = int(input("Enter task ID: "))
        task_manager.mark_completed(task_id)
        print("🎉 Task completed!")

    elif choice == "5":
        city = input("Enter city: ")
        print(weather.get_weather(city))

    elif choice == "6":
        headlines = news.get_news()
        print("\n📰 News:")
        for i, h in enumerate(headlines, 1):
            print(f"{i}. {h}")

    elif choice == "7":
        tasks = task_manager.view_tasks()
        if not tasks:
            print("No data for chart 📉")
        else:
            print("📊 Opening chart...")
            productivity.generate_chart(tasks)

    elif choice == "8":
        msg = input("Enter reminder: ")
        reminder.show_notification(msg)
        print("🔔 Reminder shown!")

    elif choice == "0":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice")