import sys
import subprocess
import os

from config import iu_config
from config import pdf_corpus_config

def pass_rate_by_check_return_code():
    passed_pdfs = 0
    total_pdfs = 0
    cmd = iu_config['sut_path'] + iu_config['sut_arguments'] + "./citation.cff"
    # cmd = 'D:/afl/mupdf/platform/win32/Release/mutool.exe clean -difa D:/iust_pdf_corpus/corpus_merged/pdftc_mozilla_0333.pdf'
    
    
    x = subprocess.run(cmd, shell=True)

    print(x.stderr)
    # print(20*'---')
    print(x.returncode)

    total_pdfs += 1
    if x.returncode == 0:
        passed_pdfs += 1
    # input()

    print('passed_pdfs: %s out of %s' % (passed_pdfs, total_pdfs))
    print('pass_rate percentage:', (100 * passed_pdfs)/total_pdfs)

pass_rate_by_check_return_code()

def pass_rate_by_check_output_size():
    passed_pdfs = 0
    total_pdfs = 0
    for filename in os.listdir(pdf_corpus_config['corpus_merged']):
        cmd = iu_config['sut_path'] + iu_config['sut_arguments'] + pdf_corpus_config['corpus_merged'] + filename
        # cmd = 'D:/afl/mupdf/platform/win32/Release/mutool.exe clean -difa D:/iust_pdf_corpus/corpus_merged/pdftc_mozilla_0333.pdf'
        print(cmd)
        x = subprocess.run(cmd,check=False, shell=True)
        total_pdfs += 1
        print(os.path.getsize('out.pdf'))
        if os.path.getsize('out.pdf') > 0:
            passed_pdfs += 1
        # if x.stderr is None:
        #     passed_pdfs += 1
        print(x.stderr)
        input()

    print('passed_pdfs: %s out of %s' % (passed_pdfs, total_pdfs))
    print('pass_rate percentage:', (100 * passed_pdfs) / total_pdfs)
