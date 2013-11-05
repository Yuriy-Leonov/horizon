# Copyright 2013 Mirantis Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from django.utils.translation import ugettext_lazy as _
from horizon import exceptions


BRONZE = 'bronze'
GOLD = 'gold'
PLATINUM = 'platinum'
qos_levels = [BRONZE, GOLD, PLATINUM]


def check_valid_qos_level_for_quota(qos_level_index, request):
    try:
        qos_levels[qos_level_index - 1]
    except IndexError:
        raise exceptions.handle(request, _('Modified project information and '
                                           'members, but unable to modify '
                                           'project quotas.'))
