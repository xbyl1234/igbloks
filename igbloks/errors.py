class IGBlokException(Exception): pass

class InvalidRawBranchError(IGBlokException): pass
class NonMatchingBKIDError(IGBlokException): pass
class MissingDefaultBuilderError(IGBlokException): pass