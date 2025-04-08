using ComicsCatalog.Models;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// Configuração do banco de dados
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
builder.Services.AddDbContext<ComicsDbContext>(options =>
	options.UseSqlServer(connectionString));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
	app.UseExceptionHandler("/Home/Error");
	app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
	name: "default",
	pattern: "{controller=Home}/{action=Index}/{id?}");

// After the line that creates the DbContext
using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;
    try
    {
        var context = services.GetRequiredService<ComicsDbContext>();
        var logger = services.GetRequiredService<ILogger<Program>>();

        // First check if the table exists
        var tableExists = false;
        try {
            // Try a simple count query
            var count = context.Comics.Count();
            tableExists = true;
            logger.LogInformation("Comics table exists with {Count} records", count);
        }
        catch {
            logger.LogWarning("Comics table doesn't exist yet");
        }

        if (!tableExists) {
            // Create the table directly with SQL
            logger.LogInformation("Creating Comics table directly...");
            var createTableSql = @"
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Comics')
                BEGIN
                    CREATE TABLE Comics (
                        Id INT PRIMARY KEY IDENTITY(1,1),
                        Title NVARCHAR(MAX) NOT NULL,
                        Publisher NVARCHAR(MAX) NOT NULL,
                        Writer NVARCHAR(MAX) NOT NULL,
                        Artist NVARCHAR(MAX) NOT NULL,
                        ReleaseYear INT NOT NULL,
                        IssueNumber INT NOT NULL,
                        CoverImage NVARCHAR(MAX) NULL,
                        Description NVARCHAR(MAX) NULL,
                        Price DECIMAL(18,2) NULL,
                        DateAdded DATETIME2 NOT NULL
                    )
                END";

            context.Database.ExecuteSqlRaw(createTableSql);
            logger.LogInformation("Comics table created successfully");

            // Add initial data
            logger.LogInformation("Adding initial seed data...");
            context.Comics.AddRange(
                new Comic { Title = "Batman: The Dark Knight Returns", Publisher = "DC Comics", Writer = "Frank Miller", Artist = "Frank Miller", ReleaseYear = 1986, IssueNumber = 1, DateAdded = DateTime.Now },
                new Comic { Title = "Watchmen", Publisher = "DC Comics", Writer = "Alan Moore", Artist = "Dave Gibbons", ReleaseYear = 1986, IssueNumber = 1, DateAdded = DateTime.Now },
                new Comic { Title = "Saga", Publisher = "Image Comics", Writer = "Brian K. Vaughan", Artist = "Fiona Staples", ReleaseYear = 2012, IssueNumber = 1, DateAdded = DateTime.Now },
                new Comic { Title = "Spider-Man: Maximum Carnage", Publisher = "Marvel Comics", Writer = "Tom DeFalco", Artist = "Mark Bagley", ReleaseYear = 1993, IssueNumber = 1, DateAdded = DateTime.Now }
            );
            context.SaveChanges();
            logger.LogInformation("Seed data added successfully");
        }
    }
    catch (Exception ex)
    {
        var logger = services.GetRequiredService<ILogger<Program>>();
        logger.LogError(ex, "An error occurred during database initialization: {Message}", ex.Message);

        // Get more detailed exception info
        if (ex.InnerException != null) {
            logger.LogError("Inner exception: {Message}", ex.InnerException.Message);
        }
    }
}

app.Run();
