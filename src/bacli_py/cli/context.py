"""Output context management for CLI commands."""

from __future__ import annotations

from enum import IntEnum


class OutputLevel(IntEnum):
    """Output verbosity level."""

    QUIET = 0  # Errors only
    NORMAL = 1  # Standard output
    VERBOSE = 2  # Detailed output


class OutputContext:
    """Global output context for controlling verbosity.

    This class manages the output level across all CLI commands.
    Use set_level() in the main callback and check is_quiet()/is_verbose()
    in individual commands.
    """

    _level: OutputLevel = OutputLevel.NORMAL

    @classmethod
    def set_level(cls, quiet: bool = False, verbose: bool = False) -> None:
        """Set the output level based on flags.

        Args:
            quiet: If True, set to QUIET level.
            verbose: If True, set to VERBOSE level.
                     quiet takes precedence if both are True.
        """
        if quiet:
            cls._level = OutputLevel.QUIET
        elif verbose:
            cls._level = OutputLevel.VERBOSE
        else:
            cls._level = OutputLevel.NORMAL

    @classmethod
    def reset(cls) -> None:
        """Reset to default NORMAL level."""
        cls._level = OutputLevel.NORMAL

    @classmethod
    def is_quiet(cls) -> bool:
        """Check if output should be minimal."""
        return cls._level == OutputLevel.QUIET

    @classmethod
    def is_verbose(cls) -> bool:
        """Check if output should be detailed."""
        return cls._level == OutputLevel.VERBOSE

    @classmethod
    def is_normal(cls) -> bool:
        """Check if output level is normal."""
        return cls._level == OutputLevel.NORMAL

    @classmethod
    def get_level(cls) -> OutputLevel:
        """Get current output level."""
        return cls._level
