from itertools import repeat
from typing import Mapping

from ue.properties import ArrayProperty, LinearColor, ObjectProperty
from ue.proxy import *

STAT_COUNT = 12
COLOR_REGION_COUNT = 6

PDSC_CLS = '/Script/ShooterGame.PrimalDinoStatusComponent'
PDC_CLS = '/Script/ShooterGame.PrimalDinoCharacter'
PGD_CLS = '/Script/ShooterGame.PrimalGameData'
PRIMAL_CHR_CLS = '/Script/ShooterGame.PrimalCharacter'
PRIMAL_ITEM_CLS = '/Script/ShooterGame.PrimalItem'
PRIMAL_ITEM_DYE_CLS = '/Script/ShooterGame.PrimalItem_Dye'
PRIMAL_DINO_SETTINGS_CLS = '/Script/ShooterGame.PrimalDinoSettings'
SHOOTER_CHR_MOVEMENT_CLS = '/Script/ShooterGame.ShooterCharacterMovement'

DCSC_CLS = '/Game/PrimalEarth/CoreBlueprints/DinoCharacterStatusComponent_BP.DinoCharacterStatusComponent_BP_C'
DINO_CHR_CLS = '/Game/PrimalEarth/CoreBlueprints/Dino_Character_BP.Dino_Character_BP_C'

COREMEDIA_PGD_PKG = '/Game/PrimalEarth/CoreBlueprints/COREMEDIA_PrimalGameData_BP'


