from _typeshed import Incomplete
from pyarrow._compute import ArraySortOptions as ArraySortOptions, AssumeTimezoneOptions as AssumeTimezoneOptions, CastOptions as CastOptions, CountOptions as CountOptions, CumulativeSumOptions as CumulativeSumOptions, DayOfWeekOptions as DayOfWeekOptions, DictionaryEncodeOptions as DictionaryEncodeOptions, ElementWiseAggregateOptions as ElementWiseAggregateOptions, Expression as Expression, ExtractRegexOptions as ExtractRegexOptions, FilterOptions as FilterOptions, Function as Function, FunctionOptions as FunctionOptions, FunctionRegistry as FunctionRegistry, HashAggregateFunction as HashAggregateFunction, HashAggregateKernel as HashAggregateKernel, IndexOptions as IndexOptions, JoinOptions as JoinOptions, Kernel as Kernel, MakeStructOptions as MakeStructOptions, MapLookupOptions as MapLookupOptions, MatchSubstringOptions as MatchSubstringOptions, ModeOptions as ModeOptions, NullOptions as NullOptions, PadOptions as PadOptions, PartitionNthOptions as PartitionNthOptions, QuantileOptions as QuantileOptions, RandomOptions as RandomOptions, RankOptions as RankOptions, ReplaceSliceOptions as ReplaceSliceOptions, ReplaceSubstringOptions as ReplaceSubstringOptions, RoundOptions as RoundOptions, RoundTemporalOptions as RoundTemporalOptions, RoundToMultipleOptions as RoundToMultipleOptions, ScalarAggregateFunction as ScalarAggregateFunction, ScalarAggregateKernel as ScalarAggregateKernel, ScalarAggregateOptions as ScalarAggregateOptions, ScalarFunction as ScalarFunction, ScalarKernel as ScalarKernel, ScalarUdfContext as ScalarUdfContext, SelectKOptions as SelectKOptions, SetLookupOptions as SetLookupOptions, SliceOptions as SliceOptions, SortOptions as SortOptions, SplitOptions as SplitOptions, SplitPatternOptions as SplitPatternOptions, StrftimeOptions as StrftimeOptions, StrptimeOptions as StrptimeOptions, StructFieldOptions as StructFieldOptions, TDigestOptions as TDigestOptions, TakeOptions as TakeOptions, TrimOptions as TrimOptions, Utf8NormalizeOptions as Utf8NormalizeOptions, VarianceOptions as VarianceOptions, VectorFunction as VectorFunction, VectorKernel as VectorKernel, WeekOptions as WeekOptions, call_function as call_function, function_registry as function_registry, get_function as get_function, list_functions as list_functions, register_scalar_function as register_scalar_function
from pyarrow.vendored import docscrape as docscrape
from typing import NamedTuple

class _OptionsClassDoc(NamedTuple):
    params: Incomplete

def cast(arr, target_type: Incomplete | None = ..., safe: Incomplete | None = ..., options: Incomplete | None = ...): ...
def index(data, value, start: Incomplete | None = ..., end: Incomplete | None = ..., *, memory_pool: Incomplete | None = ...): ...
def take(data, indices, *, boundscheck: bool = ..., memory_pool: Incomplete | None = ...): ...
def fill_null(values, fill_value): ...
def top_k_unstable(values, k, sort_keys: Incomplete | None = ..., *, memory_pool: Incomplete | None = ...): ...
def bottom_k_unstable(values, k, sort_keys: Incomplete | None = ..., *, memory_pool: Incomplete | None = ...): ...
def random(n, *, initializer: str = ..., options: Incomplete | None = ..., memory_pool: Incomplete | None = ...): ...
def field(*name_or_index): ...
def scalar(value): ...