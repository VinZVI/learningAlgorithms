import cProfile

import numpy


def restor_result(ans, prev, k):
    l = [1 for _ in range(ans)]
    j = ans - 1
    while k > 0:
        l[j] = k + 1
        j -= 1
        k = prev[k]
    return l


def CeilIndex(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] <= key):
            r = m
        else:
            l = m
    return r


from bisect import bisect_right


def LongestIncreasingSubsequenceLength2(v):
    if len(v) == 0:  # boundary case
        return 0

    tail = [0 for i in range(len(v) + 1)]
    length = 1  # always points empty slot in tail

    tail[0] = v[0]

    for i in range(1, len(v)):
        if v[i] > tail[length - 1]:
            # v[i] extends the largest subsequence
            tail[length] = v[i]
            length += 1

        else:
            # v[i] will extend a subsequence and discard older subsequence

            # find the largest value just smaller than v[i] in tail

            # to find that value do binary search for the v[i] in
            # the range from begin to 0 + length

            # bisect function either returns index where element is found
            # or the appropriate index at which element should be placed

            # finally replace the existing subsequence with new end value
            tail[bisect_right(tail, v[i], 0, length - 1)] = v[i]

    return length


def LongestIncreasingSubsequenceLength(A, size):
    A = [i * -1 for i in A]
    prev = [0] * size
    tailTable = [0] * (size + 1)
    tailTable[0] = A[0]
    prev[0] = 0
    len = 1
    for i in range(1, size):

        # if (A[i] > tailTable[0]):
        #     tailTable[0] = A[i]
        #     prev[i] = 0

        if (A[i] >= tailTable[len - 1]):
            tailTable[len] = A[i]
            prev[i] = len
            len += 1

        else:
            # tail[bisect_right(tail, v[i], 0, length - 1)] = v[i]
            j = bisect_right(tailTable, A[i], 0, len - 1)

            # while tailTable[j] == A[i]:
            #     j += 1
            prev[i] = j
            tailTable[j] = A[i]

    # print(A)
    # print(tailTable)
    # print(prev)
    l = restor_result2(len, prev, size)
    return len, l


def restor_result2(ans, prev, size):
    l = [0] * ans
    for i in range(size - 1, 0, -1):
        if prev[i] == ans - 1:
            l[ans - 1] = i + 1
            ans -= 1
        if ans < 0:
            break

    return l



