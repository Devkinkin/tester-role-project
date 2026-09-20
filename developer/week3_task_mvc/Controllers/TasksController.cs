using Microsoft.AspNetCore.Mvc;
using TaskMvc.Models;

namespace TaskMvc.Controllers;

public class TasksController : Controller
{
    private static readonly List<TaskItem> Tasks =
    [
        new TaskItem
        {
            Id = 1,
            Title = "Review MVC notes",
            IsComplete = false
        }
    ];

    public IActionResult Index()
    {
        return View(Tasks);
    }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Create(TaskItem input)
    {
        if (!ModelState.IsValid)
            return View("Index", Tasks);

        input.Id = Tasks.Count == 0
            ? 1
            : Tasks.Max(t => t.Id) + 1;

        Tasks.Add(input);

        return RedirectToAction(nameof(Index));
    }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Toggle(int id)
    {
        var task = Tasks.FirstOrDefault(t => t.Id == id);

        if (task is not null)
            task.IsComplete = !task.IsComplete;

        return RedirectToAction(nameof(Index));
    }
}
