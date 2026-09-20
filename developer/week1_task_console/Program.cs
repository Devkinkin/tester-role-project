using Microsoft.Data.Sqlite;

const string connectionString = "Data Source=tasks.db";
CreateDatabase();

while (true)
{
    Console.WriteLine("\nTASK CONSOLE");
    Console.WriteLine("1. List tasks");
    Console.WriteLine("2. Add task");
    Console.WriteLine("3. Mark complete");
    Console.WriteLine("4. Delete task");
    Console.WriteLine("0. Exit");
    Console.Write("Choose: ");

    switch (Console.ReadLine())
    {
        case "1": ListTasks(); break;
        case "2": AddTask(); break;
        case "3": MarkComplete(); break;
        case "4": DeleteTask(); break;
        case "0": return;
        default: Console.WriteLine("Choose a valid option."); break;
    }
}

void CreateDatabase()
{
    using var connection = new SqliteConnection(connectionString);
    connection.Open();

    var command = connection.CreateCommand();
    command.CommandText =
        "CREATE TABLE IF NOT EXISTS Tasks (" +
        "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
        "Title TEXT NOT NULL, " +
        "IsComplete INTEGER NOT NULL DEFAULT 0)";

    command.ExecuteNonQuery();
}

void ListTasks()
{
    using var connection = new SqliteConnection(connectionString);
    connection.Open();

    var command = connection.CreateCommand();
    command.CommandText = "SELECT Id, Title, IsComplete FROM Tasks ORDER BY Id";

    using var reader = command.ExecuteReader();

    Console.WriteLine("\nCurrent tasks:");
    while (reader.Read())
    {
        var status = reader.GetBoolean(2) ? "Done" : "Open";
        Console.WriteLine($"{reader.GetInt32(0)}. {reader.GetString(1)} [{status}]");
    }
}

void AddTask()
{
    Console.Write("Task title: ");
    var title = Console.ReadLine()?.Trim();

    if (string.IsNullOrWhiteSpace(title))
    {
        Console.WriteLine("Title cannot be empty.");
        return;
    }

    using var connection = new SqliteConnection(connectionString);
    connection.Open();

    var command = connection.CreateCommand();
    command.CommandText = "INSERT INTO Tasks (Title, IsComplete) VALUES ($title, 0)";
    command.Parameters.AddWithValue("$title", title);
    command.ExecuteNonQuery();

    Console.WriteLine("Task added.");
}

void MarkComplete()
{
    Console.Write("Task ID: ");
    if (!int.TryParse(Console.ReadLine(), out var id))
    {
        Console.WriteLine("Invalid ID.");
        return;
    }

    using var connection = new SqliteConnection(connectionString);
    connection.Open();

    var command = connection.CreateCommand();
    command.CommandText = "UPDATE Tasks SET IsComplete = 1 WHERE Id = $id";
    command.Parameters.AddWithValue("$id", id);

    Console.WriteLine(command.ExecuteNonQuery() == 1
        ? "Task updated."
        : "Task not found.");
}

void DeleteTask()
{
    Console.Write("Task ID: ");
    if (!int.TryParse(Console.ReadLine(), out var id))
    {
        Console.WriteLine("Invalid ID.");
        return;
    }

    using var connection = new SqliteConnection(connectionString);
    connection.Open();

    var command = connection.CreateCommand();
    command.CommandText = "DELETE FROM Tasks WHERE Id = $id";
    command.Parameters.AddWithValue("$id", id);

    Console.WriteLine(command.ExecuteNonQuery() == 1
        ? "Task deleted."
        : "Task not found.");
}
