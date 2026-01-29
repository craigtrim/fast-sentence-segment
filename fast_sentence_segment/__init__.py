from .bp import *
from .svc import *
from .dmo import *

from .bp.segmenter import Segmenter
from .dmo.unwrap_hard_wrapped_text import unwrap_hard_wrapped_text
from .dmo.normalize_quotes import normalize_quotes

segment = Segmenter().input_text


def segment_text(input_text: str, flatten: bool = False, unwrap: bool = False) -> list:
    if unwrap:
        input_text = unwrap_hard_wrapped_text(input_text)
        input_text = normalize_quotes(input_text)

    results = segment(input_text)

    if flatten:
        flat = []
        [[flat.append(y) for y in x] for x in results]
        return flat

    return results
