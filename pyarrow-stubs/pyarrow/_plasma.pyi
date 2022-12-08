from typing import Any, ClassVar

import _abc
import collections.abc
import pyarrow.lib
PLASMA_WAIT_TIMEOUT: int

class ArrowException(Exception): ...

class ObjectID(pyarrow.lib._Weakrefable):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def binary(self) -> Any: ...
    def from_random(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class ObjectNotAvailable(pyarrow.lib._Weakrefable):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PlasmaBuffer(pyarrow.lib.Buffer):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce_cython__(self) -> Any: ...
    def __setstate_cython__(self, __pyx_state) -> Any: ...

class PlasmaClient(pyarrow.lib._Weakrefable):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    store_socket_name: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def _release(self, ObjectIDobject_id) -> Any: ...
    def contains(self, ObjectIDobject_id) -> Any: ...
    def create(self, ObjectIDobject_id, int64_tdata_size, stringmetadata = ...) -> Any: ...
    def create_and_seal(self, ObjectIDobject_id, stringdata, stringmetadata = ...) -> Any: ...
    def debug_string(self) -> Any: ...
    def decode_notifications(self, *args, **kwargs) -> Any: ...
    def delete(self, object_ids) -> Any: ...
    def disconnect(self) -> Any: ...
    def evict(self, int64_tnum_bytes) -> Any: ...
    def get(self, object_ids, inttimeout_ms = ..., serialization_context = ...) -> Any: ...
    def get_buffers(self, object_ids, timeout_ms = ..., with_meta = ...) -> Any: ...
    def get_metadata(self, object_ids, timeout_ms = ...) -> Any: ...
    def get_next_notification(self) -> Any: ...
    def get_notification_socket(self) -> Any: ...
    def hash(self, ObjectIDobject_id) -> Any: ...
    def list(self) -> Any: ...
    def put(self, value, ObjectIDobject_id = ..., intmemcopy_threads = ..., serialization_context = ...) -> Any: ...
    def put_raw_buffer(self, value, ObjectIDobject_id = ..., stringmetadata = ..., intmemcopy_threads = ...) -> Any: ...
    def seal(self, ObjectIDobject_id) -> Any: ...
    def set_client_options(self, client_name, int64_tlimit_output_memory) -> Any: ...
    def store_capacity(self) -> Any: ...
    def subscribe(self) -> Any: ...
    def to_capsule(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class PlasmaObjectExists(pyarrow.lib.ArrowException): ...

class PlasmaObjectNotFound(pyarrow.lib.ArrowException): ...

class PlasmaStoreFull(pyarrow.lib.ArrowException): ...

class Sequence(collections.abc.Reversible, collections.abc.Collection):
    _abc_impl: ClassVar[_abc._abc_data] = ...
    count: ClassVar[function] = ...
    index: ClassVar[function] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    __contains__: ClassVar[function] = ...
    __getitem__: ClassVar[function] = ...
    __iter__: ClassVar[function] = ...
    __reversed__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...

def __pyx_unpickle_ObjectNotAvailable(__pyx_type, long__pyx_checksum, __pyx_state) -> Any: ...
def connect(store_socket_name, intnum_retries = ...) -> Any: ...
def frombytes(*args, **kwargs) -> Any: ...
def get_socket_from_fd(fileno, family, type) -> Any: ...
def make_object_id(object_id) -> Any: ...