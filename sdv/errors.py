# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

class ValidationError(Exception):
    """Base Exception for all validator-specific exceptions. This is used
    directly by some modules as a generic Exception.

    """
    pass


class UnknownNamespaceError(ValidationError):
    """Raised when an unknown namespace is encountered in a function."""
    pass


class UnknownVocabularyError(ValidationError):
    """Raised when an unknown controlled vocabulary name is discovered
    during best practice validation."""
    pass


class XMLSchemaIncludeError(ValidationError):
    """Raised when errors occur during the processing of ``xs:include``
    directives found within schema documents.

    """
    pass


class XMLSchemaImportError(ValidationError):
    """Raised when errors occur when generating ``xs:import`` directives for
    the "uber" schema, used to validate XML instance documents.

    """
    pass


class UnknownSTIXVersionError(ValidationError):
    """Raised when no STIX version information can be found in an instance
    document and no version information was provided to a method which
    requires version information.

    """
    pass


class InvalidSTIXVersionError(ValidationError):
    """Raised when an invalid version of STIX is discovered within an instance
    document or is passed into a method which depends on STIX version
    information.

    Args:
        message: The error message.
        expected: A version or list of expected versions.
        found: The STIX version that was declared for an instance document or
            found within an instance document.

    """
    def __init__(self, message, expected=None, found=None):
        super(InvalidSTIXVersionError, self).__init__(message)
        self.expected = expected
        self.found = found


class ProfileParseError(ValidationError):
    """Raised when an error occurs during the parse or initialization
    of a STIX profile document.

    """
    pass