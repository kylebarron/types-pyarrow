import pyarrow._hdfsio as _hdfsio
from _typeshed import Incomplete
from collections.abc import Generator
from pyarrow.filesystem import FileSystem as FileSystem
from pyarrow.util import implements as implements

class HadoopFileSystem(_hdfsio.HadoopFileSystem, FileSystem):
    def __init__(self, host: str = ..., port: int = ..., user: Incomplete | None = ..., kerb_ticket: Incomplete | None = ..., driver: str = ..., extra_conf: Incomplete | None = ...) -> None: ...
    def __reduce__(self): ...
    def isdir(self, path): ...
    def isfile(self, path): ...
    def delete(self, path, recursive: bool = ...): ...
    def mkdir(self, path, **kwargs): ...
    def rename(self, path, new_path): ...
    def exists(self, path): ...
    def ls(self, path, detail: bool = ...): ...
    def walk(self, top_path) -> Generator[Incomplete, None, None]: ...

def connect(host: str = ..., port: int = ..., user: Incomplete | None = ..., kerb_ticket: Incomplete | None = ..., extra_conf: Incomplete | None = ...): ...
