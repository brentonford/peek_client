'''
 *
 *  Copyright Synerty Pty Ltd 2013
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by 
 *  Synerty Pty Ltd
 *
 * Website : http://www.synerty.com
 * Support : support@synerty.com
 *
'''
import logging
import os

from jsoncfg.value_mappers import require_integer
from peek_platform.file_config.PeekFileConfigABC import PeekFileConfigABC
from peek_platform.file_config.PeekFileConfigFrontendDirMixin import \
    PeekFileConfigFrontendDirMixin
from peek_platform.file_config.PeekFileConfigOsMixin import PeekFileConfigOsMixin
from peek_platform.file_config.PeekFileConfigPeekServerClientMixin import \
    PeekFileConfigPeekServerClientMixin
from peek_platform.file_config.PeekFileConfigPlatformABC import \
    PeekFileConfigPlatformABC

logger = logging.getLogger(__name__)


class PeekClientConfig(PeekFileConfigABC,
                       PeekFileConfigPeekServerClientMixin,
                       PeekFileConfigPlatformABC,
                       PeekFileConfigOsMixin,
                       PeekFileConfigFrontendDirMixin):
    """
    This class creates a basic client configuration
    """

    import peek_client_fe
    _frontendProjectDir = os.path.dirname(peek_client_fe.__file__)

    @property
    def platformVersion(self):
        import peek_client
        return peek_client.__version__

    ### SERVER SECTION ###
    @property
    def sitePort(self) -> int:
        with self._cfg as c:
            return c.server.port(8000, require_integer)


peekClientConfig = PeekClientConfig()
