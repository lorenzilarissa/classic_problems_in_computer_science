
# convert string to bits

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

# compressation

def _compress(self, gene: str) -> None:
    self.bit_string: int = 1                # sentinel
    for nucleotide in gene.upper():
        self.bit_string <<= 2               # dislocate two bits to the left
        if nucleotide == 'A':               # change the last two bits to 00 (zero zero)
            self.bit_string |= 0b00
        elif nucleotide == 'C':             # change the last two bits to 01 (zero one)
            self.bit_string |= 0b01
        elif nucleotide == 'G':             # change the last two bits to 10 (one zero)
            self.bit_string |= 0b10
        elif nucleotide == 'T':             # change the last two bits to 11 (one one)
            self.bit_string |= 0b11
        else:
            raise ValueError('Invalid Nucleotide: {}.'.format(nucleotide))

# decompressation

def decompress(self) -> str:
    gene: str = ''
    for i in range(0, self.bit_string.bit_lenght() - 1, 2):         # - 1 to exclude the sentinel
        bits: int = self.bit_string >> i & 0b11                     # takes only two relevant bits
        if bits == 0b00:
            gene += 'A'
        elif bits == 0b01:
            gene += 'C'
        elif bits == 0b10:
            gene += 'G'
        elif bits == 0b11:
            gene += 'T'
        else:
            raise ValueError('Invalid bits: {}.'.format(bits))
    return gene[:: -1]                                              # invert the string 

def __str__(self) -> str:
    return self.decompress()

# testing

if __name__ == '__main__':
    from sys import getsizeof
    original: str = 'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATTAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA' * 100
    print('original is {} bytes.'.format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print('compressed is {} bytes.'.format(getsizeof(compressed.bit_string)))
    print(compressed)
    print('original and decompressed are the same: {}.'.format(original == compressed.decompress()))
