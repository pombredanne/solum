# Copyright 2013 - Noorul Islam K M
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import pecan
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan

from solum.api.controllers import common_types
from solum.api.controllers.v1 import assembly
from solum.api.controllers.v1 import component
from solum.api.controllers.v1 import extension
from solum.api.controllers.v1 import operation
from solum.api.controllers.v1 import sensor
from solum.api.controllers.v1 import service
from solum import version


class Platform(wtypes.Base):
    """Representation of a Platform.

    The Platform resource is the root level resource that refers
    to all the other resources owned by this tenant.
    """

    uri = common_types.Uri
    "Uri to the platform"

    name = wtypes.text
    "The name of the platform"

    description = wtypes.text
    "Description of the platform"

    implementation_version = wtypes.text
    "Version of the platform"

    assemblies = [common_types.Link]
    "List of links to assemblies"

    @classmethod
    def sample(cls):
        return cls(uri='http://example.com/v1',
                   name='solum',
                   description='solum native implementation',
                   implementation_version='2014.1.1',
                   assemblies=[common_types.Link(
                       href='http://example.com:9777/v1/assemblies/x2',
                       target_name='x2')])


class Controller(object):
    """Version 1 API controller root."""

    assemblies = assembly.AssembliesController()
    services = service.ServicesController()
    components = component.ComponentsController()
    extensions = extension.ExtensionsController()
    operations = operation.OperationsController()
    sensors = sensor.SensorsController()

    @wsme_pecan.wsexpose(Platform)
    def index(self):
        host_url = '%s/%s' % (pecan.request.host_url, 'v1')
        return Platform(uri=host_url,
                        name='solum',
                        description='solum native implementation',
                        implementation_version=version.version_string())
