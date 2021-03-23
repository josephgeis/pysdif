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

from datetime import date
from typing import Union, List

from pysdif.codes import FileType, OrgType
from pysdif.meet import Meet


class File(object):
    def __init__(
        self,
        organization_type: Union[OrgType, str] = None,
        version: str = None,
        file_type: FileType = None,
        software_name: str = None,
        software_version: str = "v3",
        contact_name: str = None,
        contact_phone: str = None,
        creation_date: date = None,
        notes: str = None,
        meet: Meet = None,
        splashes: List = None,
    ):
        """
        Stores information about an SDIF file.

        :param organization_type: Indicates the type of organization that created the file.
        :param version: Version of the SDIF file. Defaults to v3.
        :param file_type: Indicates the type of file.
        :param software_name: Name of the program that created the SDIF file.
        :param software_version: Version of the program that created the file.
        :param contact_name: Name of the person responsible for the SDIF file.
        :param contact_phone: Phone number of the person responsible for the SDIF file.
        :param creation_date: Date the SDIF file was created.
        :param notes: Additional file information.
        """

        self.organization_type = OrgType(organization_type)
        self.version = version
        self.file_type = file_type
        self.software_name = software_name
        self.software_version = software_version
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.creation_date = creation_date
        self.notes = notes

        self.meet = meet
        self.splashes = splashes if splashes else list()
