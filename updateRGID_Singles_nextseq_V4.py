# Python 3.6
'''
# Author: Sai Ma
# Date: 11/22/2018
# Objective: Update the RGID of splitATAC bam files
'''
import pysam
import argparse
import subprocess

R1 = {'ATCACGTT': 'R1.01',
      'CGATGTTT': 'R1.02',
      'TTAGGCAT': 'R1.03',
      'TGACCACT': 'R1.04',
      'ACAGTGGT': 'R1.05',
      'GCCAATGT': 'R1.06',
      'CAGATCTG': 'R1.07',
      'ACTTGATG': 'R1.08',
      'GATCAGCG': 'R1.09',
      'TAGCTTGT': 'R1.10',
      'GGCTACAG': 'R1.11',
      'CTTGTACT': 'R1.12',
      'TGGTTGTT': 'R1.13',
      'TCTCGGTT': 'R1.14',
      'TAAGCGTT': 'R1.15',
      'TCCGTCTT': 'R1.16',
      'TGTACCTT': 'R1.17',
      'TTCTGTGT': 'R1.18',
      'TCTGCTGT': 'R1.19',
      'TTGGAGGT': 'R1.20',
      'TCGAGCGT': 'R1.21',
      'TGATACGT': 'R1.22',
      'TGCATAGT': 'R1.23',
      'TTGACTCT': 'R1.24',
      'TGCGATCT': 'R1.25',
      'TTCCTGCT': 'R1.26',
      'TAGTGACT': 'R1.27',
      'TACAGGAT': 'R1.28',
      'TCCTCAAT': 'R1.29',
      'TGTGGTTG': 'R1.30',
      'TACTAGTC': 'R1.31',
      'TTCCATTG': 'R1.32',
      'TCGAAGTG': 'R1.33',
      'TAACGCTG': 'R1.34',
      'TTGGTATG': 'R1.35',
      'TGAACTGG': 'R1.36',
      'TACTTCGG': 'R1.37',
      'TCTCACGG': 'R1.38',
      'TCAGGAGG': 'R1.39',
      'TAAGTTCG': 'R1.40',
      'TCCAGTCG': 'R1.41',
      'TGTATGCG': 'R1.42',
      'TCATTGAG': 'R1.43',
      'TGGCTCAG': 'R1.44',
      'TATGCCAG': 'R1.45',
      'TCAGATTC': 'R1.46',
      'TAGTCTTG': 'R1.47',
      'TTCAGCTC': 'R1.48',
      'TGTCTATC': 'R1.49',
      'TATGTGGC': 'R1.50',
      'TTACTCGC': 'R1.51',
      'TCGTTAGC': 'R1.52',
      'TACCGAGC': 'R1.53',
      'TGTTCTCC': 'R1.54',
      'TTCGCACC': 'R1.55',
      'TTGCGTAC': 'R1.56',
      'TCTACGAC': 'R1.57',
      'TGACAGAC': 'R1.58',
      'TAGAACAC': 'R1.59',
      'TCATCCTA': 'R1.60',
      'TGCTGATA': 'R1.61',
      'TAGACGGA': 'R1.62',
      'TGTGAAGA': 'R1.63',
      'TCTCTTCA': 'R1.64',
      'TTGTTCCA': 'R1.65',
      'TGAAGCCA': 'R1.66',
      'TACCACCA': 'R1.67',
      'TGCGTGAA': 'R1.68',
      'GGTGAGTT': 'R1.69',
      'GATCTCTT': 'R1.70',
      'GTGTCCTT': 'R1.71',
      'GACGGATT': 'R1.72',
      'GCAACATT': 'R1.73',
      'GGTCGTGT': 'R1.74',
      'GAATCTGT': 'R1.75',
      'GTACATCT': 'R1.76',
      'GAGGTGCT': 'R1.77',
      'GCATGGCT': 'R1.78',
      'GTTAGCCT': 'R1.79',
      'GTCGCTAT': 'R1.80',
      'GGAATGAT': 'R1.81',
      'GAGCCAAT': 'R1.82',
      'GCTCCTTG': 'R1.83',
      'GTAAGGTG': 'R1.84',
      'GAGGATGG': 'R1.85',
      'GTTGTCGG': 'R1.86',
      'GGATTAGG': 'R1.87',
      'GATAGAGG': 'R1.88',
      'GTGTGTCG': 'R1.89',
      'GCAATCCG': 'R1.90',
      'GACCTTAG': 'R1.91',
      'GCCTGTTC': 'R1.92',
      'GCACTGTC': 'R1.93',
      'GCTAACTC': 'R1.94',
      'GATTCATC': 'R1.95',
      'GTCTTGGC': 'R1.96'}
