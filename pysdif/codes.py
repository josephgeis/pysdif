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

from enum import Enum

from aenum import MultiValueEnum


class OrgType(Enum):
    USS = "1"
    MASTERS = "2"
    NCAA = "3"
    NCAA_D1 = "4"
    NCAA_D2 = "5"
    NCAA_D3 = "6"
    YMCA = "7"
    FINA = "8"
    HS = "9"


class FileType(Enum):
    ENTRIES = "01"
    RESULTS = "02"
    OVC = "03"
    NAT_AG_RECORDS = "04"
    LSC_AG_RECORDS = "05"
    LSC_MOTIVATIONAL = "06"
    NAT_RECORDS = "07"
    TEAM_SELECTION = "08"
    LSC_BEST_TIMES = "09"
    USS_REGISTRATION = "10"
    TOP_16 = "16"
    NON_STANDARD = "20"


class MeetType(Enum):
    INVITATIONAL = "1"
    REGIONAL = "2"
    LSC_CHAMPIONSHIP = "3"
    ZONE = "4"
    ZONE_CHAMPIONSHIP = "5"
    NATIONALS = "6"
    JUNIORS = "7"
    SENIORS = "8"
    DUAL = "9"
    TIME_TRIALS = "0"
    INTERNATIONAL = "A"
    OPEN = "B"
    LEAGUE = "C"


class Sex(Enum):
    MALE = "M"
    FEMALE = "F"


class EventSex(Enum):
    MALE = "M"
    FEMALE = "F"
    MIXED = "X"


class Stroke(Enum):
    FREE = "1"
    BACK = "2"
    BREAST = "3"
    FLY = "4"
    IM = "5"
    R_FREE = "6"
    R_MEDLEY = "7"


class Course(MultiValueEnum):
    SCM = "M", "1"
    SCY = "Y", "2"
    LCM = "L", "3"
    DQ = "X"


class TimeCode(Enum):
    NT = "NT"
    NS = "NS"
    DNF = "DNF"
    DQ = "DQ"
    SCRATCH = "SCR"


class RelayLeg(Enum):
    NS = "0"
    FIRST = "1"
    SECOND = "2"
    THIRD = "3"
    FOURTH = "4"
    ANCHOR = "4"
    ALTERNATE = "A"
