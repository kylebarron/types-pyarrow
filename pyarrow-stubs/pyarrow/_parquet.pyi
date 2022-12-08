from typing import Any, ClassVar

import pyarrow.lib
_stringify_path: function
indent: function

class ArrowException(Exception): ...

class BufferOutputStream(pyarrow.lib.NativeFile):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def getvalue(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class ColumnChunkMetaData(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    compression: Any
    data_page_offset: Any
    dictionary_page_offset: Any
    encodings: Any
    file_offset: Any
    file_path: Any
    has_dictionary_page: Any
    has_index_page: Any
    index_page_offset: Any
    is_stats_set: Any
    num_values: Any
    path_in_schema: Any
    physical_type: Any
    statistics: Any
    total_compressed_size: Any
    total_uncompressed_size: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def equals(self, ColumnChunkMetaDataother) -> Any: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class ColumnSchema(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    converted_type: Any
    length: Any
    logical_type: Any
    max_definition_level: Any
    max_repetition_level: Any
    name: Any
    path: Any
    physical_type: Any
    precision: Any
    scale: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def equals(self, ColumnSchemaother) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class FileDecryptionProperties:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class FileEncryptionProperties:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class FileMetaData(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    created_by: Any
    format_version: Any
    metadata: Any
    num_columns: Any
    num_row_groups: Any
    num_rows: Any
    schema: Any
    serialized_size: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def append_row_groups(self, FileMetaDataother) -> Any: ...
    def equals(self, FileMetaDataother) -> Any: ...
    def row_group(self, inti) -> Any: ...
    def set_file_path(self, path) -> Any: ...
    def to_dict(self) -> Any: ...
    def write_metadata_file(self, where) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class ParquetLogicalType(pyarrow.lib._Weakrefable):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    type: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def to_json(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class ParquetReader(pyarrow.lib._Weakrefable):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    _column_idx_map: _column_idx_map
    closed: Any
    column_paths: Any
    metadata: Any
    num_row_groups: Any
    schema_arrow: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def close(self) -> Any: ...
    def column_name_idx(self, column_name) -> Any: ...
    def iter_batches(self, int64_tbatch_size, row_groups, column_indices = ..., booluse_threads = ...) -> Any: ...
    def open(self, *args, **kwargs) -> Any: ...
    def read_all(self, column_indices = ..., booluse_threads = ...) -> Any: ...
    def read_column(self, intcolumn_index) -> Any: ...
    def read_row_group(self, inti, column_indices = ..., booluse_threads = ...) -> Any: ...
    def read_row_groups(self, row_groups, column_indices = ..., booluse_threads = ...) -> Any: ...
    def scan_contents(self, column_indices = ..., batch_size = ...) -> Any: ...
    def set_batch_size(self, int64_tbatch_size) -> Any: ...
    def set_use_threads(self, booluse_threads) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class ParquetSchema(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    names: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def column(self, i) -> Any: ...
    def equals(self, ParquetSchemaother) -> Any: ...
    def to_arrow_schema(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class ParquetWriter(pyarrow.lib._Weakrefable):
    allow_truncated_timestamps: Any
    coerce_timestamps: Any
    column_encoding: Any
    compression: Any
    compression_level: Any
    data_page_size: Any
    data_page_version: Any
    dictionary_pagesize_limit: Any
    encryption_properties: Any
    metadata: Any
    row_group_size: Any
    use_byte_stream_split: Any
    use_compliant_nested_type: Any
    use_deprecated_int96_timestamps: Any
    use_dictionary: Any
    version: Any
    write_batch_size: Any
    write_statistics: Any
    writer_engine_version: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def close(self) -> Any: ...
    def write_table(self, Tabletable, row_group_size = ...) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class RowGroupMetaData(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    num_columns: Any
    num_rows: Any
    total_byte_size: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def column(self, inti) -> Any: ...
    def equals(self, RowGroupMetaDataother) -> Any: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class Statistics(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    converted_type: Any
    distinct_count: Any
    has_distinct_count: Any
    has_min_max: Any
    has_null_count: Any
    logical_type: Any
    max: Any
    max_raw: Any
    min: Any
    min_raw: Any
    null_count: Any
    num_values: Any
    physical_type: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def equals(self, Statisticsother) -> Any: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

def _datetime_from_int(int64_tvalue, TimeUnitunit, tzinfo = ...) -> Any: ...
def _reconstruct_filemetadata(Bufferserialized) -> Any: ...
def frombytes(*args, **kwargs) -> Any: ...
def tobytes(o) -> Any: ...
