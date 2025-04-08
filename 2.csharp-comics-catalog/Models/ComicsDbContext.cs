using Microsoft.EntityFrameworkCore;

namespace ComicsCatalog.Models
{
    public class ComicsDbContext : DbContext
    {
        public ComicsDbContext(DbContextOptions<ComicsDbContext> options)
            : base(options)
        {
        }

        public DbSet<Comic> Comics { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // Fix the decimal precision warning
            modelBuilder.Entity<Comic>()
                .Property(c => c.Price)
                .HasColumnType("decimal(18,2)");

            // Make sure to map to the correct table name
            modelBuilder.Entity<Comic>().ToTable("Comics");
        }
    }
}
