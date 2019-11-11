from functools import lru_cache
from typing import *
from typing import cast

from ark.defaults import *

from .asset import ExportTableItem
from .base import UEBase
from .consts import BLUEPRINT_GENERATED_CLASS_CLS
from .hierarchy import find_parent_classes
from .loader import AssetLoader
from .properties import ObjectProperty
from .proxy import UEProxyStructure, get_proxy_for_type
from .tree import discover_inheritance_chain, is_fullname_an_asset

__all__ = [
    'gather_properties',
    'get_default_props_for_class',
]

Tproxy = TypeVar('Tproxy', bound=UEProxyStructure)


def gather_properties(export: Union[ExportTableItem, ObjectProperty]) -> Tproxy:
    '''Collect properties from an export, respecting the inheritance tree.'''
    if isinstance(export, ObjectProperty):
        return gather_properties(cast(ExportTableItem, export.value))

    if not isinstance(export, ExportTableItem):
        raise TypeError("ExportTableItem required")

    assert export.fullname
    assert export.asset and export.asset.loader
    loader = export.asset.loader
    proxy = get_proxy_for_type(export.fullname, loader)

    for fullname in reversed(list(find_parent_classes(export, include_self=True))):
        if not is_fullname_an_asset(fullname):
            continue  # Defaults are already in proxy - skip

        props = get_default_props_for_class(fullname, loader)
        proxy.update(props)

    return cast(Tproxy, proxy)


def get_default_props_for_class(klass: Union[str, ExportTableItem], loader: AssetLoader) -> Mapping[str, Mapping[int, UEBase]]:
    '''Fetch properties for an export.

    This reads the properties directly for bare classes, or finds the appropriate
    Default__ prefixed export for BlueprintGeneratedClasses.'''
    cls: ExportTableItem
    if isinstance(klass, str):
        cls = loader.load_class(klass)
    elif isinstance(klass, ExportTableItem):
        cls = klass
    else:
        raise TypeError("Must supply an export or fullname of an export")

    # Special-case all BP-generated classes - redirect to the Default__ export's properties
    if cls.klass and cls.klass.value.fullname == BLUEPRINT_GENERATED_CLASS_CLS:
        # Check the asset's default_export as this is usually the correct export
        if cls.asset.default_export and cls.asset.default_export.klass and cls.asset.default_export.klass.value is cls:
            return cls.asset.default_export.properties.as_dict()

        # Find the Default__ export for this class and return its properties
        for export in cls.asset.exports:
            if str(export.name).startswith('Default__') and export.klass and export.klass.value is cls:
                return export.properties.as_dict()

        raise RuntimeError("Unable to find Default__ property export for: " + str(cls))

    return cls.properties.as_dict()
