import collections


class ParseWarning(collections.namedtuple('ParseWarning', ['type', 'fields'])):

    def __str__(self):
        return "{}: {}".format(self.type, ", ".join(self.fields))

    @classmethod
    def missing_fields(cls, fields):
        return cls('MISSING_FIELDS', frozenset(fields))

    @classmethod
    def extra_fields(cls, fields):
        return cls('EXTRA_FIELDS', frozenset(fields))


# TODO add support for tracking by files and perhaps element index
class ParseSupport:

    def __init__(self):
        self._seen_field_warnings = collections.Counter()

    def mark_field_difference(self, expected_fields, actual_fields, optional=set()):
        missing_fields = expected_fields - actual_fields
        if missing_fields:
            warning = ParseWarning.missing_fields(missing_fields)
            self._seen_field_warnings[warning] += 1

        extra_fields = actual_fields - expected_fields - optional
        if extra_fields:
            warning = ParseWarning.extra_fields(extra_fields)
            self._seen_field_warnings[warning] += 1

    def items(self):
        return self._seen_field_warnings.items()

    def as_dict(self):
        return dict(self._seen_field_warnings)
