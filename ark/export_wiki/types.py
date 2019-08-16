from itertools import repeat
from typing import Mapping

from ue.properties import ArrayProperty, ObjectProperty
from ue.proxy import *

__all__ = [
    'WORLD_SETTINGS_EXPORTED_PROPERTIES',
    'ZONE_MANAGER_EXPORTED_PROPERTIES',
    'BIOME_VOLUME_EXPORTED_PROPERTIES',
    'SUPPLY_DROP_EXPORTED_PROPERTIES',
    'PrimalWorldSettings',
    'NPCZoneManager',
    'BiomeZoneVolume',
    'SupplyCrateSpawningVolume'
]

WORLD_SETTINGS_EXPORTED_PROPERTIES = {
    'OverrideDifficultyMax': 'difficultyMax',
    'OverrideWeaponMapTextureEmpty': 'heldMapEmpty',
    'OverrideWeaponMapTextureFilled': 'heldMap',
    'OverrideUIMapTextureEmpty': 'mapEmpty',
    'OverrideUIMapTextureFilled': 'bigMap',
    'OverrideUIMapTextureSmall': 'smallMap',
}

ZONE_MANAGER_EXPORTED_PROPERTIES = {
    'NPCSpawnEntriesContainerObject': 'spawnGroup',
    'MinDesiredNumberOfNPC': 'MinDesiredNumberOfNPC',
    'bNeverSpawnInWater': 'bNeverSpawnInWater',
    'bForceUntameable': 'bForceUntameable',
}

BIOME_VOLUME_EXPORTED_PROPERTIES = {
    'BiomeZoneName': 'BiomeZoneName',
    'BiomeZonePriority': 'BiomeZonePriority',
    'bIsOutside': 'bIsOutside',
    'bPreventCrops': 'bPreventCrops',

    'FinalTemperatureMultiplier': 'FinalTemperatureMultiplier',
    'FinalTemperatureExponent': 'FinalTemperatureExponent',
    'FinalTemperatureAddition': 'FinalTemperatureAddition',
    
    'PreOffsetTemperatureMultiplier': 'PreOffsetTemperatureMultiplier',
    'PreOffsetTemperatureExponent': 'PreOffsetTemperatureExponent',
    'PreOffsetTemperatureAddition': 'PreOffsetTemperatureAddition',
    
    'AboveTemperatureOffsetThreshold': 'AboveTemperatureOffsetThreshold',
    'AboveTemperatureOffsetMultiplier': 'AboveTemperatureOffsetMultiplier',
    'AboveTemperatureOffsetExponent': 'AboveTemperatureOffsetExponent',
    
    'BelowTemperatureOffsetThreshold': 'BelowTemperatureOffsetThreshold',
    'BelowTemperatureOffsetMultiplier': 'BelowTemperatureOffsetMultiplier',
    'BelowTemperatureOffsetExponent': 'BelowTemperatureOffsetExponent',

    'AbsoluteTemperatureOverride': 'AbsoluteTemperatureOverride',
    'AbsoluteMaxTemperature': 'AbsoluteMaxTemperature',
    'AbsoluteMinTemperature': 'AbsoluteMinTemperature',

    'AbsoluteWindOverride': 'AbsoluteWindOverride',

    'PreOffsetWindMultiplier': 'PreOffsetWindMultiplier',
    'PreOffsetWindExponent': 'PreOffsetWindExponent',
    'PreOffsetWindAddition': 'PreOffsetWindAddition',

    'AboveWindOffsetThreshold': 'AboveWindOffsetThreshold',
    'AboveWindOffsetMultiplier': 'AboveWindOffsetMultiplier',
    'AboveWindOffsetExponent': 'AboveWindOffsetExponent',

    'BelowWindOffsetThreshold': 'BelowWindOffsetThreshold',
    'BelowWindOffsetMultiplier': 'BelowWindOffsetMultiplier',
    'BelowWindOffsetExponent': 'BelowWindOffsetExponent',

    'FinalWindMultiplier': 'FinalWindMultiplier',
    'FinalWindExponent': 'FinalWindExponent',
    'FinalWindAddition': 'FinalWindAddition'
}

SUPPLY_DROP_EXPORTED_PROPERTIES = {
    'MaxNumCrates': 'maxNumCrates',
    'DelayBeforeFirstCrate': 'delayBeforeFirstCrate',
    'MaxDelayBeforeFirstCrate': 'maxDelayBeforeFirstCrate',
    'IntervalBetweenCrateSpawns': 'intervalBetweenCrateSpawns',
    'MaxIntervalBetweenCrateSpawns': 'maxIntervalBetweenCrateSpawns',
    'IntervalBetweenMaxedCrateSpawns': 'intervalBetweenMaxedCrateSpawns',
    'MaxIntervalBetweenMaxedCrateSpawns': 'maxIntervalBetweenMaxedCrateSpawns',
    'SP_IntervalBetweenCrateSpawns': 'SP_IntervalBetweenCrateSpawns',
    'SP_MaxIntervalBetweenCrateSpawns': 'SP_MaxIntervalBetweenCrateSpawns',
    'SP_IntervalBetweenMaxedCrateSpawns': 'SP_IntervalBetweenMaxedCrateSpawns',
    'SP_MaxIntervalBetweenMaxedCrateSpawns': 'SP_MaxIntervalBetweenMaxedCrateSpawns',
    'MinTimeBetweenCrateSpawnsAtSamePoint': 'minTimeBetweenCrateSpawnsAtSamePoint',
}