class PrimalDinoStatusComponent(UEProxyStructure, uetype=PDSC_CLS):
    # DevKit Verified
    AmountMaxGainedPerLevelUpValue = uefloats(*repeat(0, STAT_COUNT))
    AmountMaxGainedPerLevelUpValueTamed = uefloats(*repeat(0, STAT_COUNT))
    BaseFoodConsumptionRate = uefloats(-0.025000)  # TODO: needs raw data
    bCanSuffocate = uebools(True)
    bCanSuffocateIfTamed = uebools(False)
    bForceGainOxygen = uebools(False)
    CanLevelUpValue = uefloats(*repeat(0, STAT_COUNT))
    DinoMaxStatAddMultiplierImprinting = uefloats(0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0, 0)
    DontUseValue = uefloats(*repeat(0, STAT_COUNT))
    ExtraTamedHealthMultiplier = uefloats(1.35)  # TODO: needs raw data
    KnockedOutTorpidityRecoveryRateMultiplier = uefloats(3.0)
    MaxStatusValues = uefloats(100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0)
    ProneWaterFoodConsumptionMultiplier = uefloats(1.0)
    RecoveryRateStatusValue = uefloats(100.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    TamedBaseHealthMultiplier = uefloats(1.0)
    TamingMaxStatAdditions = uefloats(*repeat(0, STAT_COUNT))
    TamingMaxStatMultipliers = uefloats(*repeat(0, STAT_COUNT))
    TheMaxTorporIncreasePerBaseLevel = uefloats(0.06)  # TODO: needs raw data
    WakingTameFoodConsumptionRateMultiplier = uefloats(2.0)

    # DevKit Unverified


class DinoCharacterStatusComponent(PrimalDinoStatusComponent, uetype=DCSC_CLS):
    pass


class PrimalDinoCharacter(UEProxyStructure, uetype=PDC_CLS):
    # DevKit Verified
    BabyAgeSpeed = uefloats(0.033)  # TODO: needs raw data
    BabyGestationSpeed = uefloats(0.000035)  # TODO: needs raw data
    bCanBeTamed = uebools(True)
    bCanBeTorpid = uebools(True)
    bCanHaveBaby = uebools(False)
    bIgnoreAllImmobilizationTraps = uebools(False)
    bIsBossDino = uebools(False)
    bIsCorrupted = uebools(False)
    bIsWaterDino = uebools(False)
    bPreventImmobilization = uebools(False)
    bPreventSleepingTame = uebools(False)
    bSupportWakingTame = uebools(False)
    bUseBabyGestation = uebools(False)
    bUseColorization = uebools(False)
    CustomTag = uestrings('')  # NameProperty (Default: None)
    DescriptiveName = uestrings('')  # StringProperty (Default: 'PrimalCharacter')
    DinoNameTag = uestrings('')  # NameProperty (Default: None)
    DragWeight = uefloats(35.0)
    ExtraBabyAgeSpeedMultiplier = uefloats(1.0)
    ExtraBabyGestationSpeedMultiplier = uefloats(1.0)
    ExtraTamedBaseHealthMultiplier = uefloats(1.0)
    NewFemaleMaxTimeBetweenMating = uefloats(172800.0)
    NewFemaleMinTimeBetweenMating = uefloats(64800.0)
    PreventColorizationRegions = uebytes(*repeat(0, COLOR_REGION_COUNT))
    RequiredTameAffinity = uefloats(100)
    RequiredTameAffinityPerBaseLevel = uefloats(5.0)
    TameIneffectivenessByAffinity = uefloats(20)
    WakingTameFoodAffinityMultiplier = uefloats(1.6)  # TODO: needs raw data
    WakingTameFoodIncreaseMultiplier = uefloats(1.0)

    RandomColorSetsMale: Mapping[int, ObjectProperty]  # = 'None'
    RandomColorSetsFemale: Mapping[int, ObjectProperty]  # = 'None'
    FertilizedEggItemsToSpawn: Mapping[int, ArrayProperty]  # = []
    BoneDamageAdjusters: Mapping[int, ArrayProperty]  # = []

    # DevKit Unverified


class ShooterCharacterMovement(UEProxyStructure, uetype=SHOOTER_CHR_MOVEMENT_CLS):
    # DevKit Verified
    Mass = uefloats(100.0)

    # DevKit Unverified


class PrimalGameData(UEProxyStructure, uetype=PGD_CLS):
    # DevKit Verified
    ModDescription = uestrings('')
    ModName = uestrings('')

    ColorDefinitions: Mapping[int, ArrayProperty]  # = []
    MasterDyeList: Mapping[int, ArrayProperty]  # = []

    # DevKit Unverified


class PrimalItem(UEProxyStructure, uetype=PRIMAL_ITEM_CLS):
    # DevKit Verified
    bSupportDragOntoOtherItem = uebools(False)
    DescriptiveNameBase = uestrings('')
    EggLoseDurabilityPerSecond = uefloats(1.0)
    EggMaxTemperature = uefloats(30.0)
    EggMinTemperature = uefloats(15.0)
    ExtraEggLoseDurabilityPerSecondMultiplier = uefloats(1.0)
    ItemDescription = uestrings('')

    BaseCraftingResourceRequirements: Mapping[int, ArrayProperty]  # = []
    UseItemAddCharacterStatusValues: Mapping[int, ArrayProperty]  # = []

    # DevKit Unverified


class PrimalItem_Dye(PrimalItem, uetype=PRIMAL_ITEM_DYE_CLS):
    bSupportDragOntoOtherItem = uebools(True)
    # DevKit Verified
    DyeColor: Mapping[int, LinearColor]  # = (0.0, 0.0, 0.0, 0.0)
    DyeUISceneTemplate: Mapping[int, ObjectProperty]  # = None

    # DevKit Unverified


class PrimalDinoSettings(UEProxyStructure, uetype=PRIMAL_DINO_SETTINGS_CLS):
    # DevKit Verified
    DinoFoodTypeName = uestrings('')
    TamingAffinityNoFoodDecreasePercentageSpeed = uefloats(0.0075)  # TODO: needs raw data
    WakingTameDisplayItemName = uebools(False)

    BaseDamageTypeAdjusters: Mapping[int, ArrayProperty]  # = []
    ExtraDamageTypeAdjusters: Mapping[int, ArrayProperty]  # = []
    ExtraFoodEffectivenessMultipliers: Mapping[int, ArrayProperty]  # = []
    FoodEffectivenessMultipliers: Mapping[int, ArrayProperty]  # = []
    DinoFoodTypeImage: Mapping[int, ObjectProperty]  # = None

    # DevKit Unverified