R2 = {'ATCACGTT': 'R2.01',
      'CGATGTTT': 'R2.02',
      'TTAGGCAT': 'R2.03',
      'TGACCACT': 'R2.04',
      'ACAGTGGT': 'R2.05',
      'GCCAATGT': 'R2.06',
      'CAGATCTG': 'R2.07',
      'ACTTGATG': 'R2.08',
      'GATCAGCG': 'R2.09',
      'TAGCTTGT': 'R2.10',
      'GGCTACAG': 'R2.11',
      'CTTGTACT': 'R2.12',
      'TGGTTGTT': 'R2.13',
      'TCTCGGTT': 'R2.14',
      'TAAGCGTT': 'R2.15',
      'TCCGTCTT': 'R2.16',
      'TGTACCTT': 'R2.17',
      'TTCTGTGT': 'R2.18',
      'TCTGCTGT': 'R2.19',
      'TTGGAGGT': 'R2.20',
      'TCGAGCGT': 'R2.21',
      'TGATACGT': 'R2.22',
      'TGCATAGT': 'R2.23',
      'TTGACTCT': 'R2.24',
      'TGCGATCT': 'R2.25',
      'TTCCTGCT': 'R2.26',
      'TAGTGACT': 'R2.27',
      'TACAGGAT': 'R2.28',
      'TCCTCAAT': 'R2.29',
      'TGTGGTTG': 'R2.30',
      'TACTAGTC': 'R2.31',
      'TTCCATTG': 'R2.32',
      'TCGAAGTG': 'R2.33',
      'TAACGCTG': 'R2.34',
      'TTGGTATG': 'R2.35',
      'TGAACTGG': 'R2.36',
      'TACTTCGG': 'R2.37',
      'TCTCACGG': 'R2.38',
      'TCAGGAGG': 'R2.39',
      'TAAGTTCG': 'R2.40',
      'TCCAGTCG': 'R2.41',
      'TGTATGCG': 'R2.42',
      'TCATTGAG': 'R2.43',
      'TGGCTCAG': 'R2.44',
      'TATGCCAG': 'R2.45',
      'TCAGATTC': 'R2.46',
      'TAGTCTTG': 'R2.47',
      'TTCAGCTC': 'R2.48',
      'TGTCTATC': 'R2.49',
      'TATGTGGC': 'R2.50',
      'TTACTCGC': 'R2.51',
      'TCGTTAGC': 'R2.52',
      'TACCGAGC': 'R2.53',
      'TGTTCTCC': 'R2.54',
      'TTCGCACC': 'R2.55',
      'TTGCGTAC': 'R2.56',
      'TCTACGAC': 'R2.57',
      'TGACAGAC': 'R2.58',
      'TAGAACAC': 'R2.59',
      'TCATCCTA': 'R2.60',
      'TGCTGATA': 'R2.61',
      'TAGACGGA': 'R2.62',
      'TGTGAAGA': 'R2.63',
      'TCTCTTCA': 'R2.64',
      'TTGTTCCA': 'R2.65',
      'TGAAGCCA': 'R2.66',
      'TACCACCA': 'R2.67',
      'TGCGTGAA': 'R2.68',
      'GGTGAGTT': 'R2.69',
      'GATCTCTT': 'R2.70',
      'GTGTCCTT': 'R2.71',
      'GACGGATT': 'R2.72',
      'GCAACATT': 'R2.73',
      'GGTCGTGT': 'R2.74',
      'GAATCTGT': 'R2.75',
      'GTACATCT': 'R2.76',
      'GAGGTGCT': 'R2.77',
      'GCATGGCT': 'R2.78',
      'GTTAGCCT': 'R2.79',
      'GTCGCTAT': 'R2.80',
      'GGAATGAT': 'R2.81',
      'GAGCCAAT': 'R2.82',
      'GCTCCTTG': 'R2.83',
      'GTAAGGTG': 'R2.84',
      'GAGGATGG': 'R2.85',
      'GTTGTCGG': 'R2.86',
      'GGATTAGG': 'R2.87',
      'GATAGAGG': 'R2.88',
      'GTGTGTCG': 'R2.89',
      'GCAATCCG': 'R2.90',
      'GACCTTAG': 'R2.91',
      'GCCTGTTC': 'R2.92',
      'GCACTGTC': 'R2.93',
      'GCTAACTC': 'R2.94',
      'GATTCATC': 'R2.95',
      'GTCTTGGC': 'R2.96'}