class PrimalWorldSettings(UEProxyStructure, uetype='/Script/ShooterGame.PrimalWorldSettings'):
    # DevKit Verified
    LatitudeOrigin = uefloats(400_000.0)
    LongitudeOrigin = uefloats(400_000.0)
    LatitudeScale = uefloats(800.0)
    LongitudeScale = uefloats(800.0)

    # DevKit Unverified
    Title = uestrings('')
    OverrideDifficultyMax = uefloats(1)
    OverrideWeaponMapTextureEmpty = uestrings('')
    OverrideWeaponMapTextureFilled = uestrings('')
    OverrideUIMapTextureEmpty = uestrings('')
    OverrideUIMapTextureFilled = uestrings('')
    OverrideUIMapTextureSmall = uestrings('')
    OverrideWeaponMapTextureEmpty = uestrings('')
    OverrideWeaponMapTextureEmpty = uestrings('')
    
    NPCRandomSpawnClassWeights: Mapping[int, ArrayProperty]


class NPCZoneManager(UEProxyStructure, uetype='/Script/ShooterGame.NPCZoneManager'):
    # DevKit Verified
    bEnabled = uebools(True)
    MinDesiredNumberOfNPC = ueints(-1)
    bNeverSpawnInWater = uebools(False)
    bForceUntameable = uebools(False)

    # DevKit Unverified

    NPCSpawnEntriesContainerObject: Mapping[int, ObjectProperty]
    LinkedZoneVolumes: Mapping[int, ArrayProperty]
    LinkedZoneSpawnVolumeEntries: Mapping[int, ArrayProperty]
    SpawnPointOverrides: Mapping[int, ArrayProperty]


class BiomeZoneVolume(UEProxyStructure, uetype='/Script/ShooterGame.BiomeZoneVolume'):
    # DevKit Verified
    BiomeZoneName = uestrings('') # Should be None.
    BiomeZonePriority = ueints(0)
    bHidden = uebools(False)
    bIsOutside = uebools(True)
    bPreventCrops = uebools(False)

    FinalTemperatureMultiplier = uefloats(1.0)
    FinalTemperatureExponent = uefloats(1.0)
    FinalTemperatureAddition = uefloats(0)

    PreOffsetTemperatureMultiplier = uefloats(1.0)
    PreOffsetTemperatureExponent = uefloats(1.0)
    PreOffsetTemperatureAddition = uefloats(0)

    AboveTemperatureOffsetThreshold = uefloats(1_000_000.0)
    AboveTemperatureOffsetMultiplier = uefloats(1.0)
    AboveTemperatureOffsetExponent = uefloats(1.0)

    BelowTemperatureOffsetThreshold = uefloats(-1_000_000.0)
    BelowTemperatureOffsetMultiplier = uefloats(1.0)
    BelowTemperatureOffsetExponent = uefloats(1.0)

    AbsoluteTemperatureOverride = uefloats(-1_000_000.0)
    AbsoluteMaxTemperature = uefloats(70.0)
    AbsoluteMinTemperature = uefloats(-999.0)

    AbsoluteWindOverride = uefloats(-1_000_000.0)

    PreOffsetWindMultiplier = uefloats(1.0)
    PreOffsetWindExponent = uefloats(1.0)
    PreOffsetWindAddition = uefloats(0.0)
    
    AboveWindOffsetThreshold = uefloats(1_000_000.0)
    AboveWindOffsetMultiplier = uefloats(1.0)
    AboveWindOffsetExponent = uefloats(1.0)

    BelowWindOffsetThreshold = uefloats(-1_000_000.0)
    BelowWindOffsetMultiplier = uefloats(1.0)
    BelowWindOffsetExponent = uefloats(1.0)

    FinalWindMultiplier = uefloats(0.0)
    FinalWindExponent = uefloats(1.0)
    FinalWindAddition = uefloats(0.0)

    # DevKit Unverified


class SupplyCrateSpawningVolume(UEProxyStructure, uetype='/Script/ShooterGame.SupplyCrateSpawningVolume'):
    # DevKit Verified
    bHidden = uebools(False) # Devkit calls this bIsEnabled
    MaxNumCrates = ueints(0)
    DelayBeforeFirstCrate = uefloats(0)
    MaxDelayBeforeFirstCrate = uefloats(0)
    IntervalBetweenCrateSpawns = uefloats(0)
    MaxIntervalBetweenCrateSpawns = uefloats(0)
    IntervalBetweenMaxedCrateSpawns = uefloats(0)
    MaxIntervalBetweenMaxedCrateSpawns = uefloats(0)
    SP_IntervalBetweenCrateSpawns = uefloats(0)
    SP_MaxIntervalBetweenCrateSpawns = uefloats(0)
    SP_IntervalBetweenMaxedCrateSpawns = uefloats(0)
    SP_MaxIntervalBetweenMaxedCrateSpawns = uefloats(0)
    MinTimeBetweenCrateSpawnsAtSamePoint = uefloats(0)

    # DevKit Unverified

    LinkedSupplyCrateEntries: Mapping[int, ArrayProperty]
    LinkedSpawnPointEntries: Mapping[int, ArrayProperty]
