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
from typing import List, Union

from pysdif.codes import MeetType, Course, OrgType


class Meet(object):
    def __init__(
        self,
        organization_type: Union[OrgType, str] = None,
        name: str = None,
        address: Union[str, List[str]] = None,
        city: str = None,
        state: str = None,
        postal_code: str = None,
        country_code: str = None,
        meet_type: Union[MeetType, str] = None,
        start_date: date = None,
        end_date: date = None,
        altitude: int = None,
        course: Union[Course, str] = None,
    ):
        """
        Stores information about meet results.

        :param organization_type: Organization type
        :param name: Meet name
        :param address: Meet venue street address. Either a string or list of strings (for multiple lines).
        :param city: Meet venue city
        :param state: Meet venue state
        :param postal_code: Meet venue postal code
        :param country_code: Meet venue country
        :param meet_type: Meet type
        :param start_date: Starting date
        :param end_date: Ending date
        :param altitude: Altitude of pool in feet above sea level
        :param course: Course code (i.e. SCM/SCY/LCM)
        """

        self.organization_type = OrgType(organization_type)
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country_code = country_code
        self.meet_type: MeetType = MeetType(meet_type) if meet_type.strip() else None
        self.start_date = start_date
        self.end_date = end_date
        self.altitude = int(altitude)
        self.course: Course = Course(course) if course else None