R3 = {'ATCACGTT': 'R3.01',
      'CGATGTTT': 'R3.02',
      'TTAGGCAT': 'R3.03',
      'TGACCACT': 'R3.04',
      'ACAGTGGT': 'R3.05',
      'GCCAATGT': 'R3.06',
      'CAGATCTG': 'R3.07',
      'ACTTGATG': 'R3.08',
      'GATCAGCG': 'R3.09',
      'TAGCTTGT': 'R3.10',
      'GGCTACAG': 'R3.11',
      'CTTGTACT': 'R3.12',
      'TGGTTGTT': 'R3.13',
      'TCTCGGTT': 'R3.14',
      'TAAGCGTT': 'R3.15',
      'TCCGTCTT': 'R3.16',
      'TGTACCTT': 'R3.17',
      'TTCTGTGT': 'R3.18',
      'TCTGCTGT': 'R3.19',
      'TTGGAGGT': 'R3.20',
      'TCGAGCGT': 'R3.21',
      'TGATACGT': 'R3.22',
      'TGCATAGT': 'R3.23',
      'TTGACTCT': 'R3.24',
      'TGCGATCT': 'R3.25',
      'TTCCTGCT': 'R3.26',
      'TAGTGACT': 'R3.27',
      'TACAGGAT': 'R3.28',
      'TCCTCAAT': 'R3.29',
      'TGTGGTTG': 'R3.30',
      'TACTAGTC': 'R3.31',
      'TTCCATTG': 'R3.32',
      'TCGAAGTG': 'R3.33',
      'TAACGCTG': 'R3.34',
      'TTGGTATG': 'R3.35',
      'TGAACTGG': 'R3.36',
      'TACTTCGG': 'R3.37',
      'TCTCACGG': 'R3.38',
      'TCAGGAGG': 'R3.39',
      'TAAGTTCG': 'R3.40',
      'TCCAGTCG': 'R3.41',
      'TGTATGCG': 'R3.42',
      'TCATTGAG': 'R3.43',
      'TGGCTCAG': 'R3.44',
      'TATGCCAG': 'R3.45',
      'TCAGATTC': 'R3.46',
      'TAGTCTTG': 'R3.47',
      'TTCAGCTC': 'R3.48',
      'TGTCTATC': 'R3.49',
      'TATGTGGC': 'R3.50',
      'TTACTCGC': 'R3.51',
      'TCGTTAGC': 'R3.52',
      'TACCGAGC': 'R3.53',
      'TGTTCTCC': 'R3.54',
      'TTCGCACC': 'R3.55',
      'TTGCGTAC': 'R3.56',
      'TCTACGAC': 'R3.57',
      'TGACAGAC': 'R3.58',
      'TAGAACAC': 'R3.59',
      'TCATCCTA': 'R3.60',
      'TGCTGATA': 'R3.61',
      'TAGACGGA': 'R3.62',
      'TGTGAAGA': 'R3.63',
      'TCTCTTCA': 'R3.64',
      'TTGTTCCA': 'R3.65',
      'TGAAGCCA': 'R3.66',
      'TACCACCA': 'R3.67',
      'TGCGTGAA': 'R3.68',
      'GGTGAGTT': 'R3.69',
      'GATCTCTT': 'R3.70',
      'GTGTCCTT': 'R3.71',
      'GACGGATT': 'R3.72',
      'GCAACATT': 'R3.73',
      'GGTCGTGT': 'R3.74',
      'GAATCTGT': 'R3.75',
      'GTACATCT': 'R3.76',
      'GAGGTGCT': 'R3.77',
      'GCATGGCT': 'R3.78',
      'GTTAGCCT': 'R3.79',
      'GTCGCTAT': 'R3.80',
      'GGAATGAT': 'R3.81',
      'GAGCCAAT': 'R3.82',
      'GCTCCTTG': 'R3.83',
      'GTAAGGTG': 'R3.84',
      'GAGGATGG': 'R3.85',
      'GTTGTCGG': 'R3.86',
      'GGATTAGG': 'R3.87',
      'GATAGAGG': 'R3.88',
      'GTGTGTCG': 'R3.89',
      'GCAATCCG': 'R3.90',
      'GACCTTAG': 'R3.91',
      'GCCTGTTC': 'R3.92',
      'GCACTGTC': 'R3.93',
      'GCTAACTC': 'R3.94',
      'GATTCATC': 'R3.95',
      'GTCTTGGC': 'R3.96'}
