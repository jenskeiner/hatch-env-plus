import os

from hatchling.version.source.plugin.interface import VersionSourceInterface


class EnvironmentVariableVersionSource(VersionSourceInterface):
    PLUGIN_NAME = 'env+'

    def get_version_data(self) -> dict:
        variable = self.config.get('variable', 'PACKAGE_VERSION')
        fallback = self.config.get('fallback', '0.0.0')
        version = os.environ.get(variable, fallback)
        return {'version': version}
