def format_string(string, formatter=None):
    """Format a string using the formatter object, which is expeted to have a
    format() method that accepts a string."""
    class DefaultFormatter:
        """Format a string in title case."""
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)