P5 = {'GCGATCTA': 'P1.01',
      'ATAGAGAG': 'P1.02',
      'AGAGGATA': 'P1.03',
      'TCTACTCT': 'P1.04',
      'CTCCTTAC': 'P1.05',
      'TATGCAGT': 'P1.06',
      'TACTCCTT': 'P1.07',
      'AGGCTTAG': 'P1.08',
      'GATTTCCA': 'P1.09',
      'ATCATGTT': 'P1.10',
      'TTTCATCA': 'P1.11',
      'AGTCCGAC': 'P1.12',
      'GCTAGAAA': 'P1.13',
      'CTTGGTTA': 'P1.14',
      'CGATACAC': 'P1.15',
      'TTGATGGA': 'P1.16',
      'TGCACGAA': 'P1.17',
      'GGCAACCT': 'P1.18',
      'ACATAAGG': 'P1.19',
      'CGTTGCTG': 'P1.20',
      'ATTGAACC': 'P1.21',
      'ACGAATGT': 'P1.22',
      'TGGGAATC': 'P1.23',
      'GCAGTCCG': 'P1.24',
      'GAACGGCT': 'P1.25',
      'GACCCAAT': 'P1.26',
      'AGTATGCA': 'P1.27',
      'CCAAGCCC': 'P1.28',
      'GCCACGTC': 'P1.29',
      'AAATTTGC': 'P1.30',
      'GAGGCTGC': 'P1.31',
      'AACTCGGA': 'P1.32',
      'CTTAATGC': 'P1.33',
      'GTTATCGT': 'P1.34',
      'CCCGCAGG': 'P1.35',
      'AACAATCA': 'P1.36',
      'TCCGTGCC': 'P1.37',
      'GAATGATC': 'P1.38',
      'ATGACCAT': 'P1.39',
      'TTGGTACG': 'P1.40',
      'TAAACTGG': 'P1.41',
      'GGGCCGGT': 'P1.42',
      'ACTTCTAG': 'P1.43',
      'ATCTGGCG': 'P1.44',
      'CCATGTGA': 'P1.45',
      'TCGAGTTC': 'P1.46',
      'AACGGTGG': 'P1.47',
      'GTAACTTA': 'P1.48',
      'CACGTCTC': 'P1.49',
      'TTAGGCAA': 'P1.50',
      'CAAGTTAA': 'P1.51',
      'TGTTAAAG': 'P1.52',
      'GGTCTACG': 'P1.53',
      'CGCAAATA': 'P1.54',
      'TCCTGGAT': 'P1.55',
      'CAGGAACA': 'P1.56',
      'CTGCGCGT': 'P1.57',
      'TCGCCAGA': 'P1.58',
      'TGTAGATT': 'P1.59',
      'GGTCAGTA': 'P1.60',
      'CCCTATCG': 'P1.61',
      'TTCTAAGT': 'P1.62',
      'AGATCTCT': 'P1.63',
      'CCTTCACC': 'P1.64',
      'CATTCGAT': 'P1.65',
      'GCTCTTGA': 'P1.66',
      'ACGTGGGC': 'P1.67',
      'ACCGCCCA': 'P1.68',
      'TCCAAGGG': 'P1.69',
      'ACGGTAAT': 'P1.70',
      'CTCGGACT': 'P1.71',
      'CAACAAGT': 'P1.72',
      'TGTATTAC': 'P1.73',
      'TAGACGCC': 'P1.74',
      'AGCAGCGC': 'P1.75',
      'AATGGCAC': 'P1.76',
      'CATACCTA': 'P1.77',
      'TAGGTGTT': 'P1.78',
      'GTTCGGAG': 'P1.79',
      'TGCCGTTG': 'P1.80',
      'CTACATTG': 'P1.81',
      'GGGTAGCC': 'P1.82',
      'CGGACTTT': 'P1.83',
      'CCGCGGAA': 'P1.84',
      'AAGTGCCT': 'P1.85',
      'CACTGAAG': 'P1.86',
      'CTACCGGC': 'P1.87',
      'GGATTGAA': 'P1.88',
      'GTGTGTGG': 'P1.89',
      'GATAATAT': 'P1.90',
      'TGCTTCGG': 'P1.91',
      'ACCGATAC': 'P1.92'}

