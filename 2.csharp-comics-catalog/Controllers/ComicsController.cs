using ComicsCatalog.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ComicsCatalog.Controllers
{
	public class ComicsController : Controller
	{
		private readonly ComicsDbContext _context;

		public ComicsController(ComicsDbContext context)
		{
			_context = context;
		}

		// GET: Comics
		public async Task<IActionResult> Index()
		{
			try
			{
				var comics = await _context.Comics.ToListAsync();
				return View(comics);
			}
			catch (Exception ex)
			{
				Console.WriteLine($"Error in Comics/Index: {ex.Message}");
				return Content($"Error: {ex.Message}");
			}
		}

		// GET: Comics/Details/5
		public async Task<IActionResult> Details(int? id)
		{
			if (id == null)
			{
				return NotFound();
			}

			var comic = await _context.Comics
				.FirstOrDefaultAsync(m => m.Id == id);
			if (comic == null)
			{
				return NotFound();
			}

			return View(comic);
		}

		// GET: Comics/Create
		public IActionResult Create()
		{
			return View();
		}

		// POST: Comics/Create
		[HttpPost]
		[ValidateAntiForgeryToken]
		public async Task<IActionResult> Create([Bind("Title,Publisher,Writer,Artist,ReleaseYear,IssueNumber,CoverImage,Description,Price")] Comic comic)
		{
			if (ModelState.IsValid)
			{
				comic.DateAdded = DateTime.UtcNow;
				_context.Add(comic);
				await _context.SaveChangesAsync();
				return RedirectToAction(nameof(Index));
			}
			return View(comic);
		}

		// GET: Comics/Edit/5
		public async Task<IActionResult> Edit(int? id)
		{
			if (id == null)
			{
				return NotFound();
			}

			var comic = await _context.Comics.FindAsync(id);
			if (comic == null)
			{
				return NotFound();
			}
			return View(comic);
		}

		// POST: Comics/Edit/5
		[HttpPost]
		[ValidateAntiForgeryToken]
		public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Publisher,Writer,Artist,ReleaseYear,IssueNumber,CoverImage,Description,Price,DateAdded")] Comic comic)
		{
			if (id != comic.Id)
			{
				return NotFound();
			}

			if (ModelState.IsValid)
			{
				try
				{
					_context.Update(comic);
					await _context.SaveChangesAsync();
				}
				catch (DbUpdateConcurrencyException)
				{
					if (!ComicExists(comic.Id))
					{
						return NotFound();
					}
					else
					{
						throw;
					}
				}
				return RedirectToAction(nameof(Index));
			}
			return View(comic);
		}

		// GET: Comics/Delete/5
		public async Task<IActionResult> Delete(int? id)
		{
			if (id == null)
			{
				return NotFound();
			}

			var comic = await _context.Comics
				.FirstOrDefaultAsync(m => m.Id == id);
			if (comic == null)
			{
				return NotFound();
			}

			return View(comic);
		}

		// POST: Comics/Delete/5
		[HttpPost, ActionName("Delete")]
		[ValidateAntiForgeryToken]
		public async Task<IActionResult> DeleteConfirmed(int id)
		{
			var comic = await _context.Comics.FindAsync(id);
			if (comic != null)
			{
				_context.Comics.Remove(comic);
			}

			await _context.SaveChangesAsync();
			return RedirectToAction(nameof(Index));
		}

		private bool ComicExists(int id)
		{
			return _context.Comics.Any(e => e.Id == id);
		}
	}
}
