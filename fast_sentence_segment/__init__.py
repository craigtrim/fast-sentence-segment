from .bp import *
from .svc import *
from .dmo import *

from .bp.segmenter import Segmenter

segment = Segmenter().input_text


def segment_text(input_text: str, flatten: bool = False) -> list:
    results = segment(input_text)

    if flatten:
        flat = []
        [[flat.append(y) for y in x] for x in results]
        return flat

    return results
