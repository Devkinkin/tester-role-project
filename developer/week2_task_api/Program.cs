using Microsoft.EntityFrameworkCore;
using TaskApi.Data;
using TaskApi.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite("Data Source=tasks-api.db"));

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    db.Database.EnsureCreated();
}

app.MapGet("/api/tasks", async (AppDbContext db) =>
    await db.Tasks.AsNoTracking().ToListAsync());

app.MapGet("/api/tasks/{id:int}", async (int id, AppDbContext db) =>
    await db.Tasks.FindAsync(id) is TaskItem task
        ? Results.Ok(task)
        : Results.NotFound());

app.MapPost("/api/tasks", async (TaskItem input, AppDbContext db) =>
{
    if (string.IsNullOrWhiteSpace(input.Title))
        return Results.BadRequest(new { message = "Title is required." });

    var task = new TaskItem
    {
        Title = input.Title.Trim(),
        IsComplete = input.IsComplete
    };

    db.Tasks.Add(task);
    await db.SaveChangesAsync();

    return Results.Created($"/api/tasks/{task.Id}", task);
});

app.MapPut("/api/tasks/{id:int}", async (int id, TaskItem input, AppDbContext db) =>
{
    var task = await db.Tasks.FindAsync(id);

    if (task is null)
        return Results.NotFound();

    if (string.IsNullOrWhiteSpace(input.Title))
        return Results.BadRequest(new { message = "Title is required." });

    task.Title = input.Title.Trim();
    task.IsComplete = input.IsComplete;

    await db.SaveChangesAsync();
    return Results.NoContent();
});

app.MapDelete("/api/tasks/{id:int}", async (int id, AppDbContext db) =>
{
    var task = await db.Tasks.FindAsync(id);

    if (task is null)
        return Results.NotFound();

    db.Tasks.Remove(task);
    await db.SaveChangesAsync();

    return Results.NoContent();
});

app.Run();
