from typing import *

from ark.export_wiki.consts import KNOWN_KLASS_NAMES
from config import get_global_config
from ue.asset import UAsset
from ue.loader import AssetLoader

__all__ = [
    'SublevelDiscoverer',
]


class ByRawData:
    '''Very fast/cheap method for bulk searching. Over-selects slightly.'''
    def __init__(self, loader: AssetLoader):
        self.loader = loader

    def is_world(self, assetname: str):
        '''Use binary string matching to check if an asset contains data to export.'''
        # Load asset as raw data
        mem = self.loader.load_raw_asset(assetname)

        # Check whether the asset is a world
        if b'World' not in mem.obj:
            return False
        # Check whether the asset has occurrences of names of possibly
        # interesting exports.
        for klass_name in KNOWN_KLASS_NAMES:
            if klass_name.encode() in mem.obj:
                return True

        return False


class ByWorldTileData:
    def __init__(self, loader: AssetLoader):
        self.loader = loader

    def is_sublevel(self, assetname: str):
        if not assetname.startswith('/Game'):
            return False

        asset = self.loader.partially_load_asset(assetname)

        if 'tile_info' in asset.field_values:
            return True

        # partially_load_asset does not cache the result.
        #del self.loader[assetname]
        return False


class SublevelDiscoverer:
    def __init__(self, loader: AssetLoader):
        self.loader = loader
        self.testByRawData = ByRawData(self.loader)
        self.testByTileInfo = ByWorldTileData(self.loader)

        self.global_excludes = tuple(set(get_global_config().optimisation.SearchIgnore))

    def _is_a_world(self, assetname: str) -> bool:
        return self.testByRawData.is_world(assetname) and self.testByTileInfo.is_sublevel(assetname)

    def discover_submaps(self, toplevel_map: UAsset) -> Iterator[str]:
        assert toplevel_map.assetname
        base_path = toplevel_map.assetname.rsplit('/', 1)[0]

        # Scan toplevel's map directory, excluding excludes from config
        for level in self.loader.find_assetnames('.*', base_path, exclude=self.global_excludes, extension='.umap'):
            if self._is_a_world(level):
                yield level