def barcodeSet(barcode):
    bases = "ATCGN"
    barcodeSet = set()
    barcodeSet.add(barcode)
    for i, c in enumerate(barcode):
        if c in bases:
            for base in bases:
                if c != base:
                    barcodeSet.add((barcode[:i] + base + barcode[i + 1:]))
                    barcodeSet.add((barcode[1:] + base))
                    barcodeSet.add((base + barcode[:-1]))
    return barcodeSet

def barcodeSetShift2(barcode):
    bases = "ATCGN"
    barcodeSet = set()
    barcodeSet.add(barcode)
    for i, c in enumerate(barcode):
        if c in bases:
            for base in bases:
                if c != base:
                    barcodeSet.add((barcode[:i] + base + barcode[i + 1:]))
                    barcodeSet.add((barcode[1:] + base))
                    barcodeSet.add((base + barcode[:-1]))
#                    barcodeSet.add((barcode[2:] + base + base))
                    barcodeSet.add(("AC" + barcode[:-2]))
    return barcodeSet

# allow 1 mismatch
# and 2 bp shift for R3

def updateRGID(bamfile, outfile, discard, libtype):
#    print("Opening files")
    bam = pysam.AlignmentFile(bamfile, 'rb')
    out = pysam.AlignmentFile(outfile, 'wb', template=bam)
    err = pysam.AlignmentFile(discard, 'wb', template=bam)
#    print("Generate barcode maps")
#    barcodeNames = set()
    r1 = dict()
    r2 = dict()
    r3 = dict()
    p5 = dict()
    for barcode, name in R1.items():
        barcodes = barcodeSet(barcode)
        for bc in barcodes:
            r1[bc] = name
    for barcode, name in R2.items():
        barcodes = barcodeSet(barcode)
        for bc in barcodes:
            r2[bc] = name
    for barcode, name in R3.items():
        barcodes = barcodeSetShift2(barcode)
        # allow 2 base shift for R3 only
        for bc in barcodes:
            r3[bc] = name
    for barcode, name in P5.items():
        barcodes = barcodeSet(barcode)
        for bc in barcodes:
            p5[bc] = name
