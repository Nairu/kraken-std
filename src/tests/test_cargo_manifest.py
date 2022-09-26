from pathlib import Path
from pickle import NONE

from kraken.std.cargo.manifest import CargoManifest


def test_cargo_manifest_handles_unknown_fields_correctly():
    manifest = CargoManifest.of(
        Path(""),
        {
            "package": {
                "name": "test",
                "version": "0.1.2",
                "edition": "2021",
                "include": ["test1", "test2"],
                "authors": ["author1", "author2"],
            },
            "bin": [{"name": "bin1", "path": "path"}],
        },
    )

    assert manifest.package is not None
    assert manifest.package.name == "test"
    assert manifest.package.version == "0.1.2"
    assert manifest.package.edition == "2021"

    assert manifest.package.unhandled is not None
    assert len(manifest.package.unhandled) == 2
    assert len(manifest.package.unhandled["include"]) == 2
    assert manifest.package.unhandled["authors"] == ["author1", "author2"]


def test_cargo_manifest_writes_json_correctly():
    input_json = {
        "package": {
            "name": "test",
            "version": "0.1.2",
            "edition": "2021",
            "include": ["test1", "test2"],
            "authors": ["author1", "author2"],
        },
        "bin": [{"name": "bin1", "path": "path"}],
    }

    manifest = CargoManifest.of(Path(""), input_json)
    output_json = manifest.to_json()

    print(input_json)
    print(output_json)

    assert input_json == output_json
