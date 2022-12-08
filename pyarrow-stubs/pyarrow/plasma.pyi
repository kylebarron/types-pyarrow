from _typeshed import Incomplete
from collections.abc import Generator
from pyarrow._plasma import ObjectID as ObjectID, ObjectNotAvailable as ObjectNotAvailable, PlasmaBuffer as PlasmaBuffer, PlasmaClient as PlasmaClient, PlasmaObjectExists as PlasmaObjectExists, PlasmaObjectNotFound as PlasmaObjectNotFound, PlasmaStoreFull as PlasmaStoreFull, connect as connect

TF_PLASMA_OP_PATH: Incomplete
tf_plasma_op: Incomplete

def load_plasma_tensorflow_op() -> None: ...
def build_plasma_tensorflow_op() -> None: ...
def start_plasma_store(plasma_store_memory, use_valgrind: bool = ..., use_profiler: bool = ..., plasma_directory: Incomplete | None = ..., use_hugepages: bool = ..., external_store: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
