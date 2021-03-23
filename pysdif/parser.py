# pysdif - parser of USS Swimming Data Interchange Format for Python
# Copyright (C) 2021  Joseph Geis
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

from collections import defaultdict
from pathlib import Path
from typing import Optional, Union

import chardet

from pysdif.codes import FileType
from pysdif.errors import ParserException
from pysdif.file import File
from pysdif.meet import Meet
from pysdif.util import parse_date


class Parser(object):
    @staticmethod
    def assert_directive(expected: str, actual: str):
        if not actual == expected:
            raise ParserException.expected_directive(expected, actual)

    def parse_A0(self):
        data = self._lines[self.line]

        directive = data[0:2]
        Parser.assert_directive("A0", directive)

        # TODO: assert 1 per file

        if self.file:
            raise ParserException("File already instantiated.")

        organization_type = data[2]

        version = data[3:11]

        file_type = FileType(data[11:13])

        software_name = data[43:63].strip()
        software_version = data[63:73].strip()
        contact_name = data[73:93].strip()
        contact_phone = data[93:105].strip()
        creation_date_code = data[105:113]

        creation_date = parse_date(creation_date_code)

        self.file = File(
            organization_type,
            version,
            file_type,
            software_name,
            software_version,
            contact_name,
            contact_phone,
            creation_date,
        )

    def parse_B1(self):
        data = self._lines[self.line]

        directive = data[0:2]
        Parser.assert_directive("B1", directive)

        # TODO: assert 1 per file

        if self.meet:
            raise ParserException("File already has meet.")

        organization_type = data[2]

        name = data[11:41].strip()

        address_line_one = data[41:63].strip()
        address_line_two = data[63:85].strip()

        address = address_line_one + (
            f"\n{address_line_two}" if address_line_two else ""
        )

        city = data[85:105].strip()
        state = data[105:107]
        postal_code = data[107:117].strip()
        country_code = data[117:120]
        meet_type = data[120]

        start_date_code = data[121:129]
        end_date_code = data[129:137]

        start_date = parse_date(start_date_code)
        end_date = parse_date(end_date_code)

        altitude = data[137:141].strip()
        course = data[149]

        self.meet = Meet(
            organization_type,
            name,
            address,
            city,
            state,
            postal_code,
            country_code,
            meet_type,
            start_date,
            end_date,
            altitude,
            course,
        )

    def parse_Z0(self):
        data = self._lines[self.line]

        directive = data[0:2]
        Parser.assert_directive("Z0", directive)

        organization_type = data[2]
        file_type = data[11:13]
        notes = data[13:43]

        # TODO: Assertions

        self.file.notes = notes

    def parse_file(self) -> File:
        """
        Parses a file from a configured Parser object

        :return: A File object representing the SDIF file
        """

        if self.file:
            return self.file

        parsers = {"A0": self.parse_A0, "B1": self.parse_B1, "Z0": self.parse_Z0}

        self._lines = self.raw_data.splitlines()

        while True:
            if self.line >= len(self._lines):
                raise ParserException(
                    "Unexpected end of file. (Didn't process any Z0 records.)"
                )

            data = self._lines[self.line]

            length = len(data)
            if length != 160:
                raise ParserException(
                    f"Line {self.line + 1} is incorrect length. Expected 162 characters, got {length}."
                )

            directive = data[0:2]

            if self.line == 0:
                self.assert_directive("A0", directive)

            parsers.get(directive, lambda: None)()

            if directive == "Z0":
                break

            self.line += 1

        self.file.meet = self.meet

        return self.file

    @staticmethod
    def from_file(file: Path) -> File:
        parser = Parser()

        with file.open("rb") as f:
            byte_data = f.read()

        byte_data = byte_data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        charset = chardet.detect(byte_data).get("encoding", "utf8")
        parser.raw_data = byte_data.decode(charset)

        return parser.parse_file()

    @staticmethod
    def from_data(data: Union[bytes, str]) -> File:
        parser = Parser()

        if type(data) == bytes:
            byte_data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            charset = chardet.detect(byte_data).get("encoding", "utf8")
            parser.raw_data = byte_data.decode(charset)
        else:
            parser.raw_data = data

        return parser.parse_file()

    def __init__(self):
        self.file_path: Optional[Path] = None
        self.raw_data: str = None
        self._lines = None

        # Parser state
        self.line = 0
        self.directive_counts = defaultdict(lambda: 0)

        self.file: File = None
        self.meet: Optional[Meet] = None
