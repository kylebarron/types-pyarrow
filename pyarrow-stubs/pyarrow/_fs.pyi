from typing import Any, ClassVar

from typing import overload
import _abc
import abc
import datetime
import enum
import importlib._bootstrap
import pyarrow.lib
Directory: importlib._bootstrap.FileType
File: importlib._bootstrap.FileType
NotFound: importlib._bootstrap.FileType
Unknown: importlib._bootstrap.FileType
_stringify_path: function
abstractmethod: function

class ABC:
    _abc_impl: ClassVar[_abc._abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    __slots__: ClassVar[tuple] = ...

class FileInfo(pyarrow.lib._Weakrefable):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    base_name: Any
    extension: Any
    is_file: Any
    mtime: Any
    mtime_ns: Any
    path: Any
    size: Any
    type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class FileSelector(pyarrow.lib._Weakrefable):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    allow_not_found: Any
    base_dir: Any
    recursive: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class FileSystem(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    type_name: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _wrap_input_stream(self, stream, path, compression, buffer_size) -> Any: ...
    def _wrap_output_stream(self, stream, path, compression, buffer_size) -> Any: ...
    def copy_file(self, src, dest) -> Any: ...
    def create_dir(self, *args, **kwargs) -> Any: ...
    def delete_dir(self, path) -> Any: ...
    def delete_dir_contents(self, *args, **kwargs) -> Any: ...
    def delete_file(self, path) -> Any: ...
    def equals(self, FileSystemother) -> Any: ...
    @overload
    def from_uri(self, uri) -> Any: ...
    @overload
    def from_uri(self, uri) -> Any: ...
    def get_file_info(self, paths_or_selector) -> Any: ...
    def move(self, src, dest) -> Any: ...
    def normalize_path(self, path) -> Any: ...
    @overload
    def open_append_stream(self, path, compression = ..., buffer_size = ..., metadata = ...) -> Any: ...
    @overload
    def open_append_stream(self, path) -> Any: ...
    @overload
    def open_input_file(self, path) -> Any: ...
    @overload
    def open_input_file(self) -> Any: ...
    @overload
    def open_input_file(self, path) -> Any: ...
    @overload
    def open_input_stream(self, path, compression = ..., buffer_size = ...) -> Any: ...
    @overload
    def open_input_stream(self) -> Any: ...
    @overload
    def open_input_stream(self, path) -> Any: ...
    @overload
    def open_output_stream(self, path, compression = ..., buffer_size = ..., metadata = ...) -> Any: ...
    @overload
    def open_output_stream(self, path) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class FileSystemHandler(abc.ABC):
    _abc_impl: ClassVar[_abc._abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    def copy_file(self, src, dest) -> Any: ...
    def create_dir(self, path, recursive) -> Any: ...
    def delete_dir(self, path) -> Any: ...
    def delete_dir_contents(self, path, missing_dir_ok = ...) -> Any: ...
    def delete_file(self, path) -> Any: ...
    def delete_root_dir_contents(self) -> Any: ...
    @overload
    def get_file_info(self, paths) -> Any: ...
    @overload
    def get_file_info(self, paths) -> Any: ...
    def get_file_info_selector(self, selector) -> Any: ...
    def get_type_name(self) -> Any: ...
    def move(self, src, dest) -> Any: ...
    def normalize_path(self, path) -> Any: ...
    def open_append_stream(self, path, metadata) -> Any: ...
    def open_input_file(self, path) -> Any: ...
    def open_input_stream(self, path) -> Any: ...
    def open_output_stream(self, path, metadata) -> Any: ...

class FileType(enum.IntEnum):
    class _member_type_:
        denominator: Any
        imag: Any
        numerator: Any
        real: Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @overload
        def as_integer_ratio(self) -> Any: ...
        @overload
        def as_integer_ratio(self) -> Any: ...
        @overload
        def as_integer_ratio(self) -> Any: ...
        def bit_count(self) -> Any: ...
        def bit_length(self) -> Any: ...
        def conjugate(self, *args, **kwargs) -> Any: ...
        @classmethod
        def from_bytes(cls, *args, **kwargs) -> Any: ...
        def to_bytes(self, *args, **kwargs) -> Any: ...
        def __abs__(self) -> Any: ...
        def __add__(self, other) -> Any: ...
        def __and__(self, other) -> Any: ...
        def __bool__(self) -> Any: ...
        def __ceil__(self, *args, **kwargs) -> Any: ...
        def __divmod__(self, other) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __float__(self) -> Any: ...
        def __floor__(self, *args, **kwargs) -> Any: ...
        def __floordiv__(self, other) -> Any: ...
        def __format__(self, *args, **kwargs) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __getnewargs__(self, *args, **kwargs) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __hash__(self) -> Any: ...
        def __index__(self) -> Any: ...
        def __int__(self) -> Any: ...
        def __invert__(self) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __lshift__(self, other) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __mod__(self, other) -> Any: ...
        def __mul__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __neg__(self) -> Any: ...
        def __or__(self, other) -> Any: ...
        def __pos__(self) -> Any: ...
        def __pow__(self, other) -> Any: ...
        def __radd__(self, other) -> Any: ...
        def __rand__(self, other) -> Any: ...
        def __rdivmod__(self, other) -> Any: ...
        def __rfloordiv__(self, other) -> Any: ...
        def __rlshift__(self, other) -> Any: ...
        def __rmod__(self, other) -> Any: ...
        def __rmul__(self, other) -> Any: ...
        def __ror__(self, other) -> Any: ...
        def __round__(self) -> Any: ...
        def __rpow__(self, other) -> Any: ...
        def __rrshift__(self, other) -> Any: ...
        def __rshift__(self, other) -> Any: ...
        def __rsub__(self, other) -> Any: ...
        def __rtruediv__(self, other) -> Any: ...
        def __rxor__(self, other) -> Any: ...
        def __sizeof__(self) -> Any: ...
        def __sub__(self, other) -> Any: ...
        def __truediv__(self, other) -> Any: ...
        def __trunc__(self) -> Any: ...
        def __xor__(self, other) -> Any: ...
    __new__: ClassVar[function] = ...
    Directory: ClassVar[importlib._bootstrap.FileType] = ...
    File: ClassVar[importlib._bootstrap.FileType] = ...
    NotFound: ClassVar[importlib._bootstrap.FileType] = ...
    Unknown: ClassVar[importlib._bootstrap.FileType] = ...
    _generate_next_value_: ClassVar[function] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _value2member_map_: ClassVar[dict] = ...

class LocalFileSystem(FileSystem):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def _reconstruct(cls, typecls, kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class PyFileSystem(FileSystem):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    handler: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class SubTreeFileSystem(FileSystem):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    base_fs: Any
    base_path: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _MockFileSystem(FileSystem):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class timezone(datetime.tzinfo):
    max: ClassVar[datetime.timezone] = ...
    min: ClassVar[datetime.timezone] = ...
    utc: ClassVar[datetime.timezone] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def dst(self, *args, **kwargs) -> Any: ...
    def fromutc(self, *args, **kwargs) -> Any: ...
    def tzname(self, *args, **kwargs) -> Any: ...
    def utcoffset(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs) -> Any: ...
def _copy_files(FileSystemsource_fs, unicodesource_path, FileSystemdestination_fs, unicodedestination_path, int64_tchunk_size, booluse_threads) -> Any: ...
def _copy_files_selector(FileSystemsource_fs, FileSelectorsource_sel, FileSystemdestination_fs, unicodedestination_base_dir, int64_tchunk_size, booluse_threads) -> Any: ...
def _detect_compression(path) -> Any: ...
def _file_type_to_string(ty) -> Any: ...
def frombytes(*args, **kwargs) -> Any: ...
def tobytes(o) -> Any: ...
