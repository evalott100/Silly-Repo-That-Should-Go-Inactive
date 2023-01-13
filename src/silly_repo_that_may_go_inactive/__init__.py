from importlib.metadata import version

__version__ = version("silly_repo_that_may_go_inactive")
del version

__all__ = ["__version__"]
