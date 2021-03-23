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

import datetime
from typing import Union

from pysdif.codes import OrgType, Sex, Stroke, EventSex


class Splash(object):
    def __init__(
        self,
        organization_type: OrgType = None,
        name: str = None,
        uss_number: str = None,
        attached: bool = None,
        citizenship: str = None,
        birthdate: datetime.date = None,
        age_class: Union[int, str] = None,
        sex: Sex = None,
        event_sex: EventSex = None,
        stroke: Stroke = None,
        event_number: str = None,
        event_lower_age: Union[int, str] = None,
        event_upper_age: Union[int, str] = None,
        date: datetime.date = None,
        seed_time: str = None,
        prelim_time: str = None,
        swimoff_time: str = None,
        finals_time: str = None,
        prelim_heat: Union[int, str] = None,
        prelim_lane: Union[int, str] = None,
        finals_heat: Union[int, str] = None,
        finals_lane: Union[int, str] = None,
        prelim_place: Union[int, str] = None,
        finals_place: Union[int, str] = None,
        points: Union[float, str] = None,
        time_min_class: str = None,  # TODO: Implement in codes.py
        time_max_class: str = None,
        flight: str = None,
    ):
        # TODO: Implement
        pass
