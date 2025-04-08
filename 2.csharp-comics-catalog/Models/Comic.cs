namespace ComicsCatalog.Models
{
	public class Comic
	{
		public int Id { get; set; }
		public string Title { get; set; } = string.Empty;
		public string Publisher { get; set; } = string.Empty;
		public string Writer { get; set; } = string.Empty;
		public string Artist { get; set; } = string.Empty;
		public int ReleaseYear { get; set; }
		public int IssueNumber { get; set; }
		public string? CoverImage { get; set; }
		public string? Description { get; set; }
		public decimal? Price { get; set; }
		public DateTime DateAdded { get; set; } = DateTime.UtcNow;
	}
}
