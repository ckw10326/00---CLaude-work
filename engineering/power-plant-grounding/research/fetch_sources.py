from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, requests

ROOT = Path(__file__).resolve().parent
SOURCES = {
    'NIOSH_2009_113.pdf': 'https://www.cdc.gov/niosh/docs/2009-113/pdfs/2009-113.pdf',
    'DOE_HDBK_1092_2013.pdf': 'https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1092-2013.pdf',
    'DOE_Electrical_Science_Vol3.pdf': 'https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1011-92_VOL3.pdf',
    'USBR_FIST_4_7_2023.pdf': 'https://www.usbr.gov/power/data/fist/FIST_4-7_%288-2023%29.pdf',
    'EPRI_3002013162.pdf': 'https://restservice.epri.com/publicdownload/000000003002013162/0/Product',
}

def fetch(item):
    name, url = item
    path = ROOT / name
    try:
        if not path.exists():
            r = requests.get(url, timeout=45)
            r.raise_for_status()
            if not r.content.startswith(b'%PDF'):
                raise ValueError('Response is not PDF')
            path.write_bytes(r.content)
        data = path.read_bytes()
        return {'file': name, 'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'retrieved': '2026-10-31'}
    except Exception as e:
        return {'file': name, 'url': url, 'error': str(e)}

if __name__ == '__main__':
    results = list(ThreadPoolExecutor(max_workers=5).map(fetch, SOURCES.items()))
    (ROOT / 'source_manifest.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(results, ensure_ascii=False, indent=2))
