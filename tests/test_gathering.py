from typing import *

import pytest  # type: ignore

from ark.gathering import gather_dcsc_properties
from ark.types import PrimalDinoCharacter, PrimalDinoStatusComponent, PrimalGameData
from ue.gathering import gather_properties
from ue.hierarchy import inherits_from
from ue.proxy import UEProxyStructure

from .common import *


@pytest.mark.requires_game
def test_gather_purloviatest_pgd(loader: AssetLoader, internal_hierarchy, test_hierarchy):  # pylint: disable=unused-argument
    asset = loader[PGD_ASSETNAME]
    assert asset.default_export

    pgd: PrimalGameData = gather_properties(asset.default_export)
    assert isinstance(pgd, UEProxyStructure)
    assert isinstance(pgd, PrimalGameData)

    assert str(pgd.ModName[0]) == 'PurloviaTEST'
    assert str(pgd.ModDescription[0]) == 'Test mod used for Purlovia'


@pytest.mark.requires_game
def test_gather_dodo(loader: AssetLoader, dodos):  # pylint: disable=unused-argument
    dodo = loader.load_class(DODO_CHR)
    dodo_chr: PrimalDinoCharacter = gather_properties(dodo)
    assert isinstance(dodo_chr, UEProxyStructure)
    assert isinstance(dodo_chr, PrimalDinoCharacter)
    assert str(dodo_chr.DescriptiveName[0]) == 'Dodo'


@pytest.mark.requires_game
def test_gather_ab_dodo(loader: AssetLoader, dodos):  # pylint: disable=unused-argument
    # dodo_ab = loader[DODO_AB_CHR].default_export
    dodo_ab = loader.load_class(DODO_AB_CHR)
    assert inherits_from(dodo_ab, DODO_CHR)
    dodo_ab_chr: PrimalDinoCharacter = gather_properties(dodo_ab)
    assert isinstance(dodo_ab_chr, UEProxyStructure)
    assert isinstance(dodo_ab_chr, PrimalDinoCharacter)
    assert str(dodo_ab_chr.DescriptiveName[0]) == 'Aberrant Dodo'
    # TODO: Failing because the properties are in Default__ not the main class!


@pytest.mark.requires_game
def test_gather_dodo_dcsc(loader: AssetLoader, dodos):  # pylint: disable=unused-argument
    dodo = loader.load_class(DODO_CHR)
    dodo_dcsc = gather_dcsc_properties(dodo)
    assert isinstance(dodo_dcsc, UEProxyStructure)
    assert isinstance(dodo_dcsc, PrimalDinoStatusComponent)
    assert dodo_dcsc.MaxStatusValues[0] == 40  # only in Dodo chr
    assert dodo_dcsc.MaxStatusValues[3] == 150  # only in DCSC asset
    assert dodo_dcsc.MaxStatusValues[7] == 50  # in DCSC, then overridden by Dodo


@pytest.mark.requires_game
def test_gather_troodon_dcsc(loader: AssetLoader, troodon):  # pylint: disable=unused-argument
    chr_export = loader.load_class(TROODON_CHR)
    props = gather_dcsc_properties(chr_export)
    assert isinstance(props, UEProxyStructure)
    assert isinstance(props, PrimalDinoStatusComponent)
    assert props.MaxStatusValues[0] == 200  # only in Troodon DCSC asset
    assert props.MaxStatusValues[4] == 200  # in Troodon chr asset
    assert props.MaxStatusValues[7] == 140  # in DCSC, overridden in Troodon DCSC


@pytest.mark.requires_game
def test_gather_troodon_dcsc_alt(loader: AssetLoader, troodon):  # pylint: disable=unused-argument
    chr_export = loader.load_class(TROODON_CHR)
    props = gather_dcsc_properties(chr_export, alt=True)
    assert isinstance(props, UEProxyStructure)
    assert isinstance(props, PrimalDinoStatusComponent)
    assert props.MaxStatusValues[0] == 200  # only in Troodon DCSC asset
    assert props.MaxStatusValues[4] == 100  # was 200 in Troodon chr asset, skipped
    assert props.MaxStatusValues[7] == 140  # in DCSC, overridden in Troodon DCSC
