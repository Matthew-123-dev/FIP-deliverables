
from typing import Any


class CourseModule:
	"""Represents a course module with private internal state.

	Attributes are intentionally private to prevent external code from
	mutating internal values directly. Public methods offer controlled
	ways to read state and update progress/content.
	"""

	def __init__(self, title: str, content: str = "") -> None:
		self.__title = title
		self.__content = content
		self.__progress = 0  # 0-100 integer
		self.__completed = False

	# --- Read-only accessors ---
	def title(self) -> str:
		"""Return the module title (read-only)."""
		return self.__title

	def content(self) -> str:
		"""Return the module content (read-only)."""
		return self.__content

	def progress(self) -> int:
		"""Return current progress as integer percent (0-100)."""
		return self.__progress

	def is_completed(self) -> bool:
		"""Return completion status."""
		return self.__completed

	# --- Controlled mutators ---
	def append_content(self, more: str) -> None:
		"""Add more text to the content in a controlled way."""
		if not isinstance(more, str):
			raise TypeError("Content must be a string")
		if more:
			self.__content += more

	def increase_progress(self, amount: int) -> None:
		"""Increase progress by `amount` percent.

		Rules:
		- amount must be positive integer
		- progress cannot exceed 100
		- progress can only increase (no direct decrease allowed)
		"""
		if not isinstance(amount, int):
			raise TypeError("amount must be an int")
		if amount <= 0:
			raise ValueError("amount must be a positive integer")

		new_progress = self.__progress + amount
		if new_progress >= 100:
			self.__progress = 100
			self.__completed = True
		else:
			self.__progress = new_progress

	def mark_complete(self) -> None:
		"""Mark the module as complete (sets progress to 100)."""
		self.__progress = 100
		self.__completed = True

	# Intentionally no setters for title/content/progress to prevent direct modification

	def __repr__(self) -> str:
		return (
			f"CourseModule(title={self.__title!r}, progress={self.__progress}%, "
			f"completed={self.__completed})"
		)


if __name__ == "__main__":
	# Quick demonstration / smoke test
	m = CourseModule("Intro to Debugging", "Chapter 1: Basics\n")
	print("Created:", m)
	print("Title (read-only):", m.title())
	print("Content (read-only):", m.content())

	# Increase progress safely
	m.increase_progress(25)
	print("After +25%:", m.progress(), "completed?", m.is_completed())

	m.increase_progress(50)
	print("After +50%:", m.progress(), "completed?", m.is_completed())

	# Mark complete
	m.mark_complete()
	print("After mark_complete:", m.progress(), "completed?", m.is_completed())

	# Demonstrate invalid operations (will raise)
	try:
		m.increase_progress(-10)
	except Exception as e:  
		print("Expected error for negative increase:", type(e).__name__, e)
