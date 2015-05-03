# TODO add support for tracking by files and perhaps element index
class ParseSupport:

    def __init__(self):
        self.seen_field_warnings = {}

    def mark_field_difference(self, expected_fields, actual_fields, optional=set()):
        missing_fields = expected_fields - actual_fields
        if missing_fields:
            message = 'missing fields: {}'.format(", ".join(missing_fields))
            if message not in self.seen_field_warnings:
                self.seen_field_warnings[message] = 0
            self.seen_field_warnings[message] += 1
        extra_fields = actual_fields - expected_fields - optional
        if extra_fields:
            message = 'extra fields: {}'.format(", ".join(extra_fields))
            if message not in self.seen_field_warnings:
                self.seen_field_warnings[message] = 0
            self.seen_field_warnings[message] += 1