def input_data():
    array_numbers = []
    # n = int("1000")
    n = 100000
    #
    array_numbers = numpy.random.randint(0, 1, n)
    # array_numbers = list(map(int,
    #                      '672 170 845 468 829 106 772 998 754 824 50 89 297 664 5 257 295 578 750 921 979 821 503 682 349 683 732 166 937 474 322 683 747 476 428 110 676 86 208 850 806 94 590 554 635 749 441 512 764 839 884 19 117 620 390 61 460 230 651 677 543 691 244 959 492 654 32 749 83 318 888 257 582 65 34 682 167 550 196 241 705 589 54 766 535 604 840 512 437 872 492 287 388 410 914 7 761 701 422 179 273 516 127 906 570 424 125 980 582 672 291 456 652 921 784 672 474 324 345 791 743 949 339 821 700 331 755 3 199 915 216 454 720 383 305 959 127 243 445 159 799 731 889 646 752 63 996 863 446 910 252 294 116 842 43 563 938 78 565 979 96 339 280 781 586 899 354 180 588 858 326 207 830 948 290 452 249 977 6 993 144 608 297 190 918 127 103 789 80 783 457 335 415 205 679 429 430 306 948 34 657 990 774 996 985 16 861 653 30 252 873 585 770 46 796 317 656 142 584 592 971 191 233 867 385 996 793 491 22 135 228 874 550 718 96 363 247 362 324 170 649 927 128 760 577 642 919 14 748 501 777 643 610 925 365 63 322 132 533 749 822 243 267 924 93 82 935 360 80 320 587 821 350 596 198 32 636 613 141 245 56 980 50 230 606 404 579 868 312 137 88 902 500 276 135 229 842 145 136 169 886 479 776 78 599 21 749 367 56 433 340 271 848 685 928 593 633 220 320 950 606 672 93 547 949 745 572 121 542 744 295 325 700 953 326 468 554 177 824 797 37 236 206 805 27 820 59 394 738 352 561 925 871 397 514 860 26 460 740 162 474 874 862 255 558 688 790 611 428 388 566 195 187 56 502 896 597 928 662 651 960 333 583 295 415 341 492 814 151 991 909 861 212 483 93 642 997 235 251 546 242 444 932 19 925 803 134 172 32 408 260 582 724 459 279 951 383 619 374 505 206 462 885 457 100 686 312 284 631 513 138 594 441 695 82 626 307 473 763 534 386 313 274 579 840 110 832 245 968 569 958 353 612 175 368 370 320 736 804 69 317 814 216 642 604 806 100 794 791 17 791 630 903 618 316 136 502 349 396 911 174 356 679 346 169 414 619 28 284 122 264 208 505 75 394 842 710 425 937 848 505 749 575 745 776 749 815 43 9 687 447 178 729 273 48 48 771 279 810 291 986 512 414 386 60 388 257 590 95 572 547 3 183 117 132 473 811 946 863 501 330 21 708 46 558 925 547 940 573 480 890 955 631 834 434 7 438 422 715 283 699 787 887 439 962 659 235 793 797 758 646 88 309 52 979 213 559 3 647 325 118 221 434 981 1000 449 748 546 399 619 91 104 70 704 679 29 902 17 822 944 577 566 226 362 952 256 53 132 23 394 887 141 527 971 125 378 26 802 374 664 863 411 334 699 660 91 71 551 833 61 915 992 839 116 129 332 64 460 712 610 547 73 557 687 896 871 189 496 736 24 616 981 4 685 743 272 875 834 402 319 412 800 724 590 737 220 995 696 516 910 148 167 472 309 553 619 558 17 303 904 894 589 90 399 590 221 882 753 408 705 228 400 998 626 18 175 580 250 468 862 872 311 610 606 165 230 31 267 778 567 73 93 327 103 294 456 880 713 7 350 844 570 257 169 740 596 124 991 959 699 863 321 47 838 809 687 289 847 628 191 112 60 790 316 521 740 48 523 495 70 494 988 45 519 181 606 30 416 341 695 902 63 653 988 227 485 832 568 187 886 508 195 392 945 471 713 758 532 586 766 305 353 803 308 8 215 777 983 17 24 296 487 270 678 376 972 222 513 150 904 36 763 900 264 334 946 703 971 610 677 942 941 491 818 67 624 715 493 281 163 581 228 364 254 162 452 524 22 318 129 149 780 471 636 585 126 79 1 875 2 664 257 772 510 41 110 711 279 356 547 57 437 6 936 774 949 643 876 990 705 92 600 562 856 492 196 754 679 187 305 131 710 340 378 16 437 16 147 993 967 248 739 979 384 825 208 371 421 688 276 905 974 248 900 284 700 451 962 217 327 418 48 26 43 47 579 151 592 589 927 694 379 295 517 846 886 541 350 333 844 413 852 289 942 920 488 622 437 127 292 904 603 172 743 793 619 978 577 754 983 171 762 632 501 67 110 44 280 860 213 180 816 405 427 355 543 982 513 861 461 484 990 418 349 394 468 202 840 435 900 953 189 555 724 431 694 63 35 860 57 703 601 927 3 525 624 441 947 696 733 13 637 729 108 563 310 452 924 514 777'.split()))
    return n, array_numbers


def input_file():
    # array_numbers = []
    with open("exmpl.txt", 'r') as file:
        n = int(file.readline().strip())
        # print(n)
        array_numbers = list(map(int, file.readline().split()))
    return n, array_numbers


def main():
    n, array_numbers = input_data()
    ans, x = LongestIncreasingSubsequenceLength(array_numbers, n)
    print(ans)
    #print(*x, sep=' ')


if __name__ == "__main__":
    cProfile.run("main()")
