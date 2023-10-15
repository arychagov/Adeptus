import functools
import json
import pathlib
import sys
from xml.etree.ElementTree import Element, tostring

from google.cloud import translate
from google.oauth2 import service_account

REFERENCE_LANGUAGE = 'English'
TARGET_LANGUAGE = 'Russian'


@functools.cache
def translation_service_client():
    credentials = service_account.Credentials.from_service_account_info(_get_credentials_json())
    return translate.TranslationServiceClient(
        credentials=credentials
    )


def translate_text(text, project_id="adeptus-translation"):
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = translation_service_client().translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "ru",
        }
    )

    for translation in response.translations:
        return translation.translated_text


def _get_languages_dir():
    project_dir = pathlib.Path(__file__).parent.resolve()
    return project_dir.joinpath('Mod', 'Data', 'Core', 'Languages')


def _get_credentials_json():
    project_dir = pathlib.Path(__file__).parent.resolve()
    with open(project_dir.joinpath('credentials.json'), 'r') as credentials:
        return json.loads('\n'.join(credentials.readlines()))


def _get_reference_dir():
    return _get_languages_dir().joinpath(REFERENCE_LANGUAGE)


def _read_entries(file_path: pathlib.Path):
    with open(file_path, 'r') as _in:
        lines = _in.readlines()

    result = {}
    for i in range(len(lines)):
        line = lines[i]
        if line.strip().startswith('<entry'):
            name_start = line.index('"') + 1
            name_end = line.index('"', name_start)
            name = line[name_start:name_end]
            value_start = lines[i + 1].index('"') + 1
            value_end = lines[i + 1].index('"', value_start) + 1
            value = lines[i + 1][value_start:value_end]
            result[name] = value
            i += 1
        i += 1

    return result


def _write_entries(file_path: pathlib.Path, entries: dict):
    root = Element('language')
    for name, value in entries.items():
        child = Element('entry')
        child.attrib['name'] = name
        child.attrib['value'] = value
        root.append(child)

    with open(file_path, 'w') as out:
        out.write(tostring(root, encoding='UTF-8').decode())


def main():
    to_translate_files = (f for f in pathlib.Path(_get_reference_dir()).iterdir() if f.is_file())
    for to_translate_file in to_translate_files:
        print(f'Translating {to_translate_file}')
        entries = _read_entries(to_translate_file)
        print(f'Entries: {len(entries)}')
        translated_entries = {name: translate_text(value) for name, value in entries.items()}
        _write_entries(_get_languages_dir().joinpath(TARGET_LANGUAGE, to_translate_file.name), translated_entries)


if __name__ == '__main__':
    sys.exit(main())
