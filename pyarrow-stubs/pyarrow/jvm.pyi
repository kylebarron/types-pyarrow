from _typeshed import Incomplete

class _JvmBufferNanny:
    ref_manager: Incomplete
    def __init__(self, jvm_buf) -> None: ...
    def __del__(self) -> None: ...

def jvm_buffer(jvm_buf): ...
def field(jvm_field): ...
def schema(jvm_schema): ...
def array(jvm_array): ...
def record_batch(jvm_vector_schema_root): ...