#    print("Updating RGIDs, with barcode correction")
    for read in bam.fetch():
        barcodeMatch = 0
        name = read.query_name
        nameIndex1 = name.find('_1:N:0:')
        nameIndex2 = name.find('_2:N:0:')
        if (nameIndex1 == -1):
            nameIndex = nameIndex2
        else:
            nameIndex = nameIndex1
        barcodeRaw = name[nameIndex + 7:]
#        print(barcodeRaw)
        newName = name[:nameIndex]
        barcode = ""
        if barcodeRaw[15:23] in r1:
            barcode = r1[barcodeRaw[15:23]]
            barcodeMatch += 1
        else:
            barcode = barcodeRaw[15:23]
        if barcodeRaw[53:61] in r2:
            barcode = barcode + "," + r2[barcodeRaw[53:61]]
            barcodeMatch += 1
        else:
            barcode = barcode + "," + barcodeRaw[53:61]
#        print(barcodeRaw[-17:-9])
        if barcodeRaw[-17:-9] in r3:
            barcode = barcode + "," + r3[barcodeRaw[-17:-9]]
            barcodeMatch += 1
        else:
            barcode = barcode + barcodeRaw[-17:-9]
#        print(barcodeRaw[-8:])
        if barcodeRaw[-8:] in p5:
            barcode = barcode + "," + p5[barcodeRaw[-8:]]
            barcodeMatch += 1
        else:
            barcode = barcode + barcodeRaw[-8:]
        read.set_tag('RG', barcode)
        if (libtype == 'RNA' ) :
            newName2 = newName[:nameIndex - 11] + "_" + barcode + "_" + newName[nameIndex - 10: ]
        elif (libtype == 'crop' ) :
            newName2 = newName[:nameIndex - 11] + "_" + barcode + "_" + newName[nameIndex - 10: ] 
        elif (libtype == 'Cellhash' ) :
            newName2 = newName[:nameIndex - 11] + "_" + barcode + "_" + newName[nameIndex - 10: ]
        else:
            newName2 = newName + "_" + barcode
        read.query_name = newName2
        if (barcodeMatch == 4):
            out.write(read)
#            if not (barcode in barcodeNames):
#                barcodeNames.add(barcode)
        else:
            err.write(read)
    bam.close()
    out.close()
    err.close()
#    oldHead = pysam.view("-H", outfile)
#    newRG = ""
#    count = 0
#    for bc in barcodeNames:
#        newRG = newRG + "@RG\tID:" + bc + "\tSM:Barcode" + '{:09d}'.format(count) + "\n"  # noqa
#        count += 1
#    subprocess.run(newRG)
#    startRG = oldHead.find("@RG")
#    endRG = oldHead.find("\n", startRG) + 1
#    newHead = oldHead[:startRG] + newRG + oldHead[endRG:]
#    head = open(outfile[:-4] + ".header.sam", 'w')
#    head.write(newHead)
#    head.close()


def main():
    parser = argparse.ArgumentParser(
        description="Updates bam file RGID for splitATAC barcoding",
        epilog="Intended for splitATAC data")
    parser.add_argument(
        "--bam",
        metavar="Input",
        required=True,
        help="Path to unlabeled bamfile for splitATAC sample")
    parser.add_argument(
        "--out",
        metavar="Output",
        required=True,
        help="Path for updated bamfile should be saved")
    parser.add_argument(
        "--err",
        metavar="Discard",
        required=True,
        help="Path for bamfile of low quality barcodes")
    parser.add_argument(
        "--libtype",
        metavar="Libtype",
        required=True,
        help="Tyoe of lib RNA or ATAC")
    args = parser.parse_args()
    pysam.index(args.bam)
    updateRGID(args.bam, args.out, args.err, args.libtype)
    pysam.index(args.out)


main()
